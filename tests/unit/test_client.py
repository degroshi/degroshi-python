import json
from decimal import Decimal
from pathlib import Path

import httpx2
import pytest

from degroshi import ConflictError, Degroshi, NotFoundError, RateLimitError


def client(handler, **options) -> tuple[Degroshi, list[httpx2.Request]]:
    seen: list[httpx2.Request] = []

    def record(request: httpx2.Request) -> httpx2.Response:
        seen.append(request)
        return handler(request)

    return Degroshi(
        "dg_pat_test", base_url="https://api.test", max_retries=0, transport=httpx2.MockTransport(record), **options
    ), seen


TRANSACTION = json.loads((Path(__file__).parent / "fixtures" / "transaction.json").read_text())


def test_sends_the_key_the_space_and_the_sdk_version() -> None:
    # Arrange
    degroshi, seen = client(lambda _: httpx2.Response(200, json={"success": True, "data": []}), space_id="s1")

    # Act
    degroshi.accounts.list()

    # Assert
    assert seen[0].headers["X-API-Key"] == "dg_pat_test"
    assert seen[0].headers["X-Space-ID"] == "s1"
    assert seen[0].headers["X-Degroshi-SDK"].startswith("python/")


def test_amounts_are_decimal() -> None:
    # Arrange
    degroshi, _ = client(lambda _: httpx2.Response(200, json={"success": True, "data": TRANSACTION}))

    # Act
    actual = degroshi.transactions.get("t1")

    # Assert
    assert actual.amount == Decimal("642.30")
    assert isinstance(actual.amount, Decimal)
    assert actual.to_dict()["amount"] == "642.30"


def test_errors_are_typed_with_the_api_code() -> None:
    # Arrange
    body = {"success": False, "error": {"code": "TXN_001", "message": "not found", "correlation_id": "c-1"}}
    degroshi, _ = client(lambda _: httpx2.Response(404, json=body))

    # Act & Assert
    with pytest.raises(NotFoundError) as caught:
        degroshi.transactions.get("missing")
    assert caught.value.code == "TXN_001"
    assert caught.value.correlation_id == "c-1"


def test_rate_limit_reads_retry_after() -> None:
    # Arrange
    body = {"success": False, "error": {"code": "RATE_001", "message": "slow down"}}
    degroshi, _ = client(lambda _: httpx2.Response(429, json=body, headers={"Retry-After": "7"}))

    # Act & Assert
    with pytest.raises(RateLimitError) as caught:
        degroshi.accounts.list()
    assert caught.value.retry_after_seconds == 7.0


def test_creates_send_an_idempotency_key_and_edits_if_match() -> None:
    # Arrange
    def handler(request: httpx2.Request) -> httpx2.Response:
        if request.method == "PATCH":
            return httpx2.Response(
                412, json={"success": False, "error": {"code": "SYNC_PRECONDITION_FAILED", "message": "x"}}
            )
        return httpx2.Response(201, json={"success": True, "data": TRANSACTION})

    degroshi, seen = client(handler)
    from degroshi._generated.models.create_transaction_request import CreateTransactionRequest
    from degroshi._generated.models.update_transaction_request import UpdateTransactionRequest

    # Act
    created = degroshi.transactions.create(
        CreateTransactionRequest.from_dict(
            {"account_id": "a1", "amount": "642.30", "type": "expense", "transaction_date": "2026-11-10"}
        )
    )
    degroshi.transactions.create(
        CreateTransactionRequest.from_dict(
            {"account_id": "a1", "amount": "1", "type": "expense", "transaction_date": "2026-11-10"}
        ),
        idempotency_key="mine",
    )
    with pytest.raises(ConflictError):
        degroshi.transactions.update("t1", UpdateTransactionRequest(note="кава"), if_match=3)

    # Assert
    assert created.amount == Decimal("642.30")
    assert len(seen[0].headers["Idempotency-Key"]) == 36
    assert seen[1].headers["Idempotency-Key"] == "mine"
    assert json.loads(seen[0].content)["amount"] == "642.30"
    assert seen[2].headers["If-Match"] == "3"


def test_an_edit_without_a_version_sends_no_if_match() -> None:
    # Arrange: a response row may carry no version (null or absent).
    from degroshi._generated.types import UNSET

    degroshi, seen = client(lambda request: httpx2.Response(200, json={"success": True, "data": {"deleted": True}}))

    # Act
    degroshi.transactions.delete("t1", if_match=None)
    degroshi.transactions.delete("t1", if_match=UNSET)

    # Assert
    assert "If-Match" not in seen[0].headers
    assert "If-Match" not in seen[1].headers


def test_iterates_transactions_until_has_next_is_false() -> None:
    # Arrange
    def handler(request: httpx2.Request) -> httpx2.Response:
        page = int(request.url.params["page"])
        row = {**TRANSACTION, "id": f"t{page}"}
        meta = {"page": page, "per_page": 1, "total": 2, "total_pages": 2, "has_next": page < 2, "has_prev": page > 1}
        return httpx2.Response(200, json={"success": True, "data": [row], "meta": meta})

    degroshi, seen = client(handler)

    # Act
    actual = [t.id for t in degroshi.transactions.iterate(per_page=1)]

    # Assert
    assert actual == ["t1", "t2"]
    assert len(seen) == 2


def test_needs_a_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DEGROSHI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="api_key"):
        Degroshi()
