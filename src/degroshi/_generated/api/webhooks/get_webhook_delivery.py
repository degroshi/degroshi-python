from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delivery_detail_envelope import DeliveryDetailEnvelope
from ...models.error_response import ErrorResponse
from typing import cast


def _get_kwargs(
    id: str,
    delivery_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks/{id}/deliveries/{delivery_id}".format(
            id=quote(str(id), safe=""),
            delivery_id=quote(str(delivery_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeliveryDetailEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeliveryDetailEnvelope.from_dict(response.json())

        return response_200

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
) -> Response[DeliveryDetailEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeliveryDetailEnvelope | ErrorResponse]:
    """Get webhook delivery

     One delivery: what was sent (the URL, the headers with the signature, the JSON body) and every
    attempt with its status, duration, and the answer's first 20 headers and first 4 KB.

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryDetailEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> DeliveryDetailEnvelope | ErrorResponse | None:
    """Get webhook delivery

     One delivery: what was sent (the URL, the headers with the signature, the JSON body) and every
    attempt with its status, duration, and the answer's first 20 headers and first 4 KB.

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryDetailEnvelope | ErrorResponse
    """

    return sync_detailed(
        id=id,
        delivery_id=delivery_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeliveryDetailEnvelope | ErrorResponse]:
    """Get webhook delivery

     One delivery: what was sent (the URL, the headers with the signature, the JSON body) and every
    attempt with its status, duration, and the answer's first 20 headers and first 4 KB.

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryDetailEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> DeliveryDetailEnvelope | ErrorResponse | None:
    """Get webhook delivery

     One delivery: what was sent (the URL, the headers with the signature, the JSON body) and every
    attempt with its status, duration, and the answer's first 20 headers and first 4 KB.

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryDetailEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            delivery_id=delivery_id,
            client=client,
        )
    ).parsed
