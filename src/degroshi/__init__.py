"""The official Python SDK for the Degroshi API. Amounts are Decimal; never float."""

from ._client import AsyncDegroshi, Degroshi, Page
from ._errors import (
    ApiConnectionError,
    ApiTimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    DegroshiError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)
from ._version import API_VERSION, __version__
from .webhooks import SIGNATURE_HEADER, WebhookVerificationError

__all__ = [
    "API_VERSION",
    "SIGNATURE_HEADER",
    "ApiConnectionError",
    "ApiTimeoutError",
    "AsyncDegroshi",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "Degroshi",
    "DegroshiError",
    "InternalServerError",
    "NotFoundError",
    "Page",
    "PermissionDeniedError",
    "RateLimitError",
    "UnprocessableEntityError",
    "WebhookVerificationError",
    "__version__",
]
