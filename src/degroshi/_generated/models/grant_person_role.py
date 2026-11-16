from typing import Literal

GrantPersonRole = Literal["balance", "owner", "view", "write"]

GRANT_PERSON_ROLE_VALUES: set[GrantPersonRole] = {
    "balance",
    "owner",
    "view",
    "write",
}


def check_grant_person_role(value: str) -> GrantPersonRole:
    if value in GRANT_PERSON_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRANT_PERSON_ROLE_VALUES!r}")
