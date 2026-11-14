from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_source_request import CreateSourceRequest
from ...models.error_response import ErrorResponse
from ...models.source_response_envelope import SourceResponseEnvelope
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: CreateSourceRequest,
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
        "url": "/v1/sources",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | SourceResponseEnvelope | None:
    if response.status_code == 201:
        response_201 = SourceResponseEnvelope.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | SourceResponseEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSourceRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | SourceResponseEnvelope]:
    """Create source

     Add a custom source to the space (scope `sources:write`, in the “Import from your own source” and
    “Full access” tokens). A source is read-only by default: the app then changes only its rows'
    category, merchant, note and tags, and adds no rows of its own to its accounts. Each plan allows a
    number of sources (403 BILL_013 above it).

    Args:
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (CreateSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SourceResponseEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateSourceRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | SourceResponseEnvelope | None:
    """Create source

     Add a custom source to the space (scope `sources:write`, in the “Import from your own source” and
    “Full access” tokens). A source is read-only by default: the app then changes only its rows'
    category, merchant, note and tags, and adds no rows of its own to its accounts. Each plan allows a
    number of sources (403 BILL_013 above it).

    Args:
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (CreateSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SourceResponseEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSourceRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | SourceResponseEnvelope]:
    """Create source

     Add a custom source to the space (scope `sources:write`, in the “Import from your own source” and
    “Full access” tokens). A source is read-only by default: the app then changes only its rows'
    category, merchant, note and tags, and adds no rows of its own to its accounts. Each plan allows a
    number of sources (403 BILL_013 above it).

    Args:
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (CreateSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SourceResponseEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        x_space_id=x_space_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateSourceRequest,
    x_space_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | SourceResponseEnvelope | None:
    """Create source

     Add a custom source to the space (scope `sources:write`, in the “Import from your own source” and
    “Full access” tokens). A source is read-only by default: the app then changes only its rows'
    category, merchant, note and tags, and adds no rows of its own to its accounts. Each plan allows a
    number of sources (403 BILL_013 above it).

    Args:
        x_space_id (str | Unset):
        idempotency_key (str | Unset):
        body (CreateSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SourceResponseEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_space_id=x_space_id,
            idempotency_key=idempotency_key,
        )
    ).parsed
