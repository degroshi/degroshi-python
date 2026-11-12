from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.upsert_account_request import UpsertAccountRequest
from ...models.upsert_account_response_envelope import UpsertAccountResponseEnvelope
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    external_id: str,
    *,
    body: UpsertAccountRequest,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/sources/{id}/accounts/{external_id}".format(
            id=quote(str(id), safe=""),
            external_id=quote(str(external_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | UpsertAccountResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = UpsertAccountResponseEnvelope.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | UpsertAccountResponseEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    external_id: str,
    *,
    client: AuthenticatedClient,
    body: UpsertAccountRequest,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | UpsertAccountResponseEnvelope]:
    """Create or update a source account

     Create the source's account with your id for it (`external_id`, 1 to 200 characters), or update its
    name, type and liability flag. The type defaults from the source's kind. The currency is fixed once
    the account exists (409 SRC_004). Push an account before its transactions or balance.

    Args:
        id (str):
        external_id (str):
        x_space_id (str | Unset):
        body (UpsertAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpsertAccountResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        external_id=external_id,
        body=body,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    external_id: str,
    *,
    client: AuthenticatedClient,
    body: UpsertAccountRequest,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | UpsertAccountResponseEnvelope | None:
    """Create or update a source account

     Create the source's account with your id for it (`external_id`, 1 to 200 characters), or update its
    name, type and liability flag. The type defaults from the source's kind. The currency is fixed once
    the account exists (409 SRC_004). Push an account before its transactions or balance.

    Args:
        id (str):
        external_id (str):
        x_space_id (str | Unset):
        body (UpsertAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpsertAccountResponseEnvelope
    """

    return sync_detailed(
        id=id,
        external_id=external_id,
        client=client,
        body=body,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    external_id: str,
    *,
    client: AuthenticatedClient,
    body: UpsertAccountRequest,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | UpsertAccountResponseEnvelope]:
    """Create or update a source account

     Create the source's account with your id for it (`external_id`, 1 to 200 characters), or update its
    name, type and liability flag. The type defaults from the source's kind. The currency is fixed once
    the account exists (409 SRC_004). Push an account before its transactions or balance.

    Args:
        id (str):
        external_id (str):
        x_space_id (str | Unset):
        body (UpsertAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpsertAccountResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        external_id=external_id,
        body=body,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    external_id: str,
    *,
    client: AuthenticatedClient,
    body: UpsertAccountRequest,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | UpsertAccountResponseEnvelope | None:
    """Create or update a source account

     Create the source's account with your id for it (`external_id`, 1 to 200 characters), or update its
    name, type and liability flag. The type defaults from the source's kind. The currency is fixed once
    the account exists (409 SRC_004). Push an account before its transactions or balance.

    Args:
        id (str):
        external_id (str):
        x_space_id (str | Unset):
        body (UpsertAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpsertAccountResponseEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            external_id=external_id,
            client=client,
            body=body,
            x_space_id=x_space_id,
        )
    ).parsed
