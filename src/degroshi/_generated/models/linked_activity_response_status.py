from typing import Literal

LinkedActivityResponseStatus = Literal["confirmed", "failed", "pending"]

LINKED_ACTIVITY_RESPONSE_STATUS_VALUES: set[LinkedActivityResponseStatus] = {
    "confirmed",
    "failed",
    "pending",
}


def check_linked_activity_response_status(value: str) -> LinkedActivityResponseStatus:
    if value in LINKED_ACTIVITY_RESPONSE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINKED_ACTIVITY_RESPONSE_STATUS_VALUES!r}")
