from typing import Literal

TransactionResponsePlaceSourceType0 = Literal["ai", "device", "merchant", "picked", "receipt"]

TRANSACTION_RESPONSE_PLACE_SOURCE_TYPE_0_VALUES: set[TransactionResponsePlaceSourceType0] = {
    "ai",
    "device",
    "merchant",
    "picked",
    "receipt",
}


def check_transaction_response_place_source_type_0(value: str) -> TransactionResponsePlaceSourceType0:
    if value in TRANSACTION_RESPONSE_PLACE_SOURCE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_RESPONSE_PLACE_SOURCE_TYPE_0_VALUES!r}")
