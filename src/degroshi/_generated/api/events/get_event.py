from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.event_envelope import EventEnvelope
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | EventEnvelope | None:
    if response.status_code == 200:
        response_200 = EventEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

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
) -> Response[ErrorResponse | EventEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | EventEnvelope]:
    """Get event

     One of the space's events of the last 30 days, under the same scope rules as the list.

    Args:
        id (UUID):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EventEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | EventEnvelope | None:
    """Get event

     One of the space's events of the last 30 days, under the same scope rules as the list.

    Args:
        id (UUID):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EventEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | EventEnvelope]:
    """Get event

     One of the space's events of the last 30 days, under the same scope rules as the list.

    Args:
        id (UUID):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EventEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | EventEnvelope | None:
    """Get event

     One of the space's events of the last 30 days, under the same scope rules as the list.

    Args:
        id (UUID):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EventEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_space_id=x_space_id,
        )
    ).parsed
