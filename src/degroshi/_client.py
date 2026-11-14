"""The Degroshi API client: ``Degroshi`` (blocking) and ``AsyncDegroshi``. Both share the resource classes;
a mode object decides whether a call blocks or returns a coroutine. Amounts come back as ``Decimal``."""

from __future__ import annotations

import builtins
import os
import uuid
from collections.abc import AsyncIterator, Iterator, Mapping
from dataclasses import dataclass
from types import ModuleType
from typing import TYPE_CHECKING, Any, Generic, Self, TypeVar

import httpx2

from . import webhooks
from ._errors import ApiConnectionError, ApiTimeoutError, error_from_response
from ._generated.api.accounts import get_account, get_accounts_net_worth, list_accounts
from ._generated.api.analytics import (
    get_analytics_cash_flow,
    get_analytics_categories,
    get_analytics_merchants,
    get_analytics_net_worth,
    get_analytics_spending,
    get_analytics_summary,
    get_analytics_trends,
)
from ._generated.api.budgets import get_budget, list_budgets
from ._generated.api.categories import get_category, list_categories
from ._generated.api.changes import list_changes
from ._generated.api.events import get_event, list_events
from ._generated.api.me import list_my_spaces
from ._generated.api.recurring_transactions import (
    get_recurring_transaction,
    list_recurring_occurrences,
    list_recurring_transactions,
)
from ._generated.api.sources import (
    create_source,
    delete_source,
    delete_source_transaction,
    get_source,
    list_source_transactions,
    list_sources,
    push_source_balances,
    push_source_transactions,
    update_source,
    upsert_source_account,
)
from ._generated.api.transactions import (
    create_transaction,
    delete_transaction,
    get_transaction,
    get_transaction_day_totals,
    list_transactions,
    update_transaction,
)
from ._generated.client import AuthenticatedClient
from ._generated.models import (
    AccountListResponse,
    AccountResponse,
    BalanceBatchRequest,
    BalanceBatchResponse,
    BudgetListItem,
    BudgetResponse,
    CashFlowResponse,
    Category,
    CategoryAnalyticsResponse,
    Change,
    ChangesResponse,
    CreateSourceRequest,
    CreateTransactionRequest,
    DayTotalsResponse,
    Event,
    EventListPageEnvelope,
    MerchantAnalyticsResponse,
    Meta,
    MySpaceResponse,
    NetWorthResponse,
    NetWorthTimeSeriesResponse,
    OccurrencesResponse,
    PushBatchRequest,
    PushBatchResponse,
    PushedPage,
    PushedRow,
    RecurringResponse,
    SourceResponse,
    SpendingResponse,
    SummaryResponse,
    TransactionResponse,
    TrendsResponse,
    UpdateSourceRequest,
    UpdateTransactionRequest,
    UpsertAccountRequest,
    UpsertAccountResponse,
)
from ._generated.types import Unset
from ._retry import AsyncRetryTransport, RetryTransport
from ._version import __version__

DEFAULT_BASE_URL = "https://api.degroshi.com"

Row = TypeVar("Row")
Body = TypeVar("Body")


@dataclass
class Page(Generic[Row]):
    """A page of a numbered list: the rows and ``meta`` (page, per_page, total, has_next…)."""

    data: list[Row]
    meta: Meta


def _envelope(response: Any) -> Any:
    if 200 <= int(response.status_code) < 300:
        return response.parsed
    raise error_from_response(int(response.status_code), response.content, response.headers)


def _transport_error(error: httpx2.TransportError) -> ApiConnectionError:
    if isinstance(error, httpx2.TimeoutException):
        return ApiTimeoutError(str(error))
    return ApiConnectionError(str(error))


def _data(envelope: Any) -> Any:
    return getattr(envelope, "data", None)


