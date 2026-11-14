from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_response_envelope import AccountResponseEnvelope
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    if not isinstance(x_display_currency, Unset):
        headers["X-Display-Currency"] = x_display_currency

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/accounts/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AccountResponseEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AccountResponseEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

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
) -> Response[AccountResponseEnvelope | ErrorResponse]:
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
    x_display_currency: str | Unset = UNSET,
) -> Response[AccountResponseEnvelope | ErrorResponse]:
    """Get account

     One account of the space with its balance.

    Args:
        id (str):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
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
    x_display_currency: str | Unset = UNSET,
) -> AccountResponseEnvelope | ErrorResponse | None:
    """Get account

     One account of the space with its balance.

    Args:
        id (str):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountResponseEnvelope | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[AccountResponseEnvelope | ErrorResponse]:
    """Get account

     One account of the space with its balance.

    Args:
        id (str):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> AccountResponseEnvelope | ErrorResponse | None:
    """Get account

     One account of the space with its balance.

    Args:
        id (str):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountResponseEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_space_id=x_space_id,
            x_display_currency=x_display_currency,
        )
    ).parsed
