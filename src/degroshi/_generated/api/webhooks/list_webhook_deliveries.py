from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delivery_page_envelope import DeliveryPageEnvelope
from ...models.error_response import ErrorResponse
from ...models.list_webhook_deliveries_status import check_list_webhook_deliveries_status
from ...models.list_webhook_deliveries_status import ListWebhookDeliveriesStatus
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    id: str,
    *,
    type_: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks/{id}/deliveries".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeliveryPageEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeliveryPageEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DeliveryPageEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[DeliveryPageEnvelope | ErrorResponse]:
    """List webhook deliveries

     The endpoint's log of the last 30 days, newest first: each event's delivery with its status,
    attempts, last HTTP status and latency. Filter by `type`, `status`, `from` and `to`; page with
    `meta.next_cursor`.

    Args:
        id (str):
        type_ (str | Unset):
        status (ListWebhookDeliveriesStatus | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryPageEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        status=status,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> DeliveryPageEnvelope | ErrorResponse | None:
    """List webhook deliveries

     The endpoint's log of the last 30 days, newest first: each event's delivery with its status,
    attempts, last HTTP status and latency. Filter by `type`, `status`, `from` and `to`; page with
    `meta.next_cursor`.

    Args:
        id (str):
        type_ (str | Unset):
        status (ListWebhookDeliveriesStatus | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryPageEnvelope | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        type_=type_,
        status=status,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[DeliveryPageEnvelope | ErrorResponse]:
    """List webhook deliveries

     The endpoint's log of the last 30 days, newest first: each event's delivery with its status,
    attempts, last HTTP status and latency. Filter by `type`, `status`, `from` and `to`; page with
    `meta.next_cursor`.

    Args:
        id (str):
        type_ (str | Unset):
        status (ListWebhookDeliveriesStatus | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryPageEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        status=status,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> DeliveryPageEnvelope | ErrorResponse | None:
    """List webhook deliveries

     The endpoint's log of the last 30 days, newest first: each event's delivery with its status,
    attempts, last HTTP status and latency. Filter by `type`, `status`, `from` and `to`; page with
    `meta.next_cursor`.

    Args:
        id (str):
        type_ (str | Unset):
        status (ListWebhookDeliveriesStatus | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryPageEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            type_=type_,
            status=status,
            from_=from_,
            to=to,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
