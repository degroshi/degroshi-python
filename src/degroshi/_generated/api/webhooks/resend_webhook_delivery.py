from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delivery_summary_envelope import DeliverySummaryEnvelope
from ...models.error_response import ErrorResponse
from typing import cast


def _get_kwargs(
    id: str,
    delivery_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/{id}/deliveries/{delivery_id}/resend".format(
            id=quote(str(id), safe=""),
            delivery_id=quote(str(delivery_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeliverySummaryEnvelope | ErrorResponse | None:
    if response.status_code == 202:
        response_202 = DeliverySummaryEnvelope.from_dict(response.json())

        return response_202

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DeliverySummaryEnvelope | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeliverySummaryEnvelope | ErrorResponse]:
    """Resend webhook delivery

     The same event id and body, a new attempt now. 409 `WHK_003` when the endpoint is disabled.

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliverySummaryEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> DeliverySummaryEnvelope | ErrorResponse | None:
    """Resend webhook delivery

     The same event id and body, a new attempt now. 409 `WHK_003` when the endpoint is disabled.

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliverySummaryEnvelope | ErrorResponse
    """

    return sync_detailed(
        id=id,
        delivery_id=delivery_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeliverySummaryEnvelope | ErrorResponse]:
    """Resend webhook delivery

     The same event id and body, a new attempt now. 409 `WHK_003` when the endpoint is disabled.

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliverySummaryEnvelope | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> DeliverySummaryEnvelope | ErrorResponse | None:
    """Resend webhook delivery

     The same event id and body, a new attempt now. 409 `WHK_003` when the endpoint is disabled.

    Args:
        id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliverySummaryEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            delivery_id=delivery_id,
            client=client,
        )
    ).parsed
