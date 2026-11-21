# Changelog

Versions follow semver; the major version follows the API's (v1). The API part of each entry comes from comparing the
public spec with the last release (oasdiff); the SDK part lists SDK-only changes.

## 1.0.0b12 (2026-11-21)

### API

- A recurring rule can be a transfer. `kind` gains `transfer`, and the responses now list `standard` and
  `loan_payment` explicitly. A transfer rule names `to_account_id`, plus `to_amount` when the target account is in
  another currency (unset, the amount converts at the payment day's rate). `GET /v1/recurring-transactions/occurrences`
  items carry `kind`, `to_account_id` and `to_account_name`, so a transfer's occurrence names both accounts. Transfers
  count in no income or spending total.

## 1.0.0b11 (2026-11-20)

### API

- `GET /v1/accounts`, `GET /v1/accounts/{id}` and `GET /v1/accounts/net-worth` (`by_account.items`) carry
  `archived_at`, the moment an archived account was closed. It is present only on archived accounts, so a client can
  show when an account was closed. Nothing else changed.

## 1.0.0b10 (2026-11-19)

### API

- `GET /v1/transactions` takes `count=false` together with a cursor (`after`): the page skips counting every
  matching row, so `meta.total` and `total_pages` are 0, while `has_next` and `next_cursor` work as before. Without
  `after` the parameter is ignored and the page counts as it always did. Read the total from the first page and pass
  `count=false` on the pages after it when scrolling a long list.

## 1.0.0b9 (2026-11-19)

### API

- A transaction's inline `place` (create and update) takes `{"ref": "online"}`: the space's one place for purchases
  online, found or made the first time (kind `online`, no name), the same place bank rows bought online get.
- `GET /v1/analytics/merchants` takes `group_by=category` with `limit_per_category` (1 to 20, default 3): one row
  per merchant and category (the one the operation was booked to), the largest of each category, and the new `others`
  (always present, empty without `group_by`) with what each category's rows leave, so a category's rows plus its
  `others` make its spending in `GET /v1/analytics/categories`.
- `GET /v1/analytics/merchants` takes `exclude_recurring=true`: the operations a recurring rule created or matched
  (a split part with its parent's) are left out.

## 1.0.0b8 (2026-11-18)

### API

- `GET /v1/accounts/net-worth` adds `change_24h`: the net worth now against 24 hours earlier (`since`), with
  `previous_net_worth`, `amount` (`net_worth` minus `previous_net_worth`) and `percent` of the earlier net worth
  (absent when that was zero). The earlier net worth replays every counted balance back to `since`, a wallet,
  exchange or broker account at its value of that day, at that day's exchange rates, so market moves count. The field
  is absent when a rate of that day is missing.

## 1.0.0b7 (2026-11-17)

### API

- `GET /v1/transactions` pages by cursor: `meta.next_cursor` (absent on the last page) is the place after the page's
  last row, and `after` starts the next page right after it, with the same filters and `sort` (another sort is a 400).
  Rows added or removed meanwhile don't repeat or skip a row the way `page` numbers do; `page` works as before. The
  amount sorts compare at the latest rates, so a rate change between pages can move a row across the cursor: dedupe
  by id, or walk a date sort.

### SDK

- `transactions.iterate()` walks by `next_cursor` once the API gives one, so a list that changes while it reads no
  longer repeats or skips a row; with an older API it still pages by number.

## 1.0.0b6 (2026-11-17)

### API

- Webhook event `sandbox.reset`: the developer sandbox went back to its demo data (`origin` `api` or `app`, the new
  `seeded_at` and `seed_version`). Only the sandbox sends it; it needs `transactions:read`.
- `fx_basis` on transactions (reference, card or bank): how `amount` was found from `original_amount`. Send `bank`
  when `amount` is what the account was charged: the account learns its own rate from it, and payments the server
  converts for it (an edit of the original, the assistant's drafts) use our rate times that correction.

## 1.0.0b5 (2026-11-17)

### API

- `GET /v1/transactions` and `GET /v1/transactions/day-totals` take `merchant_key`: one merchant's rows, by the key
  analytics gives a merchant (`p:<brand id>`, or `n:<text>` for an unbranded one: the merchant text, lower-cased with
  single spaces).

## 1.0.0b4 (2026-11-16)

### API

- The developer sandbox: a sandbox key starts with `dg_test_` and reaches only its owner's «Пісочниця», a space of
  invented demo data. `POST /v1/sandbox/reset` puts it back to that data (sandbox keys only, else 403 `SBX_004`; 20 a
  day, 429 `SBX_003`); change-feed cursors then get 410. `GET /v1/me/spaces` gains `is_sandbox`. New codes `SBX_001`
  to `SBX_009`.
- `RecurringResponse.day_changes`: the days a monthly rule's occurrences moved to, oldest first (`day`, and `from`,
  the first date on the new day). Omitted while the rule keeps its start date's day.
- `AccountResponse.instalment_plan_id`: a loan account's instalment plan, the active one else the latest; null for an
  account that never had one.

### SDK

- `client.sandbox.reset()` resets the sandbox with a sandbox key (`dg_test_`), on `Degroshi` and `AsyncDegroshi`.

## 1.0.0b3 (2026-11-16)

### API

- Webhook endpoints can be managed with a token that holds `webhooks:manage` (the `full` preset has it):
  `GET`/`POST /v1/webhooks`, `GET`/`PATCH`/`DELETE /v1/webhooks/{id}`, `pause`, `resume`, `rotate-secret`, `test`,
  `resend`, `stats`, `deliveries` and a delivery's `resend`, plus `GET /v1/webhooks/event-types`. A token manages the
  endpoints of the request's space alone whose every event type its scopes read; `space_ids` may be left out on
  create (it can name only that space, else 403 `WHK_009`), and an event type the token can't read answers 403
  `AUTH_007` with `details.required_scope`. The answers to creating and rotating carry the secret; a token can't
  read it back. `CreateEndpointRequest.space_ids` is no longer required.
- `GET /v1/transactions/day-totals`: every day and the response carry `count`, how many rows the list shows for the
  same filters (transfers and cancelled rows included). A day with rows but no money (transfers alone) now appears
  with `spent` and `earned` at 0. Every list filter it already took is now documented on it: places, project,
  counterparty, recurring rule, import, tax review, `include_portfolio_transfers` and `one_row_per_transfer`.
- `GET /v1/analytics/net-worth` takes `share`. With `account_ids` (an account's own chart), `whole` shows those
  accounts as they are: the whole balance and every operation, an account shared with you included. Without
  `account_ids`, net worth counts your part, as before.
- `share` on the analytics endpoints and `GET /v1/transactions/day-totals` is documented: `mine` (your part of an
  account shared with you, the default) or `whole` (the whole account). It used to read "Reserved".
- `AccountBrand.color`: our swatch (a hex colour) for a curated bank or exchange domain, which a provider's folder
  uses as its tint; absent for other domains.
- A refused key gets a code that says why: `AUTH_041` (not a whole key), `AUTH_042` (no such key), `AUTH_043`
  (expired, `details.expired_at`) and `AUTH_044` (revoked, `details.revoked_at`). They all used to be `AUTH_048`,
  which now covers only the remaining cases; all of them are still 401. A key is also accepted as
  `Authorization: Bearer dg_pat_…`.
- New webhook signing secrets start with `dg_whsec_`; secrets starting with `whsec_` keep working.
- A shared account says who has access: `grant.people` (on an account shared with you) lists the owner first, then
  everyone with access, with `user_id`, `name` (the owner's full name, everyone else's first name), `first_name`,
  `avatar_url`, `role` (`owner`, `balance`, `view` or `write`) and `is_owner`; `shared_with` (on your own account)
  gains `user_id` and `avatar_url` once a person accepts. The account sharing fields are no longer marked reserved.

### SDK

- `client.webhooks` manages endpoints: `event_types`, `list`, `get`, `create`, `update`, `delete`, `pause`, `resume`,
  `rotate_secret`, `send_test`, `stats`, `deliveries`, `iterate_deliveries` (follows `meta.next_cursor`), `delivery`,
  `resend_delivery` and `resend`, beside `verify`, on `Degroshi` and `AsyncDegroshi`. `create` isn't retried: a
  second try could make a second endpoint.

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
