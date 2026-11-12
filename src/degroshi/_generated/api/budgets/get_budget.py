from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.budget_response_envelope import BudgetResponseEnvelope
from ...models.error_response import ErrorResponse
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    id: str,
    *,
    as_of: datetime.date | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_space_id, Unset):
        headers["X-Space-ID"] = x_space_id

    params: dict[str, Any] = {}

    json_as_of: str | Unset = UNSET
    if not isinstance(as_of, Unset):
        json_as_of = as_of.isoformat()
    params["as_of"] = json_as_of

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/budgets/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> BudgetResponseEnvelope | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = BudgetResponseEnvelope.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[BudgetResponseEnvelope | ErrorResponse]:
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
    as_of: datetime.date | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[BudgetResponseEnvelope | ErrorResponse]:
    """Get budget

     One budget with its progress for one period: the period containing `as_of`, else the current one. An
    allocation's `spent` is the period's expenses minus refunds in its categories, never below zero;
    transfers and cancelled rows never count. Foreign-currency spending is converted at the current
    rate.

    Args:
        id (str):
        as_of (datetime.date | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        as_of=as_of,
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
    as_of: datetime.date | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> BudgetResponseEnvelope | ErrorResponse | None:
    """Get budget

     One budget with its progress for one period: the period containing `as_of`, else the current one. An
    allocation's `spent` is the period's expenses minus refunds in its categories, never below zero;
    transfers and cancelled rows never count. Foreign-currency spending is converted at the current
    rate.

    Args:
        id (str):
        as_of (datetime.date | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetResponseEnvelope | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        as_of=as_of,
        x_space_id=x_space_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    as_of: datetime.date | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> Response[BudgetResponseEnvelope | ErrorResponse]:
    """Get budget

     One budget with its progress for one period: the period containing `as_of`, else the current one. An
    allocation's `spent` is the period's expenses minus refunds in its categories, never below zero;
    transfers and cancelled rows never count. Foreign-currency spending is converted at the current
    rate.

    Args:
        id (str):
        as_of (datetime.date | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetResponseEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        as_of=as_of,
        x_space_id=x_space_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    as_of: datetime.date | Unset = UNSET,
    x_space_id: str | Unset = UNSET,
) -> BudgetResponseEnvelope | ErrorResponse | None:
    """Get budget

     One budget with its progress for one period: the period containing `as_of`, else the current one. An
    allocation's `spent` is the period's expenses minus refunds in its categories, never below zero;
    transfers and cancelled rows never count. Foreign-currency spending is converted at the current
    rate.

    Args:
        id (str):
        as_of (datetime.date | Unset):
        x_space_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetResponseEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            as_of=as_of,
            x_space_id=x_space_id,
        )
    ).parsed
