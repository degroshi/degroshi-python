from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.balance_batch_request import BalanceBatchRequest
from ...models.balance_batch_response_envelope import BalanceBatchResponseEnvelope
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: BalanceBatchRequest,
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
        "url": "/v1/sources/{id}/balances/batch".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> BalanceBatchResponseEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = BalanceBatchResponseEnvelope.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[BalanceBatchResponseEnvelope | ErrorResponse]:
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
    body: BalanceBatchRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[BalanceBatchResponseEnvelope | ErrorResponse]:
    """Push balances

     Tell Degroshi what each account holds at a moment (`as_of`). The latest `as_of` wins: an older
    balance is skipped (`stale`). When the account's rows don't add up to the balance, the difference is
    booked as one balance adjustment, as when the person corrects a balance by hand.

    Args:
        id (str):
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (BalanceBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BalanceBatchResponseEnvelope | ErrorResponse]
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
    body: BalanceBatchRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> BalanceBatchResponseEnvelope | ErrorResponse | None:
    """Push balances

     Tell Degroshi what each account holds at a moment (`as_of`). The latest `as_of` wins: an older
    balance is skipped (`stale`). When the account's rows don't add up to the balance, the difference is
    booked as one balance adjustment, as when the person corrects a balance by hand.

    Args:
        id (str):
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (BalanceBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BalanceBatchResponseEnvelope | ErrorResponse
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
    body: BalanceBatchRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[BalanceBatchResponseEnvelope | ErrorResponse]:
    """Push balances

     Tell Degroshi what each account holds at a moment (`as_of`). The latest `as_of` wins: an older
    balance is skipped (`stale`). When the account's rows don't add up to the balance, the difference is
    booked as one balance adjustment, as when the person corrects a balance by hand.

    Args:
        id (str):
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (BalanceBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BalanceBatchResponseEnvelope | ErrorResponse]
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
    body: BalanceBatchRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> BalanceBatchResponseEnvelope | ErrorResponse | None:
    """Push balances

     Tell Degroshi what each account holds at a moment (`as_of`). The latest `as_of` wins: an older
    balance is skipped (`stale`). When the account's rows don't add up to the balance, the difference is
    booked as one balance adjustment, as when the person corrects a balance by hand.

    Args:
        id (str):
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (BalanceBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BalanceBatchResponseEnvelope | ErrorResponse
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
