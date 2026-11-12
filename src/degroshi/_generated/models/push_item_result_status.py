from typing import Literal

PushItemResultStatus = Literal["created", "deleted", "failed", "unchanged", "updated"]

PUSH_ITEM_RESULT_STATUS_VALUES: set[PushItemResultStatus] = {
    "created",
    "deleted",
    "failed",
    "unchanged",
    "updated",
}


def check_push_item_result_status(value: str) -> PushItemResultStatus:
    if value in PUSH_ITEM_RESULT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ITEM_RESULT_STATUS_VALUES!r}")
