from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.transaction_response_envelope import TransactionResponseEnvelope
from ...models.update_transaction_request import UpdateTransactionRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: UpdateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/transactions/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | TransactionResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = TransactionResponseEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | TransactionResponseEnvelope]:
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
    body: UpdateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[ErrorResponse | TransactionResponseEnvelope]:
    """Update transaction

     Change a transaction (needs the «Повний доступ» token, scope `transactions:write`); fields left out
    keep their value. Editing one leg of a transfer updates both. Moving a row to or from `cancelled`
    reverses or re-applies its balance effect. With `If-Match: "<version>"` the change applies only when
    the row still has that version; otherwise 412 SYNC_VERSION_MISMATCH.

    Args:
        id (str):
        x_space_id (str | Unset):
        if_match (str | Unset):
        body (UpdateTransactionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TransactionResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: UpdateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> ErrorResponse | TransactionResponseEnvelope | None:
    """Update transaction

     Change a transaction (needs the «Повний доступ» token, scope `transactions:write`); fields left out
    keep their value. Editing one leg of a transfer updates both. Moving a row to or from `cancelled`
    reverses or re-applies its balance effect. With `If-Match: "<version>"` the change applies only when
    the row still has that version; otherwise 412 SYNC_VERSION_MISMATCH.

    Args:
        id (str):
        x_space_id (str | Unset):
        if_match (str | Unset):
        body (UpdateTransactionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TransactionResponseEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        x_space_id=x_space_id,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[ErrorResponse | TransactionResponseEnvelope]:
    """Update transaction

     Change a transaction (needs the «Повний доступ» token, scope `transactions:write`); fields left out
    keep their value. Editing one leg of a transfer updates both. Moving a row to or from `cancelled`
    reverses or re-applies its balance effect. With `If-Match: "<version>"` the change applies only when
    the row still has that version; otherwise 412 SYNC_VERSION_MISMATCH.

    Args:
        id (str):
        x_space_id (str | Unset):
        if_match (str | Unset):
        body (UpdateTransactionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TransactionResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_space_id=x_space_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> ErrorResponse | TransactionResponseEnvelope | None:
    """Update transaction

     Change a transaction (needs the «Повний доступ» token, scope `transactions:write`); fields left out
    keep their value. Editing one leg of a transfer updates both. Moving a row to or from `cancelled`
    reverses or re-applies its balance effect. With `If-Match: "<version>"` the change applies only when
    the row still has that version; otherwise 412 SYNC_VERSION_MISMATCH.

    Args:
        id (str):
        x_space_id (str | Unset):
        if_match (str | Unset):
        body (UpdateTransactionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TransactionResponseEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            x_space_id=x_space_id,
            if_match=if_match,
        )
    ).parsed
