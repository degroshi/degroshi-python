from typing import Literal

AccountConnectionKind = Literal["bank", "exchange", "wallet"]

ACCOUNT_CONNECTION_KIND_VALUES: set[AccountConnectionKind] = {
    "bank",
    "exchange",
    "wallet",
}


def check_account_connection_kind(value: str) -> AccountConnectionKind:
    if value in ACCOUNT_CONNECTION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_CONNECTION_KIND_VALUES!r}")
