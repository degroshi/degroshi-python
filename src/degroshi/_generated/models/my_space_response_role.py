from typing import Literal

MySpaceResponseRole = Literal["accountant", "admin", "member", "owner", "viewer"]

MY_SPACE_RESPONSE_ROLE_VALUES: set[MySpaceResponseRole] = {
    "accountant",
    "admin",
    "member",
    "owner",
    "viewer",
}


def check_my_space_response_role(value: str) -> MySpaceResponseRole:
    if value in MY_SPACE_RESPONSE_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MY_SPACE_RESPONSE_ROLE_VALUES!r}")