class _SyncMode:
    def __init__(self, client: AuthenticatedClient) -> None:
        self.client = client

    def envelope(self, module: ModuleType, *args: Any, **kwargs: Any) -> Any:
        try:
            response = module.sync_detailed(*args, client=self.client, **kwargs)
        except httpx2.TransportError as error:
            raise _transport_error(error) from error
        return _envelope(response)

    def one(self, module: ModuleType, *args: Any, **kwargs: Any) -> Any:
        return _data(self.envelope(module, *args, **kwargs))

    def page(self, module: ModuleType, *args: Any, **kwargs: Any) -> Page[Any]:
        envelope = self.envelope(module, *args, **kwargs)
        return Page(data=list(_data(envelope) or []), meta=getattr(envelope, "meta", None))

    def done(self, module: ModuleType, *args: Any, **kwargs: Any) -> None:
        self.envelope(module, *args, **kwargs)

    def numbered(self, module: ModuleType, per_page: int, **query: Any) -> Iterator[Any]:
        page = int(query.pop("page", 1) or 1)
        while True:
            result = self.page(module, page=page, per_page=per_page, **query)
            yield from result.data
            if not result.data or not getattr(result.meta, "has_next", False):
                return
            page += 1

    def events(self, **query: Any) -> Iterator[Any]:
        while True:
            envelope = self.envelope(list_events, **query)
            rows = list(_data(envelope) or [])
            yield from rows
            meta = getattr(envelope, "meta", None)
            if not rows or not getattr(meta, "has_more", False):
                return
            query["starting_after"] = rows[-1].id

    def pushed(self, source_id: str, **query: Any) -> Iterator[Any]:
        while True:
            page = self.one(list_source_transactions, source_id, **query)
            yield from getattr(page, "items", None) or []
            cursor = getattr(page, "next_cursor", None)
            if not isinstance(cursor, str) or not cursor:
                return
            query["cursor"] = cursor

    def change_feed(self, cursor: str | None, query: dict[str, Any]) -> ChangeFeed:
        return ChangeFeed(self, cursor, query)


class _AsyncMode:
    def __init__(self, client: AuthenticatedClient) -> None:
        self.client = client

    async def envelope(self, module: ModuleType, *args: Any, **kwargs: Any) -> Any:
        try:
            response = await module.asyncio_detailed(*args, client=self.client, **kwargs)
        except httpx2.TransportError as error:
            raise _transport_error(error) from error
        return _envelope(response)

    async def one(self, module: ModuleType, *args: Any, **kwargs: Any) -> Any:
        return _data(await self.envelope(module, *args, **kwargs))

    async def page(self, module: ModuleType, *args: Any, **kwargs: Any) -> Page[Any]:
        envelope = await self.envelope(module, *args, **kwargs)
        return Page(data=list(_data(envelope) or []), meta=getattr(envelope, "meta", None))

    async def done(self, module: ModuleType, *args: Any, **kwargs: Any) -> None:
        await self.envelope(module, *args, **kwargs)

    async def numbered(self, module: ModuleType, per_page: int, **query: Any) -> AsyncIterator[Any]:
        page = int(query.pop("page", 1) or 1)
        while True:
            result = await self.page(module, page=page, per_page=per_page, **query)
            for row in result.data:
                yield row
            if not result.data or not getattr(result.meta, "has_next", False):
                return
            page += 1

    async def events(self, **query: Any) -> AsyncIterator[Any]:
        while True:
            envelope = await self.envelope(list_events, **query)
            rows = list(_data(envelope) or [])
            for row in rows:
                yield row
            meta = getattr(envelope, "meta", None)
            if not rows or not getattr(meta, "has_more", False):
                return
            query["starting_after"] = rows[-1].id

    async def pushed(self, source_id: str, **query: Any) -> AsyncIterator[Any]:
        while True:
            page = await self.one(list_source_transactions, source_id, **query)
            for row in getattr(page, "items", None) or []:
                yield row
            cursor = getattr(page, "next_cursor", None)
            if not isinstance(cursor, str) or not cursor:
                return
            query["cursor"] = cursor

    def change_feed(self, cursor: str | None, query: dict[str, Any]) -> AsyncChangeFeed:
        return AsyncChangeFeed(self, cursor, query)


def _with_cursor(query: dict[str, Any], cursor: str | None) -> dict[str, Any]:
    return {**query, "cursor": cursor} if cursor else dict(query)


class ChangeFeed:
    """Every change since a cursor, page after page (``GET /v1/changes``), for keeping a copy.

    ``feed.cursor`` is where the next read starts: save it after the loop and pass it as ``cursor`` next time.
    Stopping early is safe: reading from it again repeats at most the rest of a page (apply changes by id). A cursor
    that can't continue raises a ``DegroshiError`` with status 410 (``CHANGES_RESYNC_REQUIRED``): read again without
    one and replace the copy.

    >>> feed = degroshi.changes.iterate(cursor=saved, types=["transaction"])
    >>> for change in feed:
    ...     if change.op == "delete":
    ...         copy.pop(change.id, None)
    ...     else:
    ...         copy[change.id] = change.data
    >>> save(feed.cursor)
    """

    def __init__(self, mode: _SyncMode, cursor: str | None, query: dict[str, Any]) -> None:
        #: Where reading again starts: the start of the page being read, then each page's next_cursor.
        self.cursor = cursor
        self._mode = mode
        self._query = query

    def __iter__(self) -> Iterator[Change]:
        while True:
            page = self._mode.one(list_changes, **_with_cursor(self._query, self.cursor))
            yield from page.items or []
            self.cursor = page.next_cursor
            if not page.has_more:
                return


