# Degroshi for Python

[![PyPI](https://img.shields.io/pypi/v/degroshi)](https://pypi.org/project/degroshi/)
[![CI](https://github.com/degroshi/degroshi-python/actions/workflows/ci.yml/badge.svg)](https://github.com/degroshi/degroshi-python/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

The official SDK for the [Degroshi API](https://docs.degroshi.com/en/developers). It has typed methods for accounts,
transactions, categories, budgets, recurring payments, analytics, custom sources and events, with blocking and asyncio
clients. Amounts are `Decimal`, retries are safe to repeat, and webhook signatures are checked for you. Python 3.11+.

## Install

```sh
pip install degroshi
```

While 1.0 is in beta, ask pip for it: `pip install --pre degroshi`.

## Authenticate

Create a personal access token in Degroshi under "Settings" › "For developers", and keep it on a server: anyone who
reads it can use it. The client takes it as `api_key`, or reads `DEGROSHI_API_KEY` from the environment.

```python
import os

from degroshi import Degroshi

with Degroshi(os.environ["DEGROSHI_API_KEY"]) as degroshi:
    accounts = degroshi.accounts.list()
```

A token that reaches several spaces needs the space too: `Degroshi(api_key, space_id=...)`. The IDs are under
"Settings" › "For developers" › "Space IDs".

The asyncio client has the same methods: `async with AsyncDegroshi(...) as degroshi`, `await` each call, and
`async for` over the iterators.

## Pagination

`transactions.list()` returns one page: `data` and `meta` (`page`, `per_page`, `total`, `has_next`).
`transactions.iterate()` walks every page for you:

```python
from datetime import date

for transaction in degroshi.transactions.iterate(from_date=date(2026, 11, 1)):
    print(transaction.transaction_date, transaction.direction, transaction.amount)
```

Lists that use cursors (`sources.iterate_pushed`, `events.iterate`) follow `next_cursor` the same way.

## Money

Amounts are `decimal.Decimal`, read from the strings the API sends (`"642.30"`), never `float`. Send them as `Decimal`
or as strings. Totals across currencies come from the API's analytics, already converted.

## Write safely

`transactions.create`, `sources.create`, `sources.push_transactions` and `sources.push_balances` send an
`Idempotency-Key`, so a retry after a dropped connection returns the first answer instead of writing twice. Pass your
own with `idempotency_key=` to retry safely across restarts.

Edits take the row's `version` as `if_match=`. If someone changed the row in the meantime, the API answers 412 and the
client raises a `ConflictError`.

## Errors

Every API error is a `DegroshiError` with `status`, `code` (for example `TXN_ACCOUNT_CONNECTED`), `details` and
`correlation_id`; include the `correlation_id` when you contact support. Subclasses name the common cases:
`BadRequestError`, `AuthenticationError`, `PermissionDeniedError`, `NotFoundError`, `ConflictError`,
`UnprocessableEntityError`, `RateLimitError` and `InternalServerError`. A network failure is an `ApiConnectionError`,
and a timeout is an `ApiTimeoutError`.

```python
from degroshi import NotFoundError

try:
    degroshi.accounts.get(account_id)
except NotFoundError:
    print("No such account in this space")
```

Requests that are safe to repeat are retried on network failures, 408, 429, 500, 502, 503 and 504, with backoff and
respecting `Retry-After`. `max_retries` sets how many times (default 2), and `timeout` how long one try may take, in
seconds (default 60).

## Webhooks

Check every delivery before you trust it. Pass the raw body, before any JSON parsing:

```python
import os

from degroshi.webhooks import verify

event = verify(request.body, request.headers["Degroshi-Signature"], os.environ["WEBHOOK_SECRET"])
if event["type"] == "transaction.created":
    print(event["data"]["object"]["amount"])
```

`verify` raises a `WebhookVerificationError` with a `reason` for a wrong signature, a malformed header or a signature
older than five minutes. While you rotate a secret, either secret passes.

`degroshi.events.iterate()` reads the space's events of the last 30 days, in the same shape as webhook deliveries, so
you can catch up after downtime.

## Documentation

- [Developer guide](https://docs.degroshi.com/en/developers): tokens, spaces, limits and errors.
- [API reference](https://docs.degroshi.com/en/developers/api/me/list-my-spaces): every endpoint and its fields.
- [Webhooks](https://docs.degroshi.com/en/developers/webhooks): events, signatures and retries.

## Versions

The SDK follows semver, and its major version follows the API's (v1). A minor release adds operations or fields, and
a patch release fixes the SDK. Breaking changes come only with a new major version. See [CHANGELOG.md](CHANGELOG.md).

## Contributing and security

Issues are welcome. The SDK is generated from the public API spec, so pull requests aren't merged here directly: see
[CONTRIBUTING.md](CONTRIBUTING.md). Report a vulnerability privately, as [SECURITY.md](SECURITY.md) explains.

## Licence

Apache-2.0: see [LICENSE](LICENSE) and [NOTICE](NOTICE). The Degroshi name and logo aren't licensed.
