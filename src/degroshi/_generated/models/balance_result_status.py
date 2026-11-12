from typing import Literal

BalanceResultStatus = Literal["adjusted", "failed", "stale", "unchanged"]

BALANCE_RESULT_STATUS_VALUES: set[BalanceResultStatus] = {
    "adjusted",
    "failed",
    "stale",
    "unchanged",
}


def check_balance_result_status(value: str) -> BalanceResultStatus:
    if value in BALANCE_RESULT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_RESULT_STATUS_VALUES!r}")
