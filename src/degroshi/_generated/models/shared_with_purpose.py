from typing import Literal

SharedWithPurpose = Literal["pooled", "show"]

SHARED_WITH_PURPOSE_VALUES: set[SharedWithPurpose] = {
    "pooled",
    "show",
}


def check_shared_with_purpose(value: str) -> SharedWithPurpose:
    if value in SHARED_WITH_PURPOSE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SHARED_WITH_PURPOSE_VALUES!r}")
