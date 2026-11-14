from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.event_list_page_envelope import EventListPageEnvelope
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime


def _get_kwargs(
    *,
    type_: list[str] | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    starting_after: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    params: dict[str, Any] = {}

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_created_gte: str | Unset = UNSET
    if not isinstance(created_gte, Unset):
        json_created_gte = created_gte.isoformat()
    params["created_gte"] = json_created_gte

    json_starting_after: str | Unset = UNSET
    if not isinstance(starting_after, Unset):
        json_starting_after = str(starting_after)
    params["starting_after"] = json_starting_after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | EventListPageEnvelope | None:
    if response.status_code == 200:
        response_200 = EventListPageEnvelope.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | EventListPageEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: list[str] | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    starting_after: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | EventListPageEnvelope]:
    """List events

     The space's events of the last 30 days, newest first, as webhook endpoints receive them. A space
    records events from its first personal access token or webhook endpoint: every type while an active
    token is bound to it, otherwise the types its endpoints take. Any read scope opens this route, and
    each event type needs the scope that reads its object: `transactions:read` for `transaction.*`,
    `transactions.bulk_updated` and `import.completed`, `accounts:read` for `account.balance.updated`
    and `connection.status_changed`, `budgets:read` and `recurring:read` for their events. Filter with
    `type` and `created_gte`; `meta.has_more` says older events follow, so pass the last `id` as
    `starting_after`.

    Args:
        type_ (list[str] | Unset):
        created_gte (datetime.datetime | Unset):
        starting_after (UUID | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EventListPageEnvelope]
    """

    kwargs = _get_kwargs(
        type_=type_,
        created_gte=created_gte,
        starting_after=starting_after,
        limit=limit,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: list[str] | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    starting_after: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | EventListPageEnvelope | None:
    """List events

     The space's events of the last 30 days, newest first, as webhook endpoints receive them. A space
    records events from its first personal access token or webhook endpoint: every type while an active
    token is bound to it, otherwise the types its endpoints take. Any read scope opens this route, and
    each event type needs the scope that reads its object: `transactions:read` for `transaction.*`,
    `transactions.bulk_updated` and `import.completed`, `accounts:read` for `account.balance.updated`
    and `connection.status_changed`, `budgets:read` and `recurring:read` for their events. Filter with
    `type` and `created_gte`; `meta.has_more` says older events follow, so pass the last `id` as
    `starting_after`.

    Args:
        type_ (list[str] | Unset):
        created_gte (datetime.datetime | Unset):
        starting_after (UUID | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EventListPageEnvelope
    """

    return sync_detailed(
        client=client,
        type_=type_,
        created_gte=created_gte,
        starting_after=starting_after,
        limit=limit,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: list[str] | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    starting_after: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | EventListPageEnvelope]:
    """List events

     The space's events of the last 30 days, newest first, as webhook endpoints receive them. A space
    records events from its first personal access token or webhook endpoint: every type while an active
    token is bound to it, otherwise the types its endpoints take. Any read scope opens this route, and
    each event type needs the scope that reads its object: `transactions:read` for `transaction.*`,
    `transactions.bulk_updated` and `import.completed`, `accounts:read` for `account.balance.updated`
    and `connection.status_changed`, `budgets:read` and `recurring:read` for their events. Filter with
    `type` and `created_gte`; `meta.has_more` says older events follow, so pass the last `id` as
    `starting_after`.

    Args:
        type_ (list[str] | Unset):
        created_gte (datetime.datetime | Unset):
        starting_after (UUID | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EventListPageEnvelope]
    """

    kwargs = _get_kwargs(
        type_=type_,
        created_gte=created_gte,
        starting_after=starting_after,
        limit=limit,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: list[str] | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    starting_after: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | EventListPageEnvelope | None:
    """List events

     The space's events of the last 30 days, newest first, as webhook endpoints receive them. A space
    records events from its first personal access token or webhook endpoint: every type while an active
    token is bound to it, otherwise the types its endpoints take. Any read scope opens this route, and
    each event type needs the scope that reads its object: `transactions:read` for `transaction.*`,
    `transactions.bulk_updated` and `import.completed`, `accounts:read` for `account.balance.updated`
    and `connection.status_changed`, `budgets:read` and `recurring:read` for their events. Filter with
    `type` and `created_gte`; `meta.has_more` says older events follow, so pass the last `id` as
    `starting_after`.

    Args:
        type_ (list[str] | Unset):
        created_gte (datetime.datetime | Unset):
        starting_after (UUID | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EventListPageEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            created_gte=created_gte,
            starting_after=starting_after,
            limit=limit,
            x_space_id=x_space_id,
        )
    ).parsed
