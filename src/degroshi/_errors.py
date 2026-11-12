"""The errors the client raises."""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any


class DegroshiError(Exception):
    """Any error the API answered with. ``code`` is the API's error code, e.g. ``TXN_ACCOUNT_CONNECTED``."""

    def __init__(
        self,
        status: int,
        code: str,
        message: str,
        details: dict[str, Any] | None = None,
        correlation_id: str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        super().__init__(message or f"HTTP {status}")
        self.status = status
        self.code = code
        self.message = message
        self.details = details or {}
        #: Include it when you report a problem: it finds the request in our logs.
        self.correlation_id = correlation_id
        self.headers = dict(headers or {})


class BadRequestError(DegroshiError):
    """400: the request is malformed or breaks a rule."""


class AuthenticationError(DegroshiError):
    """401: the key is missing, wrong, expired or revoked."""


class PermissionDeniedError(DegroshiError):
    """403: the key lacks the scope, the space or the role for this."""


class NotFoundError(DegroshiError):
    """404: no such resource in the space."""


class ConflictError(DegroshiError):
    """409 or 412: it changed meanwhile, or the version you sent is old."""


class UnprocessableEntityError(DegroshiError):
    """422: understood but refused."""


class RateLimitError(DegroshiError):
    """429: too many requests."""

    @property
    def retry_after_seconds(self) -> float | None:
        return parse_retry_after(self.headers.get("retry-after") or self.headers.get("Retry-After"))


class InternalServerError(DegroshiError):
    """5xx: our side failed. Retried for you when it's safe; this is the last answer."""


class ApiConnectionError(Exception):
    """The request never got an answer: no connection, or the connection broke."""


class ApiTimeoutError(ApiConnectionError):
    """No answer within the client's timeout."""


def _class_for(status: int) -> type[DegroshiError]:
    if status == 401:
        return AuthenticationError
    if status == 403:
        return PermissionDeniedError
    if status == 404:
        return NotFoundError
    if status in (409, 412):
        return ConflictError
    if status == 422:
        return UnprocessableEntityError
    if status == 429:
        return RateLimitError
    if status >= 500:
        return InternalServerError
    if status >= 400:
        return BadRequestError
    return DegroshiError


def error_from_response(status: int, content: bytes, headers: Mapping[str, str]) -> DegroshiError:
    """Reads ``{"success": false, "error": {code, message, details, correlation_id}}``; other bodies keep their text."""
    code, message, details, correlation_id = f"HTTP_{status}", "", None, None
    try:
        parsed = json.loads(content or b"null")
    except ValueError:
        parsed = None
    error = parsed.get("error") if isinstance(parsed, dict) else None
    if isinstance(error, dict) and isinstance(error.get("code"), str):
        code = error["code"]
        message = str(error.get("message") or "")
        details = error.get("details") if isinstance(error.get("details"), dict) else None
        correlation_id = error.get("correlation_id")
    else:
        message = content.decode("utf-8", "replace")[:500] if content else f"HTTP {status}"
    return _class_for(status)(status, code, message, details, correlation_id, headers)


def parse_retry_after(value: str | None, now: datetime | None = None) -> float | None:
    """Seconds from a Retry-After header: a number of seconds or an HTTP date."""
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        when = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    return max(0.0, (when - (now or datetime.now(UTC))).total_seconds())