class AsyncChangeFeed:
    """``ChangeFeed`` for ``AsyncDegroshi``: ``async for change in feed``, then save ``feed.cursor``."""

    def __init__(self, mode: _AsyncMode, cursor: str | None, query: dict[str, Any]) -> None:
        self.cursor = cursor
        self._mode = mode
        self._query = query

    async def __aiter__(self) -> AsyncIterator[Change]:
        while True:
            page = await self._mode.one(list_changes, **_with_cursor(self._query, self.cursor))
            for change in page.items or []:
                yield change
            self.cursor = page.next_cursor
            if not page.has_more:
                return


def _key(idempotency_key: str | None) -> str:
    return idempotency_key or str(uuid.uuid4())


def _body(model: type[Body], body: Body | Mapping[str, Any]) -> Body:
    """A request body: the model itself, or a plain dict in the API's JSON shape (read with ``model.from_dict``)."""
    if isinstance(body, Mapping):
        return model.from_dict(body)  # type: ignore[attr-defined, no-any-return]
    return body


def _if_match(version: str | int | Unset | None) -> dict[str, str]:
    """A row's ``version`` as If-Match; a response without one (``None`` or unset) sends no precondition."""
    return {} if version is None or isinstance(version, Unset) else {"if_match": str(version)}


class _Resource:
    def __init__(self, mode: _SyncMode | _AsyncMode) -> None:
        self._m = mode


# Annotations: these classes are typed for ``Degroshi`` (a call returns its result). ``AsyncDegroshi`` uses the same
# classes at runtime; type checkers see the ``Async…`` twins declared under TYPE_CHECKING below, where the same calls
# are awaited. ``builtins.list`` because a method named ``list`` hides the builtin inside its class.


class Spaces(_Resource):
    def list(self) -> builtins.list[MySpaceResponse]:
        """The spaces the token reaches."""
        return self._m.one(list_my_spaces)


class Accounts(_Resource):
    def list(self, **query: Any) -> builtins.list[AccountListResponse]:
        return self._m.one(list_accounts, **query)

    def get(self, account_id: str) -> AccountResponse:
        return self._m.one(get_account, account_id)

    def net_worth(self, **query: Any) -> NetWorthResponse:
        return self._m.one(get_accounts_net_worth, **query)


class Transactions(_Resource):
    def list(self, **query: Any) -> Page[TransactionResponse]:
        """One page; ``meta.has_next`` says whether another follows."""
        return self._m.page(list_transactions, **query)

    def iterate(self, *, per_page: int = 100, **query: Any) -> Iterator[TransactionResponse]:
        """Every matching transaction, page after page (``for``, or ``async for`` on AsyncDegroshi)."""
        return self._m.numbered(list_transactions, per_page, **query)

    def get(self, transaction_id: str) -> TransactionResponse:
        return self._m.one(get_transaction, transaction_id)

    def create(
        self, body: CreateTransactionRequest | Mapping[str, Any], *, idempotency_key: str | None = None
    ) -> TransactionResponse:
        """Safe to retry: an Idempotency-Key is sent (one is made for you when you don't pass it)."""
        return self._m.one(
            create_transaction, body=_body(CreateTransactionRequest, body), idempotency_key=_key(idempotency_key)
        )

    def update(
        self,
        transaction_id: str,
        body: UpdateTransactionRequest | Mapping[str, Any],
        *,
        if_match: str | int | Unset | None = None,
    ) -> TransactionResponse:
        """``if_match`` is the row's ``version``; the API answers 412 (ConflictError) when it changed meanwhile."""
        return self._m.one(
            update_transaction, transaction_id, body=_body(UpdateTransactionRequest, body), **_if_match(if_match)
        )

    def delete(self, transaction_id: str, *, if_match: str | int | Unset | None = None) -> None:
        return self._m.done(delete_transaction, transaction_id, **_if_match(if_match))

    def day_totals(self, **query: Any) -> DayTotalsResponse:
        return self._m.one(get_transaction_day_totals, **query)


