from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.sandbox_response_envelope import SandboxResponseEnvelope
from typing import cast


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandbox/reset",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | SandboxResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = SandboxResponseEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | SandboxResponseEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | SandboxResponseEnvelope]:
    """Reset the sandbox

     Puts the sandbox back to its demo data, so a test run starts clean: everything in it is deleted and
    seeded again; its id, keys and webhook endpoints stay, and change-feed cursors get 410 and read
    again. Only a sandbox key (`dg_test_`) can call it (403 `SBX_004`). 20 resets a day (429 `SBX_003`
    with `details.retry_after`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SandboxResponseEnvelope]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | SandboxResponseEnvelope | None:
    """Reset the sandbox

     Puts the sandbox back to its demo data, so a test run starts clean: everything in it is deleted and
    seeded again; its id, keys and webhook endpoints stay, and change-feed cursors get 410 and read
    again. Only a sandbox key (`dg_test_`) can call it (403 `SBX_004`). 20 resets a day (429 `SBX_003`
    with `details.retry_after`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SandboxResponseEnvelope
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | SandboxResponseEnvelope]:
    """Reset the sandbox

     Puts the sandbox back to its demo data, so a test run starts clean: everything in it is deleted and
    seeded again; its id, keys and webhook endpoints stay, and change-feed cursors get 410 and read
    again. Only a sandbox key (`dg_test_`) can call it (403 `SBX_004`). 20 resets a day (429 `SBX_003`
    with `details.retry_after`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SandboxResponseEnvelope]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | SandboxResponseEnvelope | None:
    """Reset the sandbox

     Puts the sandbox back to its demo data, so a test run starts clean: everything in it is deleted and
    seeded again; its id, keys and webhook endpoints stay, and change-feed cursors get 410 and read
    again. Only a sandbox key (`dg_test_`) can call it (403 `SBX_004`). 20 resets a day (429 `SBX_003`
    with `details.retry_after`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SandboxResponseEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
