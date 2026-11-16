from typing import Literal

ListWebhookDeliveriesStatus = Literal["failed", "pending", "skipped", "succeeded"]

LIST_WEBHOOK_DELIVERIES_STATUS_VALUES: set[ListWebhookDeliveriesStatus] = {
    "failed",
    "pending",
    "skipped",
    "succeeded",
}


def check_list_webhook_deliveries_status(value: str) -> ListWebhookDeliveriesStatus:
    if value in LIST_WEBHOOK_DELIVERIES_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_WEBHOOK_DELIVERIES_STATUS_VALUES!r}")
