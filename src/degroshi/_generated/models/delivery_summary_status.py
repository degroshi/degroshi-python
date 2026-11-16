from typing import Literal

DeliverySummaryStatus = Literal["failed", "pending", "skipped", "succeeded"]

DELIVERY_SUMMARY_STATUS_VALUES: set[DeliverySummaryStatus] = {
    "failed",
    "pending",
    "skipped",
    "succeeded",
}


def check_delivery_summary_status(value: str) -> DeliverySummaryStatus:
    if value in DELIVERY_SUMMARY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_SUMMARY_STATUS_VALUES!r}")
