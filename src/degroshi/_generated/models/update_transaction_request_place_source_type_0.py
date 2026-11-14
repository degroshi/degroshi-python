from typing import Literal

UpdateTransactionRequestPlaceSourceType0 = Literal["ai", "device", "merchant", "picked", "receipt"]

UPDATE_TRANSACTION_REQUEST_PLACE_SOURCE_TYPE_0_VALUES: set[UpdateTransactionRequestPlaceSourceType0] = {
    "ai",
    "device",
    "merchant",
    "picked",
    "receipt",
}


def check_update_transaction_request_place_source_type_0(value: str) -> UpdateTransactionRequestPlaceSourceType0:
    if value in UPDATE_TRANSACTION_REQUEST_PLACE_SOURCE_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_TRANSACTION_REQUEST_PLACE_SOURCE_TYPE_0_VALUES!r}"
    )
