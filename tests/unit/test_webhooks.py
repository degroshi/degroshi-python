import json
from pathlib import Path

import pytest

from degroshi.webhooks import WebhookVerificationError, verify

# The vectors come from the API's own webhook signer, so the SDK and the API agree byte for byte.
VECTORS = json.loads((Path(__file__).parent / "fixtures" / "webhook-vectors.json").read_text())


@pytest.mark.parametrize("vector", VECTORS, ids=[v["name"] for v in VECTORS])
def test_verify_against_the_api_vectors(vector: dict) -> None:
    # Act & Assert
    if vector["expected"] == "ok":
        actual = verify(vector["body"], vector["header"], vector["secret"], now=vector["now"])
        assert actual == json.loads(vector["body"])
        return
    with pytest.raises(WebhookVerificationError) as caught:
        verify(vector["body"], vector["header"], vector["secret"], now=vector["now"])
    assert caught.value.reason == vector["expected"]


def test_takes_the_body_as_bytes() -> None:
    # Arrange
    vector = VECTORS[0]

    # Act
    actual = verify(vector["body"].encode(), vector["header"], vector["secret"], now=vector["now"])

    # Assert
    assert actual["type"] == "transaction.created"
