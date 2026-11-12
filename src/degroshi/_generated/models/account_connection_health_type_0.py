from typing import Literal

AccountConnectionHealthType0 = Literal["ok", "reconnect_required", "stale"]

ACCOUNT_CONNECTION_HEALTH_TYPE_0_VALUES: set[AccountConnectionHealthType0] = {
    "ok",
    "reconnect_required",
    "stale",
}


def check_account_connection_health_type_0(value: str) -> AccountConnectionHealthType0:
    if value in ACCOUNT_CONNECTION_HEALTH_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_CONNECTION_HEALTH_TYPE_0_VALUES!r}")
