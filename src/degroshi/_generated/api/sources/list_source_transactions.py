from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.pushed_page_envelope import PushedPageEnvelope
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    id: str,
    *,
    account: str,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    params: dict[str, Any] = {}

    params["account"] = account

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sources/{id}/transactions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | PushedPageEnvelope | None:
    if response.status_code == 200:
        response_200 = PushedPageEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | PushedPageEnvelope]:
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
    account: str,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | PushedPageEnvelope]:
    """List pushed transactions

     The rows Degroshi holds for one of the source's accounts (`account`, its external id), newest first,
    to reconcile with your system: each row's external id, signed amount, time, status (booked, pending
    or cancelled) and whether it was removed. `from` and `to` are days in the person's time zone; follow
    `next_cursor` for older rows.

    Args:
        id (str):
        account (str):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        cursor (str | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PushedPageEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        account=account,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
        x_space_id=x_space_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    account: str,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | PushedPageEnvelope | None:
    """List pushed transactions

     The rows Degroshi holds for one of the source's accounts (`account`, its external id), newest first,
    to reconcile with your system: each row's external id, signed amount, time, status (booked, pending
    or cancelled) and whether it was removed. `from` and `to` are days in the person's time zone; follow
    `next_cursor` for older rows.

    Args:
        id (str):
        account (str):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        cursor (str | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PushedPageEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        account=account,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    account: str,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[ErrorResponse | PushedPageEnvelope]:
    """List pushed transactions

     The rows Degroshi holds for one of the source's accounts (`account`, its external id), newest first,
    to reconcile with your system: each row's external id, signed amount, time, status (booked, pending
    or cancelled) and whether it was removed. `from` and `to` are days in the person's time zone; follow
    `next_cursor` for older rows.

    Args:
        id (str):
        account (str):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        cursor (str | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PushedPageEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        account=account,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    account: str,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> ErrorResponse | PushedPageEnvelope | None:
    """List pushed transactions

     The rows Degroshi holds for one of the source's accounts (`account`, its external id), newest first,
    to reconcile with your system: each row's external id, signed amount, time, status (booked, pending
    or cancelled) and whether it was removed. `from` and `to` are days in the person's time zone; follow
    `next_cursor` for older rows.

    Args:
        id (str):
        account (str):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        cursor (str | Unset):
        limit (int | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PushedPageEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            account=account,
            from_=from_,
            to=to,
            cursor=cursor,
            limit=limit,
            x_space_id=x_space_id,
        )
    ).parsed
