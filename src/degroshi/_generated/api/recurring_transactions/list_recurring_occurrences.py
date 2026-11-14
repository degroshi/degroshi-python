from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.occurrences_response_envelope import OccurrencesResponseEnvelope
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    with_past: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    if not isinstance(x_display_currency, Unset):
        headers["X-Display-Currency"] = x_display_currency

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["with_past"] = with_past

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/recurring-transactions/occurrences",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | OccurrencesResponseEnvelope | None:
    if response.status_code == 200:
        response_200 = OccurrencesResponseEnvelope.from_dict(response.json())

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
) -> Response[ErrorResponse | OccurrencesResponseEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    with_past: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[ErrorResponse | OccurrencesResponseEnvelope]:
    """List upcoming occurrences

     Every active recurring rule's occurrences dated from `from` to `to` (days in the person's time zone,
    both included) that haven't been posted yet. Paused rules and dates after a rule's `end_date` are
    left out. `is_due` marks occurrences dated today or earlier.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        with_past (bool | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OccurrencesResponseEnvelope]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        with_past=with_past,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    with_past: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> ErrorResponse | OccurrencesResponseEnvelope | None:
    """List upcoming occurrences

     Every active recurring rule's occurrences dated from `from` to `to` (days in the person's time zone,
    both included) that haven't been posted yet. Paused rules and dates after a rule's `end_date` are
    left out. `is_due` marks occurrences dated today or earlier.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        with_past (bool | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OccurrencesResponseEnvelope
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        with_past=with_past,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    with_past: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> Response[ErrorResponse | OccurrencesResponseEnvelope]:
    """List upcoming occurrences

     Every active recurring rule's occurrences dated from `from` to `to` (days in the person's time zone,
    both included) that haven't been posted yet. Paused rules and dates after a rule's `end_date` are
    left out. `is_due` marks occurrences dated today or earlier.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        with_past (bool | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OccurrencesResponseEnvelope]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        with_past=with_past,
        x_space_id=x_space_id,
        x_display_currency=x_display_currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    with_past: bool | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
    x_display_currency: str | Unset = UNSET,
) -> ErrorResponse | OccurrencesResponseEnvelope | None:
    """List upcoming occurrences

     Every active recurring rule's occurrences dated from `from` to `to` (days in the person's time zone,
    both included) that haven't been posted yet. Paused rules and dates after a rule's `end_date` are
    left out. `is_due` marks occurrences dated today or earlier.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        with_past (bool | Unset):
        x_space_id (str | Unset):
        x_display_currency (str | Unset):  Example: EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OccurrencesResponseEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            with_past=with_past,
            x_space_id=x_space_id,
            x_display_currency=x_display_currency,
        )
    ).parsed
