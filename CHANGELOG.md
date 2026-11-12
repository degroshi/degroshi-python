# Changelog

Versions follow semver; the major version follows the API's (v1). The API part of each entry comes from comparing the
public spec with the last release (oasdiff); the SDK part lists SDK-only changes.

## 1.0.0b0 (2026-11-12)

### API

- Every operation and webhook of the public API v1: accounts, transactions, categories, budgets, recurring
  payments, analytics, custom sources and events.

### SDK

- `Degroshi` and `AsyncDegroshi` with resource methods, amounts as `Decimal`, typed errors, retries with backoff for
  requests that are safe to repeat, an `Idempotency-Key` on creates, page and cursor iterators, and
  `webhooks.verify`.
