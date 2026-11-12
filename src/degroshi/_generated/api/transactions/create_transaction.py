from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_transaction_request import CreateTransactionRequest
from ...models.error_response import ErrorResponse
from ...models.transaction_response_envelope import TransactionResponseEnvelope
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: CreateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/transactions",
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

    if response.status_code == 201:
        response_201 = TransactionResponseEnvelope.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

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
    *,
    client: AuthenticatedClient,
    body: CreateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | TransactionResponseEnvelope]:
    """Create transaction

     Add a transaction to a manual account (needs the «Повний доступ» token, scope `transactions:write`).
    `amount` is positive and `type` says its direction (income or expense). Completed and pending rows
    move the account's balance; cancelled ones don't. An optional client-made `id` makes the request
    safe to retry: the same id answers 200 with the stored row and the header `Idempotent-Replayed:
    true`. An account kept by a bank, wallet or exchange takes no rows from the API (422
    TXN_ACCOUNT_CONNECTED). The response carries the row's `version`, also as `ETag`.

    Args:
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (CreateTransactionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TransactionResponseEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | TransactionResponseEnvelope | None:
    """Create transaction

     Add a transaction to a manual account (needs the «Повний доступ» token, scope `transactions:write`).
    `amount` is positive and `type` says its direction (income or expense). Completed and pending rows
    move the account's balance; cancelled ones don't. An optional client-made `id` makes the request
    safe to retry: the same id answers 200 with the stored row and the header `Idempotent-Replayed:
    true`. An account kept by a bank, wallet or exchange takes no rows from the API (422
    TXN_ACCOUNT_CONNECTED). The response carries the row's `version`, also as `ETag`.

    Args:
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (CreateTransactionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TransactionResponseEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | TransactionResponseEnvelope]:
    """Create transaction

     Add a transaction to a manual account (needs the «Повний доступ» token, scope `transactions:write`).
    `amount` is positive and `type` says its direction (income or expense). Completed and pending rows
    move the account's balance; cancelled ones don't. An optional client-made `id` makes the request
    safe to retry: the same id answers 200 with the stored row and the header `Idempotent-Replayed:
    true`. An account kept by a bank, wallet or exchange takes no rows from the API (422
    TXN_ACCOUNT_CONNECTED). The response carries the row's `version`, also as `ETag`.

    Args:
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (CreateTransactionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TransactionResponseEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | TransactionResponseEnvelope | None:
    """Create transaction

     Add a transaction to a manual account (needs the «Повний доступ» token, scope `transactions:write`).
    `amount` is positive and `type` says its direction (income or expense). Completed and pending rows
    move the account's balance; cancelled ones don't. An optional client-made `id` makes the request
    safe to retry: the same id answers 200 with the stored row and the header `Idempotent-Replayed:
    true`. An account kept by a bank, wallet or exchange takes no rows from the API (422
    TXN_ACCOUNT_CONNECTED). The response carries the row's `version`, also as `ETag`.

    Args:
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (CreateTransactionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TransactionResponseEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_space_id=x_space_id,
            idempotency_key=idempotency_key,
        )
    ).parsed
