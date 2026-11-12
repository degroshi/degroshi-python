from typing import Literal

PushedRowStatus = Literal["booked", "cancelled", "pending"]

PUSHED_ROW_STATUS_VALUES: set[PushedRowStatus] = {
    "booked",
    "cancelled",
    "pending",
}


def check_pushed_row_status(value: str) -> PushedRowStatus:
    if value in PUSHED_ROW_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSHED_ROW_STATUS_VALUES!r}")
