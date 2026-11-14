from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.changes_response_envelope import ChangesResponseEnvelope
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    json_types: list[str] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types

    params["types"] = json_types

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/changes",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ChangesResponseEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ChangesResponseEnvelope.from_dict(response.json())

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

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ChangesResponseEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ChangesResponseEnvelope | ErrorResponse]:
    """List what changed

     What changed in the space since a cursor, oldest first: keep a faithful copy by polling, deletions
    included. Without `cursor` the feed starts from the beginning (every object, then the changes); keep
    `next_cursor` from every page and send it next time, and while `has_more` is true read again right
    away. Each item is an object (`transaction`, `account`, `category`, `budget`,
    `recurring_transaction`) with `op` `upsert` and `data`, the object as its list endpoint returns it,
    or `delete`. Changes come in commit order, so a slow write never lands behind a cursor already read.
    Any read scope opens this route, and each type needs the scope that reads it. 410
    `CHANGES_RESYNC_REQUIRED` means the cursor can't continue (access changed, 180 days passed, other
    `types`): read again without a cursor and replace the copy.

    Args:
        cursor (str | Unset):
        types (list[str] | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangesResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        types=types,
        limit=limit,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ChangesResponseEnvelope | ErrorResponse | None:
    """List what changed

     What changed in the space since a cursor, oldest first: keep a faithful copy by polling, deletions
    included. Without `cursor` the feed starts from the beginning (every object, then the changes); keep
    `next_cursor` from every page and send it next time, and while `has_more` is true read again right
    away. Each item is an object (`transaction`, `account`, `category`, `budget`,
    `recurring_transaction`) with `op` `upsert` and `data`, the object as its list endpoint returns it,
    or `delete`. Changes come in commit order, so a slow write never lands behind a cursor already read.
    Any read scope opens this route, and each type needs the scope that reads it. 410
    `CHANGES_RESYNC_REQUIRED` means the cursor can't continue (access changed, 180 days passed, other
    `types`): read again without a cursor and replace the copy.

    Args:
        cursor (str | Unset):
        types (list[str] | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangesResponseEnvelope | ErrorResponse
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        types=types,
        limit=limit,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ChangesResponseEnvelope | ErrorResponse]:
    """List what changed

     What changed in the space since a cursor, oldest first: keep a faithful copy by polling, deletions
    included. Without `cursor` the feed starts from the beginning (every object, then the changes); keep
    `next_cursor` from every page and send it next time, and while `has_more` is true read again right
    away. Each item is an object (`transaction`, `account`, `category`, `budget`,
    `recurring_transaction`) with `op` `upsert` and `data`, the object as its list endpoint returns it,
    or `delete`. Changes come in commit order, so a slow write never lands behind a cursor already read.
    Any read scope opens this route, and each type needs the scope that reads it. 410
    `CHANGES_RESYNC_REQUIRED` means the cursor can't continue (access changed, 180 days passed, other
    `types`): read again without a cursor and replace the copy.

    Args:
        cursor (str | Unset):
        types (list[str] | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangesResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        types=types,
        limit=limit,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ChangesResponseEnvelope | ErrorResponse | None:
    """List what changed

     What changed in the space since a cursor, oldest first: keep a faithful copy by polling, deletions
    included. Without `cursor` the feed starts from the beginning (every object, then the changes); keep
    `next_cursor` from every page and send it next time, and while `has_more` is true read again right
    away. Each item is an object (`transaction`, `account`, `category`, `budget`,
    `recurring_transaction`) with `op` `upsert` and `data`, the object as its list endpoint returns it,
    or `delete`. Changes come in commit order, so a slow write never lands behind a cursor already read.
    Any read scope opens this route, and each type needs the scope that reads it. 410
    `CHANGES_RESYNC_REQUIRED` means the cursor can't continue (access changed, 180 days passed, other
    `types`): read again without a cursor and replace the copy.

    Args:
        cursor (str | Unset):
        types (list[str] | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangesResponseEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            types=types,
            limit=limit,
            x_space_id=x_space_id,
        )
    ).parsed
