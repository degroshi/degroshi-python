from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_list_response_list_envelope import AccountListResponseListEnvelope
from ...models.error_response import ErrorResponse
from ...models.list_accounts_status import check_list_accounts_status
from ...models.list_accounts_status import ListAccountsStatus
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    currency: str | Unset = UNSET,
    status: ListAccountsStatus | Unset = "open",
    updated_since: datetime.datetime | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    if not isinstance(x_display_currency, Unset):
        headers["X-Display-Currency"] = x_display_currency

    params: dict[str, Any] = {}

    params["currency"] = currency

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_updated_since: str | Unset = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/accounts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AccountListResponseListEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AccountListResponseListEnvelope.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AccountListResponseListEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    status: ListAccountsStatus | Unset = "open",
    updated_since: datetime.datetime | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[AccountListResponseListEnvelope | ErrorResponse]:
    """List accounts

     The space's open accounts with their balances, or with `status=closed` the closed ones, most
    recently closed first, or with `status=all` both. A connected account carries `connection` (the
    bank, wallet or exchange that keeps it). With `updated_since` (RFC 3339) only the accounts whose
    details or balance changed at or after that instant, each with `changed_at`: ask with `status=all`
    to see closures too, and next time with the largest `changed_at` you saw.

    Args:
        currency (str | Unset):
        status (ListAccountsStatus | Unset):  Default: 'open'.
        updated_since (datetime.datetime | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountListResponseListEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        currency=currency,
        status=status,
        updated_since=updated_since,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    status: ListAccountsStatus | Unset = "open",
    updated_since: datetime.datetime | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> AccountListResponseListEnvelope | ErrorResponse | None:
    """List accounts

     The space's open accounts with their balances, or with `status=closed` the closed ones, most
    recently closed first, or with `status=all` both. A connected account carries `connection` (the
    bank, wallet or exchange that keeps it). With `updated_since` (RFC 3339) only the accounts whose
    details or balance changed at or after that instant, each with `changed_at`: ask with `status=all`
    to see closures too, and next time with the largest `changed_at` you saw.

    Args:
        currency (str | Unset):
        status (ListAccountsStatus | Unset):  Default: 'open'.
        updated_since (datetime.datetime | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountListResponseListEnvelope | ErrorResponse
    """

    return sync_detailed(
        client=client,
        currency=currency,
        status=status,
        updated_since=updated_since,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    status: ListAccountsStatus | Unset = "open",
    updated_since: datetime.datetime | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[AccountListResponseListEnvelope | ErrorResponse]:
    """List accounts

     The space's open accounts with their balances, or with `status=closed` the closed ones, most
    recently closed first, or with `status=all` both. A connected account carries `connection` (the
    bank, wallet or exchange that keeps it). With `updated_since` (RFC 3339) only the accounts whose
    details or balance changed at or after that instant, each with `changed_at`: ask with `status=all`
    to see closures too, and next time with the largest `changed_at` you saw.

    Args:
        currency (str | Unset):
        status (ListAccountsStatus | Unset):  Default: 'open'.
        updated_since (datetime.datetime | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountListResponseListEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        currency=currency,
        status=status,
        updated_since=updated_since,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    currency: str | Unset = UNSET,
    status: ListAccountsStatus | Unset = "open",
    updated_since: datetime.datetime | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> AccountListResponseListEnvelope | ErrorResponse | None:
    """List accounts

     The space's open accounts with their balances, or with `status=closed` the closed ones, most
    recently closed first, or with `status=all` both. A connected account carries `connection` (the
    bank, wallet or exchange that keeps it). With `updated_since` (RFC 3339) only the accounts whose
    details or balance changed at or after that instant, each with `changed_at`: ask with `status=all`
    to see closures too, and next time with the largest `changed_at` you saw.

    Args:
        currency (str | Unset):
        status (ListAccountsStatus | Unset):  Default: 'open'.
        updated_since (datetime.datetime | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountListResponseListEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
            status=status,
            updated_since=updated_since,
            x_space_id=x_space_id,
            x_display_currency=x_display_currency,
        )
    ).parsed
