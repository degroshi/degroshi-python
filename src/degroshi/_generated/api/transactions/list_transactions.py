from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.list_transactions_sort import check_list_transactions_sort
from ...models.list_transactions_sort import ListTransactionsSort
from ...models.transaction_list_response_envelope import TransactionListResponseEnvelope
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    counterparty_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    recurring_rule_id: str | Unset = UNSET,
    import_id: str | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    sort: ListTransactionsSort | Unset = UNSET,
    needs_review: bool | Unset = UNSET,
    treatment_class: str | Unset = UNSET,
    include_portfolio_transfers: bool | Unset = UNSET,
    one_row_per_transfer: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["account_id"] = account_id

    json_account_ids: list[str] | Unset = UNSET
    if not isinstance(account_ids, Unset):
        json_account_ids = account_ids

    params["account_ids"] = json_account_ids

    params["category_id"] = category_id

    params["include_subcategories"] = include_subcategories

    params["uncategorized"] = uncategorized

    params["category_review"] = category_review

    params["type"] = type_

    params["status"] = status

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["from_date"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["to_date"] = json_to_date

    params["search"] = search

    params["min_amount"] = min_amount

    params["max_amount"] = max_amount

    json_tag_id: list[str] | Unset = UNSET
    if not isinstance(tag_id, Unset):
        json_tag_id = tag_id

    params["tag_id"] = json_tag_id

    params["counterparty_id"] = counterparty_id

    params["project_id"] = project_id

    params["recurring_rule_id"] = recurring_rule_id

    params["import_id"] = import_id

    params["currencyCode"] = currency_code

    json_updated_since: str | Unset = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["needs_review"] = needs_review

    params["treatment_class"] = treatment_class

    params["include_portfolio_transfers"] = include_portfolio_transfers

    params["one_row_per_transfer"] = one_row_per_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transactions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | TransactionListResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = TransactionListResponseEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | TransactionListResponseEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    counterparty_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    recurring_rule_id: str | Unset = UNSET,
    import_id: str | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    sort: ListTransactionsSort | Unset = UNSET,
    needs_review: bool | Unset = UNSET,
    treatment_class: str | Unset = UNSET,
    include_portfolio_transfers: bool | Unset = UNSET,
    one_row_per_transfer: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | TransactionListResponseEnvelope]:
    """List transactions

     The space's transactions, newest first, with filters and pagination. Split parts are nested in their
    parent. Each row carries its category, an explicit `direction` (income, expense, transfer_in,
    transfer_out) for the always-positive `amount`, its tags and, for a transfer leg, the other account.
    `tag_id` keeps rows carrying any of the given tags (repeated or comma separated). To catch up on
    changes, pass `updated_since` (RFC 3339) with `sort=updated_asc`: rows created or edited from then
    on, oldest change first. The row at the boundary comes again, so drop duplicates by `id` and
    `version`; deleted rows don't appear (the `transaction.deleted` event reports them).

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        category_id (str | Unset):
        include_subcategories (bool | Unset):
        uncategorized (bool | Unset):
        category_review (bool | Unset):
        type_ (str | Unset):
        status (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        tag_id (list[str] | Unset):
        counterparty_id (str | Unset):
        project_id (str | Unset):
        recurring_rule_id (str | Unset):
        import_id (str | Unset):
        currency_code (str | Unset):
        updated_since (datetime.datetime | Unset):
        sort (ListTransactionsSort | Unset):
        needs_review (bool | Unset):
        treatment_class (str | Unset):
        include_portfolio_transfers (bool | Unset):
        one_row_per_transfer (bool | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TransactionListResponseEnvelope]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        account_id=account_id,
        account_ids=account_ids,
        category_id=category_id,
        include_subcategories=include_subcategories,
        uncategorized=uncategorized,
        category_review=category_review,
        type_=type_,
        status=status,
        from_date=from_date,
        to_date=to_date,
        search=search,
        min_amount=min_amount,
        max_amount=max_amount,
        tag_id=tag_id,
        counterparty_id=counterparty_id,
        project_id=project_id,
        recurring_rule_id=recurring_rule_id,
        import_id=import_id,
        currency_code=currency_code,
        updated_since=updated_since,
        sort=sort,
        needs_review=needs_review,
        treatment_class=treatment_class,
        include_portfolio_transfers=include_portfolio_transfers,
        one_row_per_transfer=one_row_per_transfer,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    counterparty_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    recurring_rule_id: str | Unset = UNSET,
    import_id: str | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    sort: ListTransactionsSort | Unset = UNSET,
    needs_review: bool | Unset = UNSET,
    treatment_class: str | Unset = UNSET,
    include_portfolio_transfers: bool | Unset = UNSET,
    one_row_per_transfer: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | TransactionListResponseEnvelope | None:
    """List transactions

     The space's transactions, newest first, with filters and pagination. Split parts are nested in their
    parent. Each row carries its category, an explicit `direction` (income, expense, transfer_in,
    transfer_out) for the always-positive `amount`, its tags and, for a transfer leg, the other account.
    `tag_id` keeps rows carrying any of the given tags (repeated or comma separated). To catch up on
    changes, pass `updated_since` (RFC 3339) with `sort=updated_asc`: rows created or edited from then
    on, oldest change first. The row at the boundary comes again, so drop duplicates by `id` and
    `version`; deleted rows don't appear (the `transaction.deleted` event reports them).

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        category_id (str | Unset):
        include_subcategories (bool | Unset):
        uncategorized (bool | Unset):
        category_review (bool | Unset):
        type_ (str | Unset):
        status (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        tag_id (list[str] | Unset):
        counterparty_id (str | Unset):
        project_id (str | Unset):
        recurring_rule_id (str | Unset):
        import_id (str | Unset):
        currency_code (str | Unset):
        updated_since (datetime.datetime | Unset):
        sort (ListTransactionsSort | Unset):
        needs_review (bool | Unset):
        treatment_class (str | Unset):
        include_portfolio_transfers (bool | Unset):
        one_row_per_transfer (bool | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TransactionListResponseEnvelope
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        account_id=account_id,
        account_ids=account_ids,
        category_id=category_id,
        include_subcategories=include_subcategories,
        uncategorized=uncategorized,
        category_review=category_review,
        type_=type_,
        status=status,
        from_date=from_date,
        to_date=to_date,
        search=search,
        min_amount=min_amount,
        max_amount=max_amount,
        tag_id=tag_id,
        counterparty_id=counterparty_id,
        project_id=project_id,
        recurring_rule_id=recurring_rule_id,
        import_id=import_id,
        currency_code=currency_code,
        updated_since=updated_since,
        sort=sort,
        needs_review=needs_review,
        treatment_class=treatment_class,
        include_portfolio_transfers=include_portfolio_transfers,
        one_row_per_transfer=one_row_per_transfer,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    counterparty_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    recurring_rule_id: str | Unset = UNSET,
    import_id: str | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    sort: ListTransactionsSort | Unset = UNSET,
    needs_review: bool | Unset = UNSET,
    treatment_class: str | Unset = UNSET,
    include_portfolio_transfers: bool | Unset = UNSET,
    one_row_per_transfer: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | TransactionListResponseEnvelope]:
    """List transactions

     The space's transactions, newest first, with filters and pagination. Split parts are nested in their
    parent. Each row carries its category, an explicit `direction` (income, expense, transfer_in,
    transfer_out) for the always-positive `amount`, its tags and, for a transfer leg, the other account.
    `tag_id` keeps rows carrying any of the given tags (repeated or comma separated). To catch up on
    changes, pass `updated_since` (RFC 3339) with `sort=updated_asc`: rows created or edited from then
    on, oldest change first. The row at the boundary comes again, so drop duplicates by `id` and
    `version`; deleted rows don't appear (the `transaction.deleted` event reports them).

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        category_id (str | Unset):
        include_subcategories (bool | Unset):
        uncategorized (bool | Unset):
        category_review (bool | Unset):
        type_ (str | Unset):
        status (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        tag_id (list[str] | Unset):
        counterparty_id (str | Unset):
        project_id (str | Unset):
        recurring_rule_id (str | Unset):
        import_id (str | Unset):
        currency_code (str | Unset):
        updated_since (datetime.datetime | Unset):
        sort (ListTransactionsSort | Unset):
        needs_review (bool | Unset):
        treatment_class (str | Unset):
        include_portfolio_transfers (bool | Unset):
        one_row_per_transfer (bool | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TransactionListResponseEnvelope]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        account_id=account_id,
        account_ids=account_ids,
        category_id=category_id,
        include_subcategories=include_subcategories,
        uncategorized=uncategorized,
        category_review=category_review,
        type_=type_,
        status=status,
        from_date=from_date,
        to_date=to_date,
        search=search,
        min_amount=min_amount,
        max_amount=max_amount,
        tag_id=tag_id,
        counterparty_id=counterparty_id,
        project_id=project_id,
        recurring_rule_id=recurring_rule_id,
        import_id=import_id,
        currency_code=currency_code,
        updated_since=updated_since,
        sort=sort,
        needs_review=needs_review,
        treatment_class=treatment_class,
        include_portfolio_transfers=include_portfolio_transfers,
        one_row_per_transfer=one_row_per_transfer,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    counterparty_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    recurring_rule_id: str | Unset = UNSET,
    import_id: str | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    sort: ListTransactionsSort | Unset = UNSET,
    needs_review: bool | Unset = UNSET,
    treatment_class: str | Unset = UNSET,
    include_portfolio_transfers: bool | Unset = UNSET,
    one_row_per_transfer: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | TransactionListResponseEnvelope | None:
    """List transactions

     The space's transactions, newest first, with filters and pagination. Split parts are nested in their
    parent. Each row carries its category, an explicit `direction` (income, expense, transfer_in,
    transfer_out) for the always-positive `amount`, its tags and, for a transfer leg, the other account.
    `tag_id` keeps rows carrying any of the given tags (repeated or comma separated). To catch up on
    changes, pass `updated_since` (RFC 3339) with `sort=updated_asc`: rows created or edited from then
    on, oldest change first. The row at the boundary comes again, so drop duplicates by `id` and
    `version`; deleted rows don't appear (the `transaction.deleted` event reports them).

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        category_id (str | Unset):
        include_subcategories (bool | Unset):
        uncategorized (bool | Unset):
        category_review (bool | Unset):
        type_ (str | Unset):
        status (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        tag_id (list[str] | Unset):
        counterparty_id (str | Unset):
        project_id (str | Unset):
        recurring_rule_id (str | Unset):
        import_id (str | Unset):
        currency_code (str | Unset):
        updated_since (datetime.datetime | Unset):
        sort (ListTransactionsSort | Unset):
        needs_review (bool | Unset):
        treatment_class (str | Unset):
        include_portfolio_transfers (bool | Unset):
        one_row_per_transfer (bool | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TransactionListResponseEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            account_id=account_id,
            account_ids=account_ids,
            category_id=category_id,
            include_subcategories=include_subcategories,
            uncategorized=uncategorized,
            category_review=category_review,
            type_=type_,
            status=status,
            from_date=from_date,
            to_date=to_date,
            search=search,
            min_amount=min_amount,
            max_amount=max_amount,
            tag_id=tag_id,
            counterparty_id=counterparty_id,
            project_id=project_id,
            recurring_rule_id=recurring_rule_id,
            import_id=import_id,
            currency_code=currency_code,
            updated_since=updated_since,
            sort=sort,
            needs_review=needs_review,
            treatment_class=treatment_class,
            include_portfolio_transfers=include_portfolio_transfers,
            one_row_per_transfer=one_row_per_transfer,
            x_space_id=x_space_id,
        )
    ).parsed
