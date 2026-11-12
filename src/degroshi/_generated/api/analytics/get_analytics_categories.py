from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.category_analytics_response_envelope import CategoryAnalyticsResponseEnvelope
from ...models.error_response import ErrorResponse
from ...models.get_analytics_categories_share import check_get_analytics_categories_share
from ...models.get_analytics_categories_share import GetAnalyticsCategoriesShare
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    from_: datetime.date,
    to: datetime.date,
    granularity: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    share: GetAnalyticsCategoriesShare | Unset = UNSET,
    aggregation_mode: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    params: dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["granularity"] = granularity

    params["currency"] = currency

    json_account_ids: list[str] | Unset = UNSET
    if not isinstance(account_ids, Unset):
        json_account_ids = account_ids

    params["account_ids"] = json_account_ids

    json_share: str | Unset = UNSET
    if not isinstance(share, Unset):
        json_share = share

    params["share"] = json_share

    params["aggregationMode"] = aggregation_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/categories",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CategoryAnalyticsResponseEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CategoryAnalyticsResponseEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CategoryAnalyticsResponseEnvelope | ErrorResponse]:
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
    account_ids: list[str] | Unset = UNSET,
    share: GetAnalyticsCategoriesShare | Unset = UNSET,
    aggregation_mode: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[CategoryAnalyticsResponseEnvelope | ErrorResponse]:
    """Category breakdown

     Income and expenses per category, with the hierarchy. Rows without a category are reported in
    `uncategorized`. With `aggregatedWithChildren` a parent's amounts include its subcategories.
    Foreign-currency amounts are converted at the current exchange rate.

    Args:
        from_ (datetime.date):
        to (datetime.date):
        granularity (str | Unset):
        currency (str | Unset):
        account_ids (list[str] | Unset):
        share (GetAnalyticsCategoriesShare | Unset):
        aggregation_mode (str | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryAnalyticsResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        granularity=granularity,
        currency=currency,
        account_ids=account_ids,
        share=share,
        aggregation_mode=aggregation_mode,
        x_space_id=x_space_id,
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
    account_ids: list[str] | Unset = UNSET,
    share: GetAnalyticsCategoriesShare | Unset = UNSET,
    aggregation_mode: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> CategoryAnalyticsResponseEnvelope | ErrorResponse | None:
    """Category breakdown

     Income and expenses per category, with the hierarchy. Rows without a category are reported in
    `uncategorized`. With `aggregatedWithChildren` a parent's amounts include its subcategories.
    Foreign-currency amounts are converted at the current exchange rate.

    Args:
        from_ (datetime.date):
        to (datetime.date):
        granularity (str | Unset):
        currency (str | Unset):
        account_ids (list[str] | Unset):
        share (GetAnalyticsCategoriesShare | Unset):
        aggregation_mode (str | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryAnalyticsResponseEnvelope | ErrorResponse
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        granularity=granularity,
        currency=currency,
        account_ids=account_ids,
        share=share,
        aggregation_mode=aggregation_mode,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date,
    to: datetime.date,
    granularity: str | Unset = UNSET,
    currency: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    share: GetAnalyticsCategoriesShare | Unset = UNSET,
    aggregation_mode: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[CategoryAnalyticsResponseEnvelope | ErrorResponse]:
    """Category breakdown

     Income and expenses per category, with the hierarchy. Rows without a category are reported in
    `uncategorized`. With `aggregatedWithChildren` a parent's amounts include its subcategories.
    Foreign-currency amounts are converted at the current exchange rate.

    Args:
        from_ (datetime.date):
        to (datetime.date):
        granularity (str | Unset):
        currency (str | Unset):
        account_ids (list[str] | Unset):
        share (GetAnalyticsCategoriesShare | Unset):
        aggregation_mode (str | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryAnalyticsResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        granularity=granularity,
        currency=currency,
        account_ids=account_ids,
        share=share,
        aggregation_mode=aggregation_mode,
        x_space_id=x_space_id,
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
    account_ids: list[str] | Unset = UNSET,
    share: GetAnalyticsCategoriesShare | Unset = UNSET,
    aggregation_mode: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> CategoryAnalyticsResponseEnvelope | ErrorResponse | None:
    """Category breakdown

     Income and expenses per category, with the hierarchy. Rows without a category are reported in
    `uncategorized`. With `aggregatedWithChildren` a parent's amounts include its subcategories.
    Foreign-currency amounts are converted at the current exchange rate.

    Args:
        from_ (datetime.date):
        to (datetime.date):
        granularity (str | Unset):
        currency (str | Unset):
        account_ids (list[str] | Unset):
        share (GetAnalyticsCategoriesShare | Unset):
        aggregation_mode (str | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryAnalyticsResponseEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            granularity=granularity,
            currency=currency,
            account_ids=account_ids,
            share=share,
            aggregation_mode=aggregation_mode,
            x_space_id=x_space_id,
        )
    ).parsed
