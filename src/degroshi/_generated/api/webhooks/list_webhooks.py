from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.endpoint_response_list_envelope import EndpointResponseListEnvelope
from ...models.error_response import ErrorResponse
from typing import cast


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> EndpointResponseListEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = EndpointResponseListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[EndpointResponseListEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[EndpointResponseListEnvelope | ErrorResponse]:
    """List webhook endpoints

     The webhook endpoints this token manages: those of the request's space alone whose every event type
    the token's scopes read. An endpoint set up in the app for several spaces, or with types the token
    can't read, isn't listed. Each comes with its health: deliveries and successes in the last 24 hours
    and 7 days (test events left out), p95 latency and the last delivery. The signing secret is never
    included.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointResponseListEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> EndpointResponseListEnvelope | ErrorResponse | None:
    """List webhook endpoints

     The webhook endpoints this token manages: those of the request's space alone whose every event type
    the token's scopes read. An endpoint set up in the app for several spaces, or with types the token
    can't read, isn't listed. Each comes with its health: deliveries and successes in the last 24 hours
    and 7 days (test events left out), p95 latency and the last delivery. The signing secret is never
    included.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointResponseListEnvelope | ErrorResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[EndpointResponseListEnvelope | ErrorResponse]:
    """List webhook endpoints

     The webhook endpoints this token manages: those of the request's space alone whose every event type
    the token's scopes read. An endpoint set up in the app for several spaces, or with types the token
    can't read, isn't listed. Each comes with its health: deliveries and successes in the last 24 hours
    and 7 days (test events left out), p95 latency and the last delivery. The signing secret is never
    included.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointResponseListEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> EndpointResponseListEnvelope | ErrorResponse | None:
    """List webhook endpoints

     The webhook endpoints this token manages: those of the request's space alone whose every event type
    the token's scopes read. An endpoint set up in the app for several spaces, or with types the token
    can't read, isn't listed. Each comes with its health: deliveries and successes in the last 24 hours
    and 7 days (test events left out), p95 latency and the last delivery. The signing secret is never
    included.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointResponseListEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
