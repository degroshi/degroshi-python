"""Against a running API: DEGROSHI_SMOKE_API_URL, DEGROSHI_SMOKE_API_KEY (a full-access token) and
DEGROSHI_SMOKE_SPACE_ID. Writes transactions to a manual account and deletes them. `uv run pytest tests/smoke`."""

import os
import time
from datetime import UTC, datetime
from decimal import Decimal

import pytest

from degroshi import AsyncDegroshi, Degroshi
from degroshi._generated.models.create_transaction_request import CreateTransactionRequest
from degroshi._generated.models.update_transaction_request import UpdateTransactionRequest
from degroshi._generated.types import UNSET

URL = os.environ.get("DEGROSHI_SMOKE_API_URL")
KEY = os.environ.get("DEGROSHI_SMOKE_API_KEY")
SPACE = os.environ.get("DEGROSHI_SMOKE_SPACE_ID")

pytestmark = pytest.mark.skipif(not URL or not KEY, reason="no local API to smoke-test against")


def manual_account(client: Degroshi):
    return next(a for a in client.accounts.list() if a.connection is UNSET and a.source is UNSET and not a.is_closed)


def body(account_id: str, amount: str) -> CreateTransactionRequest:
    return CreateTransactionRequest.from_dict(
        {
            "account_id": account_id,
            "amount": amount,
            "type": "expense",
            "transaction_date": datetime.now(UTC).isoformat(),
            "description": "SDK smoke",
        }
    )


def test_spaces_accounts_and_a_written_transaction() -> None:
    with Degroshi(KEY, base_url=URL, space_id=SPACE) as client:
        assert client.spaces.list()
        account = manual_account(client)
        created = client.transactions.create(body(account.id, "1.23"))
        edited = client.transactions.update(
            created.id, UpdateTransactionRequest(note="SDK smoke: edited"), if_match=created.version
        )
        client.transactions.delete(edited.id, if_match=edited.version)
        assert created.amount == Decimal("1.23")
        assert edited.note == "SDK smoke: edited"


def test_a_create_sent_twice_with_one_key_is_replayed() -> None:
    with Degroshi(KEY, base_url=URL, space_id=SPACE) as client:
        account = manual_account(client)
        key = f"smoke-py-replay-{time.time_ns()}"
        request = body(account.id, "2.00")  # one body: the same key with another body is refused (422)
        first = client.transactions.create(request, idempotency_key=key)
        second = client.transactions.create(request, idempotency_key=key)
        client.transactions.delete(first.id)
        assert second.id == first.id


def test_pages_and_events_async() -> None:
    import asyncio

    async def run() -> None:
        async with AsyncDegroshi(KEY, base_url=URL, space_id=SPACE) as client:
            seen = 0
            async for transaction in client.transactions.iterate(per_page=2):
                assert isinstance(transaction.amount, Decimal)
                seen += 1
                if seen >= 5:
                    break
            events = await client.events.list(limit=5)
            assert isinstance(events.data, list)

    asyncio.run(run())
