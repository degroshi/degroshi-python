from typing import Literal

GrantInfoPurpose = Literal["pooled", "show"]

GRANT_INFO_PURPOSE_VALUES: set[GrantInfoPurpose] = {
    "pooled",
    "show",
}


def check_grant_info_purpose(value: str) -> GrantInfoPurpose:
    if value in GRANT_INFO_PURPOSE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRANT_INFO_PURPOSE_VALUES!r}")
