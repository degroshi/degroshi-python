from typing import Literal

TransactionResponseUahStatusType0 = Literal["locked", "ok", "pending_rate"]

TRANSACTION_RESPONSE_UAH_STATUS_TYPE_0_VALUES: set[TransactionResponseUahStatusType0] = {
    "locked",
    "ok",
    "pending_rate",
}


def check_transaction_response_uah_status_type_0(value: str) -> TransactionResponseUahStatusType0:
    if value in TRANSACTION_RESPONSE_UAH_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_RESPONSE_UAH_STATUS_TYPE_0_VALUES!r}")
