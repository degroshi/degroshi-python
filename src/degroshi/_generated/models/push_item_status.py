from typing import Literal

PushItemStatus = Literal["booked", "pending"]

PUSH_ITEM_STATUS_VALUES: set[PushItemStatus] = {
    "booked",
    "pending",
}


def check_push_item_status(value: str) -> PushItemStatus:
    if value in PUSH_ITEM_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ITEM_STATUS_VALUES!r}")
