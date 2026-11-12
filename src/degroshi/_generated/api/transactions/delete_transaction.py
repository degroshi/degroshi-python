from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_data_envelope import DeleteDataEnvelope
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/transactions/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeleteDataEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeleteDataEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DeleteDataEnvelope | ErrorResponse]:
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
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[DeleteDataEnvelope | ErrorResponse]:
    """Delete transaction

     Delete a transaction and reverse its balance effect (needs the «Повний доступ» token, scope
    `transactions:write`). Deleting one leg of a transfer deletes both legs; deleting a split deletes
    its parts, and a single part can't be deleted (TXN_047). A repeated delete answers 404. With `If-
    Match: "<version>"` the delete applies only when the row still has that version.

    Args:
        id (str):
        x_space_id (str | Unset):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDataEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        x_space_id=x_space_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> DeleteDataEnvelope | ErrorResponse | None:
    """Delete transaction

     Delete a transaction and reverse its balance effect (needs the «Повний доступ» token, scope
    `transactions:write`). Deleting one leg of a transfer deletes both legs; deleting a split deletes
    its parts, and a single part can't be deleted (TXN_047). A repeated delete answers 404. With `If-
    Match: "<version>"` the delete applies only when the row still has that version.

    Args:
        id (str):
        x_space_id (str | Unset):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDataEnvelope | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        x_space_id=x_space_id,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[DeleteDataEnvelope | ErrorResponse]:
    """Delete transaction

     Delete a transaction and reverse its balance effect (needs the «Повний доступ» token, scope
    `transactions:write`). Deleting one leg of a transfer deletes both legs; deleting a split deletes
    its parts, and a single part can't be deleted (TXN_047). A repeated delete answers 404. With `If-
    Match: "<version>"` the delete applies only when the row still has that version.

    Args:
        id (str):
        x_space_id (str | Unset):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDataEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        x_space_id=x_space_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> DeleteDataEnvelope | ErrorResponse | None:
    """Delete transaction

     Delete a transaction and reverse its balance effect (needs the «Повний доступ» token, scope
    `transactions:write`). Deleting one leg of a transfer deletes both legs; deleting a split deletes
    its parts, and a single part can't be deleted (TXN_047). A repeated delete answers 404. With `If-
    Match: "<version>"` the delete applies only when the row still has that version.

    Args:
        id (str):
        x_space_id (str | Unset):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDataEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_space_id=x_space_id,
            if_match=if_match,
        )
    ).parsed