class Categories(_Resource):
    def list(self, **query: Any) -> builtins.list[Category]:
        return self._m.one(list_categories, **query)

    def get(self, category_id: str) -> Category:
        return self._m.one(get_category, category_id)


class Budgets(_Resource):
    def list(self, **query: Any) -> builtins.list[BudgetListItem]:
        return self._m.one(list_budgets, **query)

    def get(self, budget_id: str) -> BudgetResponse:
        return self._m.one(get_budget, budget_id)


class Recurring(_Resource):
    def list(self, **query: Any) -> builtins.list[RecurringResponse]:
        return self._m.one(list_recurring_transactions, **query)

    def get(self, rule_id: str) -> RecurringResponse:
        return self._m.one(get_recurring_transaction, rule_id)

    def occurrences(self, **query: Any) -> OccurrencesResponse:
        return self._m.one(list_recurring_occurrences, **query)


class Analytics(_Resource):
    def summary(self, **query: Any) -> SummaryResponse:
        return self._m.one(get_analytics_summary, **query)

    def cash_flow(self, **query: Any) -> CashFlowResponse:
        return self._m.one(get_analytics_cash_flow, **query)

    def categories(self, **query: Any) -> CategoryAnalyticsResponse:
        return self._m.one(get_analytics_categories, **query)

    def spending(self, **query: Any) -> SpendingResponse:
        return self._m.one(get_analytics_spending, **query)

    def trends(self, **query: Any) -> TrendsResponse:
        return self._m.one(get_analytics_trends, **query)

    def merchants(self, **query: Any) -> MerchantAnalyticsResponse:
        return self._m.one(get_analytics_merchants, **query)

    def net_worth(self, **query: Any) -> NetWorthTimeSeriesResponse:
        return self._m.one(get_analytics_net_worth, **query)


class Sources(_Resource):
    """Custom sources: push accounts, transactions and balances from your own system."""

    def list(self) -> builtins.list[SourceResponse]:
        return self._m.one(list_sources)

    def get(self, source_id: str) -> SourceResponse:
        return self._m.one(get_source, source_id)

    def create(
        self, body: CreateSourceRequest | Mapping[str, Any], *, idempotency_key: str | None = None
    ) -> SourceResponse:
        return self._m.one(create_source, body=_body(CreateSourceRequest, body), idempotency_key=_key(idempotency_key))

    def update(self, source_id: str, body: UpdateSourceRequest | Mapping[str, Any]) -> SourceResponse:
        return self._m.one(update_source, source_id, body=_body(UpdateSourceRequest, body))

    def delete(self, source_id: str) -> None:
        return self._m.done(delete_source, source_id)

    def upsert_account(
        self, source_id: str, external_id: str, body: UpsertAccountRequest | Mapping[str, Any]
    ) -> UpsertAccountResponse:
        return self._m.one(upsert_source_account, source_id, external_id, body=_body(UpsertAccountRequest, body))

    def push_transactions(
        self, source_id: str, body: PushBatchRequest | Mapping[str, Any], *, idempotency_key: str | None = None
    ) -> PushBatchResponse:
        """Up to 500 rows; safe to retry."""
        return self._m.one(
            push_source_transactions,
            source_id,
            body=_body(PushBatchRequest, body),
            idempotency_key=_key(idempotency_key),
        )

    def push_balances(
        self, source_id: str, body: BalanceBatchRequest | Mapping[str, Any], *, idempotency_key: str | None = None
    ) -> BalanceBatchResponse:
        return self._m.one(
            push_source_balances,
            source_id,
            body=_body(BalanceBatchRequest, body),
            idempotency_key=_key(idempotency_key),
        )

    def list_pushed(self, source_id: str, **query: Any) -> PushedPage:
        """What the space holds from the source, newest first, one page (``next_cursor`` for the next)."""
        return self._m.one(list_source_transactions, source_id, **query)

    def iterate_pushed(self, source_id: str, **query: Any) -> Iterator[PushedRow]:
        return self._m.pushed(source_id, **query)

    def delete_pushed(self, source_id: str, account: str, external_id: str) -> None:
        return self._m.done(delete_source_transaction, source_id, account, external_id)


