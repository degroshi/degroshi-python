from typing import Literal

WebhookEventType = Literal[
    "account.balance.updated",
    "budget.threshold_reached",
    "connection.status_changed",
    "import.completed",
    "recurring.due",
    "transaction.created",
    "transaction.deleted",
    "transaction.updated",
    "transactions.bulk_updated",
]

WEBHOOK_EVENT_TYPE_VALUES: set[WebhookEventType] = {
    "account.balance.updated",
    "budget.threshold_reached",
    "connection.status_changed",
    "import.completed",
    "recurring.due",
    "transaction.created",
    "transaction.deleted",
    "transaction.updated",
    "transactions.bulk_updated",
}


def check_webhook_event_type(value: str) -> WebhookEventType:
    if value in WEBHOOK_EVENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_EVENT_TYPE_VALUES!r}")
