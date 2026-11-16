from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.rotate_secret_request import RotateSecretRequest
from ...models.secret_response_envelope import SecretResponseEnvelope
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: RotateSecretRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/{id}/rotate-secret".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | SecretResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = SecretResponseEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | SecretResponseEnvelope]:
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
    body: RotateSecretRequest,
) -> Response[ErrorResponse | SecretResponseEnvelope]:
    """Rotate webhook secret

     Makes a new signing secret at once and returns it. The old one keeps signing for `overlap_hours` (0,
    1, 24 or 72), so both signatures appear in `Degroshi-Signature` until then and a receiver can switch
    without missing events.

    Args:
        id (str):
        body (RotateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SecretResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: RotateSecretRequest,
) -> ErrorResponse | SecretResponseEnvelope | None:
    """Rotate webhook secret

     Makes a new signing secret at once and returns it. The old one keeps signing for `overlap_hours` (0,
    1, 24 or 72), so both signatures appear in `Degroshi-Signature` until then and a receiver can switch
    without missing events.

    Args:
        id (str):
        body (RotateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SecretResponseEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: RotateSecretRequest,
) -> Response[ErrorResponse | SecretResponseEnvelope]:
    """Rotate webhook secret

     Makes a new signing secret at once and returns it. The old one keeps signing for `overlap_hours` (0,
    1, 24 or 72), so both signatures appear in `Degroshi-Signature` until then and a receiver can switch
    without missing events.

    Args:
        id (str):
        body (RotateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SecretResponseEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: RotateSecretRequest,
) -> ErrorResponse | SecretResponseEnvelope | None:
    """Rotate webhook secret

     Makes a new signing secret at once and returns it. The old one keeps signing for `overlap_hours` (0,
    1, 24 or 72), so both signatures appear in `Degroshi-Signature` until then and a receiver can switch
    without missing events.

    Args:
        id (str):
        body (RotateSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SecretResponseEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
