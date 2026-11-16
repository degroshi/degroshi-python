from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_endpoint_request import CreateEndpointRequest
from ...models.created_endpoint_response_envelope import CreatedEndpointResponseEnvelope
from ...models.error_response import ErrorResponse
from typing import cast


def _get_kwargs(
    *,
    body: CreateEndpointRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CreatedEndpointResponseEnvelope | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = CreatedEndpointResponseEnvelope.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CreatedEndpointResponseEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateEndpointRequest,
) -> Response[CreatedEndpointResponseEnvelope | ErrorResponse]:
    """Create webhook endpoint

     An endpoint for the request's space: an HTTPS `url` on a public address (400 `WHK_031` with
    `details.reason`), the `events` to send (400 `WHK_005` for an unknown type) and an optional
    `description`. Leave `space_ids` out: it may name only the request's space (403 `WHK_009`). Each
    event type needs the scope that reads its data, `transactions:read` for `transaction.*` for example
    (403 `AUTH_007` with `details.required_scope`). The answer carries the signing secret
    (`dg_whsec_…`): keep it, a token can't read it back, only rotate it. A plan caps the number of
    endpoints (403 `BILL_013`).

    Args:
        body (CreateEndpointRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedEndpointResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateEndpointRequest,
) -> CreatedEndpointResponseEnvelope | ErrorResponse | None:
    """Create webhook endpoint

     An endpoint for the request's space: an HTTPS `url` on a public address (400 `WHK_031` with
    `details.reason`), the `events` to send (400 `WHK_005` for an unknown type) and an optional
    `description`. Leave `space_ids` out: it may name only the request's space (403 `WHK_009`). Each
    event type needs the scope that reads its data, `transactions:read` for `transaction.*` for example
    (403 `AUTH_007` with `details.required_scope`). The answer carries the signing secret
    (`dg_whsec_…`): keep it, a token can't read it back, only rotate it. A plan caps the number of
    endpoints (403 `BILL_013`).

    Args:
        body (CreateEndpointRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedEndpointResponseEnvelope | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateEndpointRequest,
) -> Response[CreatedEndpointResponseEnvelope | ErrorResponse]:
    """Create webhook endpoint

     An endpoint for the request's space: an HTTPS `url` on a public address (400 `WHK_031` with
    `details.reason`), the `events` to send (400 `WHK_005` for an unknown type) and an optional
    `description`. Leave `space_ids` out: it may name only the request's space (403 `WHK_009`). Each
    event type needs the scope that reads its data, `transactions:read` for `transaction.*` for example
    (403 `AUTH_007` with `details.required_scope`). The answer carries the signing secret
    (`dg_whsec_…`): keep it, a token can't read it back, only rotate it. A plan caps the number of
    endpoints (403 `BILL_013`).

    Args:
        body (CreateEndpointRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedEndpointResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateEndpointRequest,
) -> CreatedEndpointResponseEnvelope | ErrorResponse | None:
    """Create webhook endpoint

     An endpoint for the request's space: an HTTPS `url` on a public address (400 `WHK_031` with
    `details.reason`), the `events` to send (400 `WHK_005` for an unknown type) and an optional
    `description`. Leave `space_ids` out: it may name only the request's space (403 `WHK_009`). Each
    event type needs the scope that reads its data, `transactions:read` for `transaction.*` for example
    (403 `AUTH_007` with `details.required_scope`). The answer carries the signing secret
    (`dg_whsec_…`): keep it, a token can't read it back, only rotate it. A plan caps the number of
    endpoints (403 `BILL_013`).

    Args:
        body (CreateEndpointRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedEndpointResponseEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
