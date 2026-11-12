"""Webhook signature checks: ``Degroshi-Signature: t=<unix seconds>,v1=<hex HMAC-SHA256 of "t.body">``."""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any, Literal

SIGNATURE_HEADER = "Degroshi-Signature"

Reason = Literal["malformed", "too_old", "bad_signature"]


class WebhookVerificationError(Exception):
    """The request isn't from Degroshi, or it's too old to trust. ``reason`` says which."""

    def __init__(self, reason: Reason, message: str) -> None:
        super().__init__(message)
        self.reason: Reason = reason


def verify(
    raw_body: bytes | str, header: str | None, secret: str, *, tolerance: int = 300, now: int | None = None
) -> dict[str, Any]:
    """Checks a webhook request and returns its event as a dict. Pass the body exactly as received, before any JSON
    parsing. During a secret change either secret's signature is accepted. Raises WebhookVerificationError."""
    body = raw_body.encode() if isinstance(raw_body, str) else raw_body
    parts = [part.split("=", 1) for part in (header or "").split(",") if "=" in part]
    timestamps = [value.strip() for key, value in parts if key.strip() == "t"]
    signatures = [value.strip() for key, value in parts if key.strip() == "v1"]
    if not timestamps or not timestamps[0].lstrip("-").isdigit() or not signatures:
        raise WebhookVerificationError("malformed", f"no {SIGNATURE_HEADER} header, or it has no t and v1")
    timestamp = int(timestamps[0])
    current = int(time.time()) if now is None else now
    if abs(current - timestamp) > tolerance:
        raise WebhookVerificationError("too_old", "the signature is too old or from the future")
    expected = hmac.new(secret.encode(), f"{timestamp}.".encode() + body, hashlib.sha256).hexdigest()
    if not any(hmac.compare_digest(expected, signature) for signature in signatures):
        raise WebhookVerificationError("bad_signature", "no signature matches the secret")
    return json.loads(body)