class Changes(_Resource):
    """What changed in the space since a cursor, deletions included, in the order the changes were saved."""

    def list(self, **query: Any) -> ChangesResponse:
        """One page: ``items``, ``next_cursor`` (keep it, even when ``items`` is empty) and ``has_more``."""
        return self._m.one(list_changes, **query)

    def iterate(self, *, cursor: str | None = None, **query: Any) -> ChangeFeed:
        """Every change since ``cursor`` (every object first without one); ``feed.cursor`` is where to start next."""
        return self._m.change_feed(cursor, query)


class Events(_Resource):
    """The space's events of the last 30 days, as webhook endpoints receive them."""

    def list(self, **query: Any) -> EventListPageEnvelope:
        """One page: ``data`` and ``meta.has_more``."""
        return self._m.envelope(list_events, **query)

    def iterate(self, **query: Any) -> Iterator[Event]:
        return self._m.events(**query)

    def get(self, event_id: str) -> Event:
        return self._m.one(get_event, event_id)


class Webhooks:
    """``client.webhooks.verify(raw_body, headers["Degroshi-Signature"], secret)``."""

    verify = staticmethod(webhooks.verify)


if TYPE_CHECKING:
    # What ``AsyncDegroshi`` hands out, for type checkers: the classes above with each call awaited and each iterator
    # an ``async for``. tests/unit/test_types.py keeps these in step with the classes above.

    class AsyncSpaces(_Resource):
        async def list(self) -> builtins.list[MySpaceResponse]: ...

    class AsyncAccounts(_Resource):
        async def list(self, **query: Any) -> builtins.list[AccountListResponse]: ...
        async def get(self, account_id: str) -> AccountResponse: ...
        async def net_worth(self, **query: Any) -> NetWorthResponse: ...

    class AsyncTransactions(_Resource):
        async def list(self, **query: Any) -> Page[TransactionResponse]: ...
        def iterate(self, *, per_page: int = 100, **query: Any) -> AsyncIterator[TransactionResponse]: ...
        async def get(self, transaction_id: str) -> TransactionResponse: ...
        async def create(
            self, body: CreateTransactionRequest | Mapping[str, Any], *, idempotency_key: str | None = None
        ) -> TransactionResponse: ...
        async def update(
            self,
            transaction_id: str,
            body: UpdateTransactionRequest | Mapping[str, Any],
            *,
            if_match: str | int | Unset | None = None,
        ) -> TransactionResponse: ...
        async def delete(self, transaction_id: str, *, if_match: str | int | Unset | None = None) -> None: ...
        async def day_totals(self, **query: Any) -> DayTotalsResponse: ...

    class AsyncCategories(_Resource):
        async def list(self, **query: Any) -> builtins.list[Category]: ...
        async def get(self, category_id: str) -> Category: ...

    class AsyncBudgets(_Resource):
        async def list(self, **query: Any) -> builtins.list[BudgetListItem]: ...
        async def get(self, budget_id: str) -> BudgetResponse: ...

    class AsyncRecurring(_Resource):
        async def list(self, **query: Any) -> builtins.list[RecurringResponse]: ...
        async def get(self, rule_id: str) -> RecurringResponse: ...
        async def occurrences(self, **query: Any) -> OccurrencesResponse: ...

    class AsyncAnalytics(_Resource):
        async def summary(self, **query: Any) -> SummaryResponse: ...
        async def cash_flow(self, **query: Any) -> CashFlowResponse: ...
        async def categories(self, **query: Any) -> CategoryAnalyticsResponse: ...
        async def spending(self, **query: Any) -> SpendingResponse: ...
        async def trends(self, **query: Any) -> TrendsResponse: ...
        async def merchants(self, **query: Any) -> MerchantAnalyticsResponse: ...
        async def net_worth(self, **query: Any) -> NetWorthTimeSeriesResponse: ...

    class AsyncSources(_Resource):
        async def list(self) -> builtins.list[SourceResponse]: ...
        async def get(self, source_id: str) -> SourceResponse: ...
        async def create(
            self, body: CreateSourceRequest | Mapping[str, Any], *, idempotency_key: str | None = None
        ) -> SourceResponse: ...
        async def update(self, source_id: str, body: UpdateSourceRequest | Mapping[str, Any]) -> SourceResponse: ...
        async def delete(self, source_id: str) -> None: ...
        async def upsert_account(
            self, source_id: str, external_id: str, body: UpsertAccountRequest | Mapping[str, Any]
        ) -> UpsertAccountResponse: ...
        async def push_transactions(
            self, source_id: str, body: PushBatchRequest | Mapping[str, Any], *, idempotency_key: str | None = None
        ) -> PushBatchResponse: ...
        async def push_balances(
            self, source_id: str, body: BalanceBatchRequest | Mapping[str, Any], *, idempotency_key: str | None = None
        ) -> BalanceBatchResponse: ...
        async def list_pushed(self, source_id: str, **query: Any) -> PushedPage: ...
        def iterate_pushed(self, source_id: str, **query: Any) -> AsyncIterator[PushedRow]: ...
        async def delete_pushed(self, source_id: str, account: str, external_id: str) -> None: ...

    class AsyncChanges(_Resource):
        async def list(self, **query: Any) -> ChangesResponse: ...
        def iterate(self, *, cursor: str | None = None, **query: Any) -> AsyncChangeFeed: ...

    class AsyncEvents(_Resource):
        async def list(self, **query: Any) -> EventListPageEnvelope: ...
        def iterate(self, **query: Any) -> AsyncIterator[Event]: ...
        async def get(self, event_id: str) -> Event: ...

