from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.push_item_result_envelope import PushItemResultEnvelope
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    account: str,
    external_id: str,
    *,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/sources/{id}/transactions/{account}/{external_id}".format(
            id=quote(str(id), safe=""),
            account=quote(str(account), safe=""),
            external_id=quote(str(external_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | PushItemResultEnvelope | None:
    if response.status_code == 200:
        response_200 = PushItemResultEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | PushItemResultEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    account: str,
    external_id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | PushItemResultEnvelope]:
    """Remove a pushed transaction

     Remove one row, as a batch item with `deleted: true` would. 404 SRC_003 for an unknown account or
    row; a row already removed answers `unchanged`.

    Args:
        id (str):
        account (str):
        external_id (str):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PushItemResultEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        account=account,
        external_id=external_id,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    account: str,
    external_id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | PushItemResultEnvelope | None:
    """Remove a pushed transaction

     Remove one row, as a batch item with `deleted: true` would. 404 SRC_003 for an unknown account or
    row; a row already removed answers `unchanged`.

    Args:
        id (str):
        account (str):
        external_id (str):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PushItemResultEnvelope
    """

    return sync_detailed(
        id=id,
        account=account,
        external_id=external_id,
        client=client,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    account: str,
    external_id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | PushItemResultEnvelope]:
    """Remove a pushed transaction

     Remove one row, as a batch item with `deleted: true` would. 404 SRC_003 for an unknown account or
    row; a row already removed answers `unchanged`.

    Args:
        id (str):
        account (str):
        external_id (str):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PushItemResultEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        account=account,
        external_id=external_id,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    account: str,
    external_id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | PushItemResultEnvelope | None:
    """Remove a pushed transaction

     Remove one row, as a batch item with `deleted: true` would. 404 SRC_003 for an unknown account or
    row; a row already removed answers `unchanged`.

    Args:
        id (str):
        account (str):
        external_id (str):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PushItemResultEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            account=account,
            external_id=external_id,
            client=client,
            x_space_id=x_space_id,
        )
    ).parsed
