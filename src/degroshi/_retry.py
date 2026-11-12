"""Retries as an httpx2 transport: network failures, 408, 429 and 5xx, only for requests safe to send again."""

from __future__ import annotations

import asyncio
import random
import time
from collections.abc import Callable

import httpx2

from ._errors import parse_retry_after

RETRIED_STATUSES = frozenset({408, 429, 500, 502, 503, 504})
SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})
MAX_DELAY = 8.0
MAX_RETRY_AFTER = 60.0


def is_retry_safe(request: httpx2.Request) -> bool:
    """A read, a PUT or DELETE (the same result each time), or a write carrying an Idempotency-Key."""
    return request.method.upper() in SAFE_METHODS or "idempotency-key" in request.headers


def retry_delay(attempt: int, response: httpx2.Response | None, rand: Callable[[], float] = random.random) -> float:
    """Seconds before retry ``attempt`` (1-based): Retry-After when sent, else backoff with jitter."""
    retry_after = parse_retry_after(response.headers.get("retry-after")) if response is not None else None
    if retry_after is not None:
        return min(retry_after, MAX_RETRY_AFTER)
    return min(0.5 * 2 ** (attempt - 1), MAX_DELAY) * (0.75 + rand() * 0.5)


class RetryTransport(httpx2.BaseTransport):
    def __init__(self, inner: httpx2.BaseTransport, max_retries: int, sleep: Callable[[float], None] = time.sleep):
        self._inner, self._max_retries, self._sleep = inner, max_retries, sleep

    def handle_request(self, request: httpx2.Request) -> httpx2.Response:
        retries = self._max_retries if is_retry_safe(request) else 0
        attempt = 0
        while True:
            try:
                response = self._inner.handle_request(request)
            except httpx2.TransportError:
                if attempt >= retries:
                    raise
                attempt += 1
                self._sleep(retry_delay(attempt, None))
                continue
            if response.status_code not in RETRIED_STATUSES or attempt >= retries:
                return response
            response.close()
            attempt += 1
            self._sleep(retry_delay(attempt, response))

    def close(self) -> None:
        self._inner.close()


class AsyncRetryTransport(httpx2.AsyncBaseTransport):
    def __init__(
        self, inner: httpx2.AsyncBaseTransport, max_retries: int, sleep: Callable[[float], object] = asyncio.sleep
    ):
        self._inner, self._max_retries, self._sleep = inner, max_retries, sleep

    async def handle_async_request(self, request: httpx2.Request) -> httpx2.Response:
        retries = self._max_retries if is_retry_safe(request) else 0
        attempt = 0
        while True:
            try:
                response = await self._inner.handle_async_request(request)
            except httpx2.TransportError:
                if attempt >= retries:
                    raise
                attempt += 1
                await self._sleep(retry_delay(attempt, None))  # type: ignore[misc]
                continue
            if response.status_code not in RETRIED_STATUSES or attempt >= retries:
                return response
            await response.aclose()
            attempt += 1
            await self._sleep(retry_delay(attempt, response))  # type: ignore[misc]

    async def aclose(self) -> None:
        await self._inner.aclose()
