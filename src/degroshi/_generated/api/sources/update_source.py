from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.source_response_envelope import SourceResponseEnvelope
from ...models.update_source_request import UpdateSourceRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: UpdateSourceRequest,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/sources/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | SourceResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = SourceResponseEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | SourceResponseEnvelope]:
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
    body: UpdateSourceRequest,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | SourceResponseEnvelope]:
    """Update source

     Rename, pause or resume a source; fields left out keep their value. A paused source takes no pushes
    (409 SRC_002) until it is resumed.

    Args:
        id (str):
        x_space_id (str | Unset):
        body (UpdateSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SourceResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSourceRequest,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | SourceResponseEnvelope | None:
    """Update source

     Rename, pause or resume a source; fields left out keep their value. A paused source takes no pushes
    (409 SRC_002) until it is resumed.

    Args:
        id (str):
        x_space_id (str | Unset):
        body (UpdateSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SourceResponseEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSourceRequest,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | SourceResponseEnvelope]:
    """Update source

     Rename, pause or resume a source; fields left out keep their value. A paused source takes no pushes
    (409 SRC_002) until it is resumed.

    Args:
        id (str):
        x_space_id (str | Unset):
        body (UpdateSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SourceResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSourceRequest,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | SourceResponseEnvelope | None:
    """Update source

     Rename, pause or resume a source; fields left out keep their value. A paused source takes no pushes
    (409 SRC_002) until it is resumed.

    Args:
        id (str):
        x_space_id (str | Unset):
        body (UpdateSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SourceResponseEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            x_space_id=x_space_id,
        )
    ).parsed
