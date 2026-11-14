from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.day_totals_response_envelope import DayTotalsResponseEnvelope
from ...models.error_response import ErrorResponse
from ...models.get_transaction_day_totals_share import check_get_transaction_day_totals_share
from ...models.get_transaction_day_totals_share import GetTransactionDayTotalsShare
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    share: GetTransactionDayTotalsShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    if not isinstance(x_display_currency, Unset):
        headers["X-Display-Currency"] = x_display_currency

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    json_account_ids: list[str] | Unset = UNSET
    if not isinstance(account_ids, Unset):
        json_account_ids = account_ids

    params["account_ids"] = json_account_ids

    params["category_id"] = category_id

    json_category_ids: list[str] | Unset = UNSET
    if not isinstance(category_ids, Unset):
        json_category_ids = category_ids

    params["category_ids"] = json_category_ids

    params["include_subcategories"] = include_subcategories

    params["uncategorized"] = uncategorized

    params["category_review"] = category_review

    params["type"] = type_

    json_types: list[str] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types

    params["types"] = json_types

    params["status"] = status

    json_statuses: list[str] | Unset = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses

    params["statuses"] = json_statuses

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

    params["currencyCode"] = currency_code

    json_share: str | Unset = UNSET
    if not isinstance(share, Unset):
        json_share = share

    params["share"] = json_share

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transactions/day-totals",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DayTotalsResponseEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DayTotalsResponseEnvelope.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DayTotalsResponseEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    share: GetTransactionDayTotalsShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[DayTotalsResponseEnvelope | ErrorResponse]:
    """Daily totals of a list

     For the rows `GET /v1/transactions` lists with the same filters: what was spent and received per day
    (in the person's time zone), in the display currency (`currencyCode`, else the person's), newest day
    first, with the period's sums. Transfers and cancelled rows count in neither. A currency with no
    rate to the display currency is left out and named in `unconverted`. Pagination and sorting don't
    apply.

    Args:
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        category_id (str | Unset):
        category_ids (list[str] | Unset):
        include_subcategories (bool | Unset):
        uncategorized (bool | Unset):
        category_review (bool | Unset):
        type_ (str | Unset):
        types (list[str] | Unset):
        status (str | Unset):
        statuses (list[str] | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        tag_id (list[str] | Unset):
        currency_code (str | Unset):
        share (GetTransactionDayTotalsShare | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DayTotalsResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        account_ids=account_ids,
        category_id=category_id,
        category_ids=category_ids,
        include_subcategories=include_subcategories,
        uncategorized=uncategorized,
        category_review=category_review,
        type_=type_,
        types=types,
        status=status,
        statuses=statuses,
        from_date=from_date,
        to_date=to_date,
        search=search,
        min_amount=min_amount,
        max_amount=max_amount,
        tag_id=tag_id,
        currency_code=currency_code,
        share=share,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    share: GetTransactionDayTotalsShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> DayTotalsResponseEnvelope | ErrorResponse | None:
    """Daily totals of a list

     For the rows `GET /v1/transactions` lists with the same filters: what was spent and received per day
    (in the person's time zone), in the display currency (`currencyCode`, else the person's), newest day
    first, with the period's sums. Transfers and cancelled rows count in neither. A currency with no
    rate to the display currency is left out and named in `unconverted`. Pagination and sorting don't
    apply.

    Args:
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        category_id (str | Unset):
        category_ids (list[str] | Unset):
        include_subcategories (bool | Unset):
        uncategorized (bool | Unset):
        category_review (bool | Unset):
        type_ (str | Unset):
        types (list[str] | Unset):
        status (str | Unset):
        statuses (list[str] | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        tag_id (list[str] | Unset):
        currency_code (str | Unset):
        share (GetTransactionDayTotalsShare | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DayTotalsResponseEnvelope | ErrorResponse
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        account_ids=account_ids,
        category_id=category_id,
        category_ids=category_ids,
        include_subcategories=include_subcategories,
        uncategorized=uncategorized,
        category_review=category_review,
        type_=type_,
        types=types,
        status=status,
        statuses=statuses,
        from_date=from_date,
        to_date=to_date,
        search=search,
        min_amount=min_amount,
        max_amount=max_amount,
        tag_id=tag_id,
        currency_code=currency_code,
        share=share,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    share: GetTransactionDayTotalsShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[DayTotalsResponseEnvelope | ErrorResponse]:
    """Daily totals of a list

     For the rows `GET /v1/transactions` lists with the same filters: what was spent and received per day
    (in the person's time zone), in the display currency (`currencyCode`, else the person's), newest day
    first, with the period's sums. Transfers and cancelled rows count in neither. A currency with no
    rate to the display currency is left out and named in `unconverted`. Pagination and sorting don't
    apply.

    Args:
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        category_id (str | Unset):
        category_ids (list[str] | Unset):
        include_subcategories (bool | Unset):
        uncategorized (bool | Unset):
        category_review (bool | Unset):
        type_ (str | Unset):
        types (list[str] | Unset):
        status (str | Unset):
        statuses (list[str] | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        tag_id (list[str] | Unset):
        currency_code (str | Unset):
        share (GetTransactionDayTotalsShare | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DayTotalsResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        account_ids=account_ids,
        category_id=category_id,
        category_ids=category_ids,
        include_subcategories=include_subcategories,
        uncategorized=uncategorized,
        category_review=category_review,
        type_=type_,
        types=types,
        status=status,
        statuses=statuses,
        from_date=from_date,
        to_date=to_date,
        search=search,
        min_amount=min_amount,
        max_amount=max_amount,
        tag_id=tag_id,
        currency_code=currency_code,
        share=share,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    include_subcategories: bool | Unset = UNSET,
    uncategorized: bool | Unset = UNSET,
    category_review: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    tag_id: list[str] | Unset = UNSET,
    currency_code: str | Unset = UNSET,
    share: GetTransactionDayTotalsShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> DayTotalsResponseEnvelope | ErrorResponse | None:
    """Daily totals of a list

     For the rows `GET /v1/transactions` lists with the same filters: what was spent and received per day
    (in the person's time zone), in the display currency (`currencyCode`, else the person's), newest day
    first, with the period's sums. Transfers and cancelled rows count in neither. A currency with no
    rate to the display currency is left out and named in `unconverted`. Pagination and sorting don't
    apply.

    Args:
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        category_id (str | Unset):
        category_ids (list[str] | Unset):
        include_subcategories (bool | Unset):
        uncategorized (bool | Unset):
        category_review (bool | Unset):
        type_ (str | Unset):
        types (list[str] | Unset):
        status (str | Unset):
        statuses (list[str] | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        tag_id (list[str] | Unset):
        currency_code (str | Unset):
        share (GetTransactionDayTotalsShare | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DayTotalsResponseEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            account_ids=account_ids,
            category_id=category_id,
            category_ids=category_ids,
            include_subcategories=include_subcategories,
            uncategorized=uncategorized,
            category_review=category_review,
            type_=type_,
            types=types,
            status=status,
            statuses=statuses,
            from_date=from_date,
            to_date=to_date,
            search=search,
            min_amount=min_amount,
            max_amount=max_amount,
            tag_id=tag_id,
            currency_code=currency_code,
            share=share,
            x_space_id=x_space_id,
            x_display_currency=x_display_currency,
        )
    ).parsed
