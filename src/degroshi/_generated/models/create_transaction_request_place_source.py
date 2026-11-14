from typing import Literal

CreateTransactionRequestPlaceSource = Literal["ai", "device", "merchant", "picked", "receipt"]

CREATE_TRANSACTION_REQUEST_PLACE_SOURCE_VALUES: set[CreateTransactionRequestPlaceSource] = {
    "ai",
    "device",
    "merchant",
    "picked",
    "receipt",
}


def check_create_transaction_request_place_source(value: str) -> CreateTransactionRequestPlaceSource:
    if value in CREATE_TRANSACTION_REQUEST_PLACE_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_TRANSACTION_REQUEST_PLACE_SOURCE_VALUES!r}")
