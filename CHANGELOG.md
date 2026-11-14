# Changelog

Versions follow semver; the major version follows the API's (v1). The API part of each entry comes from comparing the
public spec with the last release (oasdiff); the SDK part lists SDK-only changes.

## 1.0.0b2 (2026-11-14)

### API

- Every operation documents its `429 Too Many Requests` answer (error code `BIZ_080`) with the `Retry-After` and
  `X-RateLimit-*` headers.
- The operations that convert money (accounts, transactions, budgets, recurring occurrences, analytics) document the
  optional `X-Display-Currency` header.
- The reference reads in English throughout: descriptions and examples no longer quote the app's Ukrainian labels,
  and name fields by their JSON names. `x-error-codes` lists only the codes the API answers with, each with its HTTP
  statuses.
- `GET /v1/changes`: the change feed, everything that changed since a cursor, deletions included.
- Transactions carry `linked_activity`: the crypto wallet or exchange activity a row was recorded from (network, hash,
  explorer link, amount and fee legs, status), on reads and in the `transaction.created` / `transaction.updated`
  webhooks.
- Recurring payments can wait for confirmation: a rule's `mode` gains `confirm`, an occurrence's `status` gains
  `awaiting_confirmation`, and `POST /v1/transactions` takes `recurring_occurrence` to record a waiting payment.
- Transactions have a place: `place`, `place_id` and `place_source` on reads and writes, and the list filters `city`,
  `country`, `online` and `place_id`. Places aren't switched on yet, so these stay empty for now.

### SDK

- `changes.list()` and `changes.iterate()`: a `ChangeFeed` (`AsyncChangeFeed` on `AsyncDegroshi`) that pages the feed
  and keeps `cursor` for the next read.
- Every method names its result type instead of `Any`, for `Degroshi` and `AsyncDegroshi` alike.
- The request and response models are public in `degroshi.models` (with `UNSET` and `Unset`).
- Writes take a plain dict in the API's JSON shape as well as a model.
- A delete retried after a lost answer (a dropped connection, a timeout, a 5xx) that then finds nothing (404) counts
  as done: the earlier try deleted it. The stand-in answer is a 204 with `X-Degroshi-Retried-Delete: true`
  (`RETRIED_DELETE_HEADER`). A 404 on the first try still raises `NotFoundError`.

## 1.0.0b1 (2026-11-13)

### API

- `GET /v1/transactions` takes the new optional filters `types`, `statuses`, `category_ids` and
  `treatment_classes`.
- `GET /v1/transactions/day-totals` takes the new optional filters `types`, `statuses` and `category_ids`.

### SDK

- The generated models and `transactions.list` type the new filters.

## 1.0.0b0 (2026-11-12)

### API

- Every operation and webhook of the public API v1: accounts, transactions, categories, budgets, recurring
  payments, analytics, custom sources and events.

### SDK

- `Degroshi` and `AsyncDegroshi` with resource methods, amounts as `Decimal`, typed errors, retries with backoff for
  requests that are safe to repeat, an `Idempotency-Key` on creates, page and cursor iterators, and
  `webhooks.verify`.
