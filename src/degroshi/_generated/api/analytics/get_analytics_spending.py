from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.get_analytics_spending_share import check_get_analytics_spending_share
from ...models.get_analytics_spending_share import GetAnalyticsSpendingShare
from ...models.spending_response_envelope import SpendingResponseEnvelope
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    from_: datetime.date,
    to: datetime.date,
    granularity: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    share: GetAnalyticsSpendingShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    if not isinstance(x_display_currency, Unset):
        headers["X-Display-Currency"] = x_display_currency

    params: dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["granularity"] = granularity

    params["currency"] = currency

    json_share: str | Unset = UNSET
    if not isinstance(share, Unset):
        json_share = share

    params["share"] = json_share

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/spending",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | SpendingResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = SpendingResponseEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | SpendingResponseEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date,
    to: datetime.date,
    granularity: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    share: GetAnalyticsSpendingShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[ErrorResponse | SpendingResponseEnvelope]:
    """Spending breakdown

     Expenses per category for a date range, each with its share of `total_expenses`; expenses without a
    category are reported in `uncategorized`.

    Args:
        from_ (datetime.date):
        to (datetime.date):
        granularity (str | Unset):
        currency (str | Unset):
        share (GetAnalyticsSpendingShare | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SpendingResponseEnvelope]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        granularity=granularity,
        currency=currency,
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
    from_: datetime.date,
    to: datetime.date,
    granularity: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    share: GetAnalyticsSpendingShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> ErrorResponse | SpendingResponseEnvelope | None:
    """Spending breakdown

     Expenses per category for a date range, each with its share of `total_expenses`; expenses without a
    category are reported in `uncategorized`.

    Args:
        from_ (datetime.date):
        to (datetime.date):
        granularity (str | Unset):
        currency (str | Unset):
        share (GetAnalyticsSpendingShare | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SpendingResponseEnvelope
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        granularity=granularity,
        currency=currency,
        share=share,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date,
    to: datetime.date,
    granularity: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    share: GetAnalyticsSpendingShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[ErrorResponse | SpendingResponseEnvelope]:
    """Spending breakdown

     Expenses per category for a date range, each with its share of `total_expenses`; expenses without a
    category are reported in `uncategorized`.

    Args:
        from_ (datetime.date):
        to (datetime.date):
        granularity (str | Unset):
        currency (str | Unset):
        share (GetAnalyticsSpendingShare | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SpendingResponseEnvelope]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        granularity=granularity,
        currency=currency,
        share=share,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: datetime.date,
    to: datetime.date,
    granularity: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    share: GetAnalyticsSpendingShare | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> ErrorResponse | SpendingResponseEnvelope | None:
    """Spending breakdown

     Expenses per category for a date range, each with its share of `total_expenses`; expenses without a
    category are reported in `uncategorized`.

    Args:
        from_ (datetime.date):
        to (datetime.date):
        granularity (str | Unset):
        currency (str | Unset):
        share (GetAnalyticsSpendingShare | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SpendingResponseEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            granularity=granularity,
            currency=currency,
            share=share,
            x_space_id=x_space_id,
            x_display_currency=x_display_currency,
        )
    ).parsed
