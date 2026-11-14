from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.category_list_envelope import CategoryListEnvelope
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/categories",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CategoryListEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CategoryListEnvelope.from_dict(response.json())

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
) -> Response[CategoryListEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> Response[CategoryListEnvelope | ErrorResponse]:
    """List categories

     The space's categories as a tree: top-level categories with their children in `children`.

    Args:
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryListEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> CategoryListEnvelope | ErrorResponse | None:
    """List categories

     The space's categories as a tree: top-level categories with their children in `children`.

    Args:
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryListEnvelope | ErrorResponse
    """

    return sync_detailed(
        client=client,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> Response[CategoryListEnvelope | ErrorResponse]:
    """List categories

     The space's categories as a tree: top-level categories with their children in `children`.

    Args:
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryListEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_space_id: str | Unset = UNSET,
) -> CategoryListEnvelope | ErrorResponse | None:
    """List categories

     The space's categories as a tree: top-level categories with their children in `children`.

    Args:
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryListEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            x_space_id=x_space_id,
        )
    ).parsed
