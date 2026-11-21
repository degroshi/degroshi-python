from typing import Literal

GrantInfoEditScopeType0 = Literal["all", "own"]

GRANT_INFO_EDIT_SCOPE_TYPE_0_VALUES: set[GrantInfoEditScopeType0] = {
    "all",
    "own",
}


def check_grant_info_edit_scope_type_0(value: str) -> GrantInfoEditScopeType0:
    if value in GRANT_INFO_EDIT_SCOPE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRANT_INFO_EDIT_SCOPE_TYPE_0_VALUES!r}")
