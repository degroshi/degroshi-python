from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.push_batch_request import PushBatchRequest
from ...models.push_batch_response_envelope import PushBatchResponseEnvelope
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: PushBatchRequest,
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
        "url": "/v1/sources/{id}/transactions/batch".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | PushBatchResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = PushBatchResponseEnvelope.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | PushBatchResponseEnvelope]:
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
    body: PushBatchRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | PushBatchResponseEnvelope]:
    """Push transactions

     Create, update or remove up to 500 rows of the source's accounts by your id for each row
    (`external_id`, unique within its account). Amounts are signed decimal strings in the account's
    currency (negative is money out), unlike `POST /v1/transactions`, which takes a positive `amount`
    and a `type`. A row has a moment with its offset (`occurred_at`) or a day (`date`). Each item is
    applied on its own: a bad item fails alone, with its reason in its result, and the response is 200.
    A known external id updates the row with the fields sent; `status: booked` replaces a pending row
    (or `replaces` names the pending row's id); a pending row never booked within 14 days is cancelled;
    `deleted: true` removes a row. A row the person deleted or split in the app stays as they left it,
    and a merchant or note the person set is kept. New rows that look like rows entered by hand are
    listed in `possible_duplicates`; nothing is merged. With an `Idempotency-Key` header, the same key
    within 24 hours returns the first answer (`Idempotent-Replayed: true`); the key with another request
    is 422 SRC_007.

    Args:
        id (str):
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (PushBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PushBatchResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PushBatchRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | PushBatchResponseEnvelope | None:
    """Push transactions

     Create, update or remove up to 500 rows of the source's accounts by your id for each row
    (`external_id`, unique within its account). Amounts are signed decimal strings in the account's
    currency (negative is money out), unlike `POST /v1/transactions`, which takes a positive `amount`
    and a `type`. A row has a moment with its offset (`occurred_at`) or a day (`date`). Each item is
    applied on its own: a bad item fails alone, with its reason in its result, and the response is 200.
    A known external id updates the row with the fields sent; `status: booked` replaces a pending row
    (or `replaces` names the pending row's id); a pending row never booked within 14 days is cancelled;
    `deleted: true` removes a row. A row the person deleted or split in the app stays as they left it,
    and a merchant or note the person set is kept. New rows that look like rows entered by hand are
    listed in `possible_duplicates`; nothing is merged. With an `Idempotency-Key` header, the same key
    within 24 hours returns the first answer (`Idempotent-Replayed: true`); the key with another request
    is 422 SRC_007.

    Args:
        id (str):
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (PushBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PushBatchResponseEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PushBatchRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | PushBatchResponseEnvelope]:
    """Push transactions

     Create, update or remove up to 500 rows of the source's accounts by your id for each row
    (`external_id`, unique within its account). Amounts are signed decimal strings in the account's
    currency (negative is money out), unlike `POST /v1/transactions`, which takes a positive `amount`
    and a `type`. A row has a moment with its offset (`occurred_at`) or a day (`date`). Each item is
    applied on its own: a bad item fails alone, with its reason in its result, and the response is 200.
    A known external id updates the row with the fields sent; `status: booked` replaces a pending row
    (or `replaces` names the pending row's id); a pending row never booked within 14 days is cancelled;
    `deleted: true` removes a row. A row the person deleted or split in the app stays as they left it,
    and a merchant or note the person set is kept. New rows that look like rows entered by hand are
    listed in `possible_duplicates`; nothing is merged. With an `Idempotency-Key` header, the same key
    within 24 hours returns the first answer (`Idempotent-Replayed: true`); the key with another request
    is 422 SRC_007.

    Args:
        id (str):
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (PushBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PushBatchResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PushBatchRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | PushBatchResponseEnvelope | None:
    """Push transactions

     Create, update or remove up to 500 rows of the source's accounts by your id for each row
    (`external_id`, unique within its account). Amounts are signed decimal strings in the account's
    currency (negative is money out), unlike `POST /v1/transactions`, which takes a positive `amount`
    and a `type`. A row has a moment with its offset (`occurred_at`) or a day (`date`). Each item is
    applied on its own: a bad item fails alone, with its reason in its result, and the response is 200.
    A known external id updates the row with the fields sent; `status: booked` replaces a pending row
    (or `replaces` names the pending row's id); a pending row never booked within 14 days is cancelled;
    `deleted: true` removes a row. A row the person deleted or split in the app stays as they left it,
    and a merchant or note the person set is kept. New rows that look like rows entered by hand are
    listed in `possible_duplicates`; nothing is merged. With an `Idempotency-Key` header, the same key
    within 24 hours returns the first answer (`Idempotent-Replayed: true`); the key with another request
    is 422 SRC_007.

    Args:
        id (str):
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (PushBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PushBatchResponseEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            x_space_id=x_space_id,
            idempotency_key=idempotency_key,
        )
    ).parsed
