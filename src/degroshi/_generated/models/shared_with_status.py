from typing import Literal

SharedWithStatus = Literal["active", "invited"]

SHARED_WITH_STATUS_VALUES: set[SharedWithStatus] = {
    "active",
    "invited",
}


def check_shared_with_status(value: str) -> SharedWithStatus:
    if value in SHARED_WITH_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SHARED_WITH_STATUS_VALUES!r}")
