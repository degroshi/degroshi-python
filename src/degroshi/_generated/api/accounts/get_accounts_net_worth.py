from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.net_worth_response_envelope import NetWorthResponseEnvelope
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    base: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    params: dict[str, Any] = {}

    params["base"] = base

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/accounts/net-worth",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | NetWorthResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = NetWorthResponseEnvelope.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | NetWorthResponseEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    base: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | NetWorthResponseEnvelope]:
    """Get net worth

     Total assets, liabilities and net worth across the space's accounts counted in net worth. Amounts
    are converted into `base`, which defaults to the person's preferred currency.

    Args:
        base (str | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | NetWorthResponseEnvelope]
    """

    kwargs = _get_kwargs(
        base=base,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    base: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | NetWorthResponseEnvelope | None:
    """Get net worth

     Total assets, liabilities and net worth across the space's accounts counted in net worth. Amounts
    are converted into `base`, which defaults to the person's preferred currency.

    Args:
        base (str | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | NetWorthResponseEnvelope
    """

    return sync_detailed(
        client=client,
        base=base,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    base: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | NetWorthResponseEnvelope]:
    """Get net worth

     Total assets, liabilities and net worth across the space's accounts counted in net worth. Amounts
    are converted into `base`, which defaults to the person's preferred currency.

    Args:
        base (str | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | NetWorthResponseEnvelope]
    """

    kwargs = _get_kwargs(
        base=base,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    base: str | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | NetWorthResponseEnvelope | None:
    """Get net worth

     Total assets, liabilities and net worth across the space's accounts counted in net worth. Amounts
    are converted into `base`, which defaults to the person's preferred currency.

    Args:
        base (str | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | NetWorthResponseEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            base=base,
            x_space_id=x_space_id,
        )
    ).parsed