else:
    AsyncSpaces, AsyncAccounts, AsyncTransactions = Spaces, Accounts, Transactions
    AsyncCategories, AsyncBudgets, AsyncRecurring, AsyncAnalytics = Categories, Budgets, Recurring, Analytics
    AsyncSources, AsyncChanges, AsyncEvents = Sources, Changes, Events


def _client(
    api_key: str | None,
    space_id: str | None,
    base_url: str,
    timeout: float,
    transport: httpx2.BaseTransport | httpx2.AsyncBaseTransport,
    is_async: bool,
) -> AuthenticatedClient:
    key = api_key or os.environ.get("DEGROSHI_API_KEY")
    if not key:
        raise ValueError("degroshi: pass api_key or set DEGROSHI_API_KEY")
    headers = {"X-Degroshi-SDK": f"python/{__version__}"}
    if space_id:
        headers["X-Space-ID"] = space_id
    return AuthenticatedClient(
        base_url=base_url,
        token=key,
        prefix="",
        auth_header_name="X-API-Key",
        headers=headers,
        timeout=httpx2.Timeout(timeout),
        httpx_args={"transport": transport},
    )


class Degroshi:
    """The blocking client.

    >>> degroshi = Degroshi(api_key=os.environ["DEGROSHI_API_KEY"])
    >>> for transaction in degroshi.transactions.iterate(from_date=date(2026, 11, 1)):
    ...     print(transaction.amount)  # a Decimal
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        space_id: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        max_retries: int = 2,
        timeout: float = 60.0,
        transport: httpx2.BaseTransport | None = None,
    ) -> None:
        inner = transport or httpx2.HTTPTransport()
        #: The generated client underneath, for calling the generated functions directly.
        self.client = _client(api_key, space_id, base_url, timeout, RetryTransport(inner, max_retries), False)
        mode = _SyncMode(self.client)
        self.spaces = Spaces(mode)
        self.accounts = Accounts(mode)
        self.transactions = Transactions(mode)
        self.categories = Categories(mode)
        self.budgets = Budgets(mode)
        self.recurring = Recurring(mode)
        self.analytics = Analytics(mode)
        self.sources = Sources(mode)
        self.changes = Changes(mode)
        self.events = Events(mode)
        self.webhooks = Webhooks()

    def close(self) -> None:
        self.client.get_httpx_client().close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


class AsyncDegroshi:
    """The asyncio client: the same resources; calls are awaited and iterators are ``async for``."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        space_id: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        max_retries: int = 2,
        timeout: float = 60.0,
        transport: httpx2.AsyncBaseTransport | None = None,
    ) -> None:
        inner = transport or httpx2.AsyncHTTPTransport()
        self.client = _client(api_key, space_id, base_url, timeout, AsyncRetryTransport(inner, max_retries), True)
        mode = _AsyncMode(self.client)
        self.spaces = AsyncSpaces(mode)
        self.accounts = AsyncAccounts(mode)
        self.transactions = AsyncTransactions(mode)
        self.categories = AsyncCategories(mode)
        self.budgets = AsyncBudgets(mode)
        self.recurring = AsyncRecurring(mode)
        self.analytics = AsyncAnalytics(mode)
        self.sources = AsyncSources(mode)
        self.changes = AsyncChanges(mode)
        self.events = AsyncEvents(mode)
        self.webhooks = Webhooks()

    async def aclose(self) -> None:
        await self.client.get_async_httpx_client().aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()
