from typing import Literal

TransactionStatus = Literal["cancelled", "completed", "pending"]

TRANSACTION_STATUS_VALUES: set[TransactionStatus] = {
    "cancelled",
    "completed",
    "pending",
}


def check_transaction_status(value: str) -> TransactionStatus:
    if value in TRANSACTION_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_STATUS_VALUES!r}")
