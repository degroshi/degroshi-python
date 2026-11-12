from typing import Literal

GrantInfoRole = Literal["balance", "view", "write"]

GRANT_INFO_ROLE_VALUES: set[GrantInfoRole] = {
    "balance",
    "view",
    "write",
}


def check_grant_info_role(value: str) -> GrantInfoRole:
    if value in GRANT_INFO_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRANT_INFO_ROLE_VALUES!r}")
