from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delivery_summary_envelope import DeliverySummaryEnvelope
from ...models.error_response import ErrorResponse
from ...models.test_event_request import TestEventRequest
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: TestEventRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/{id}/test".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeliverySummaryEnvelope | ErrorResponse | None:
    if response.status_code == 202:
        response_202 = DeliverySummaryEnvelope.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

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
    *,
    client: AuthenticatedClient,
    body: TestEventRequest,
) -> Response[DeliverySummaryEnvelope | ErrorResponse]:
    """Send test webhook event

     A made-up event of `type` (`webhook.test` when empty), marked `test: true`, sent to this endpoint
    only and listed in its log, never counted in its health. An endpoint takes 10 test events a minute
    (429 `WHK_030` with `details.retry_after`). The delivery's detail shows the request sent and the
    endpoint's answer.

    Args:
        id (str):
        body (TestEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliverySummaryEnvelope | ErrorResponse]
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
    body: TestEventRequest,
) -> DeliverySummaryEnvelope | ErrorResponse | None:
    """Send test webhook event

     A made-up event of `type` (`webhook.test` when empty), marked `test: true`, sent to this endpoint
    only and listed in its log, never counted in its health. An endpoint takes 10 test events a minute
    (429 `WHK_030` with `details.retry_after`). The delivery's detail shows the request sent and the
    endpoint's answer.

    Args:
        id (str):
        body (TestEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliverySummaryEnvelope | ErrorResponse
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
    body: TestEventRequest,
) -> Response[DeliverySummaryEnvelope | ErrorResponse]:
    """Send test webhook event

     A made-up event of `type` (`webhook.test` when empty), marked `test: true`, sent to this endpoint
    only and listed in its log, never counted in its health. An endpoint takes 10 test events a minute
    (429 `WHK_030` with `details.retry_after`). The delivery's detail shows the request sent and the
    endpoint's answer.

    Args:
        id (str):
        body (TestEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliverySummaryEnvelope | ErrorResponse]
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
    body: TestEventRequest,
) -> DeliverySummaryEnvelope | ErrorResponse | None:
    """Send test webhook event

     A made-up event of `type` (`webhook.test` when empty), marked `test: true`, sent to this endpoint
    only and listed in its log, never counted in its health. An endpoint takes 10 test events a minute
    (429 `WHK_030` with `details.retry_after`). The delivery's detail shows the request sent and the
    endpoint's answer.

    Args:
        id (str):
        body (TestEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliverySummaryEnvelope | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
