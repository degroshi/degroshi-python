from typing import Literal

Status = Literal["active", "paused"]

STATUS_VALUES: set[Status] = {
    "active",
    "paused",
}


def check_status(value: str) -> Status:
    if value in STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_VALUES!r}")
