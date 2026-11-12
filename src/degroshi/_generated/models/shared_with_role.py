from typing import Literal

SharedWithRole = Literal["balance", "view", "write"]

SHARED_WITH_ROLE_VALUES: set[SharedWithRole] = {
    "balance",
    "view",
    "write",
}


def check_shared_with_role(value: str) -> SharedWithRole:
    if value in SHARED_WITH_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SHARED_WITH_ROLE_VALUES!r}")
