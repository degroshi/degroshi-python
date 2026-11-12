import httpx2
import pytest

from degroshi._retry import RetryTransport, is_retry_safe, retry_delay


def sequence(*answers: int | Exception) -> tuple[httpx2.MockTransport, list[httpx2.Request]]:
    seen: list[httpx2.Request] = []
    queue = list(answers)

    def handler(request: httpx2.Request) -> httpx2.Response:
        seen.append(request)
        answer = queue.pop(0) if queue else 200
        if isinstance(answer, Exception):
            raise answer
        return httpx2.Response(answer, json={})

    return httpx2.MockTransport(handler), seen


def send(transport: httpx2.BaseTransport, method: str = "GET", headers: dict | None = None) -> httpx2.Response:
    with httpx2.Client(transport=transport, base_url="https://api.test") as client:
        return client.request(method, "/v1/accounts", headers=headers, json={} if method != "GET" else None)


def test_retries_a_read_after_a_503() -> None:
    # Arrange
    mock, seen = sequence(503, 200)

    # Act
    actual = send(RetryTransport(mock, max_retries=2, sleep=lambda _: None))

    # Assert
    assert actual.status_code == 200
    assert len(seen) == 2


def test_never_repeats_a_post_without_a_key() -> None:
    # Arrange
    mock, seen = sequence(503)

    # Act
    actual = send(RetryTransport(mock, max_retries=2, sleep=lambda _: None), "POST")

    # Assert
    assert actual.status_code == 503
    assert len(seen) == 1


def test_repeats_a_keyed_post_after_a_network_error() -> None:
    # Arrange
    mock, seen = sequence(httpx2.ConnectError("down"), 201)

    # Act
    actual = send(RetryTransport(mock, max_retries=2, sleep=lambda _: None), "POST", {"Idempotency-Key": "k-1"})

    # Assert
    assert actual.status_code == 201
    assert len(seen) == 2
    assert seen[1].headers["Idempotency-Key"] == "k-1"


def test_gives_up_after_the_retries() -> None:
    # Arrange
    mock, _ = sequence(httpx2.ConnectError("down"), httpx2.ConnectError("down"), httpx2.ConnectError("down"))

    # Act & Assert
    with pytest.raises(httpx2.ConnectError):
        send(RetryTransport(mock, max_retries=2, sleep=lambda _: None))


def test_retry_delay() -> None:
    assert retry_delay(1, httpx2.Response(429, headers={"Retry-After": "3"})) == 3.0
    assert retry_delay(1, httpx2.Response(429, headers={"Retry-After": "600"})) == 60.0
    assert retry_delay(1, None, rand=lambda: 0.5) == 0.5
    assert retry_delay(10, None, rand=lambda: 0.5) == 8.0


@pytest.mark.parametrize(
    ("method", "has_key", "expected"),
    [
        ("GET", False, True),
        ("DELETE", False, True),
        ("POST", False, False),
        ("POST", True, True),
        ("PATCH", False, False),
    ],
)
def test_is_retry_safe(method: str, has_key: bool, expected: bool) -> None:
    headers = {"Idempotency-Key": "k"} if has_key else {}
    assert is_retry_safe(httpx2.Request(method, "https://api.test/x", headers=headers)) is expected
