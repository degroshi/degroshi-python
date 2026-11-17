from typing import Literal

CreateTransactionRequestFxBasis = Literal["bank", "card", "reference"]

CREATE_TRANSACTION_REQUEST_FX_BASIS_VALUES: set[CreateTransactionRequestFxBasis] = {
    "bank",
    "card",
    "reference",
}


def check_create_transaction_request_fx_basis(value: str) -> CreateTransactionRequestFxBasis:
    if value in CREATE_TRANSACTION_REQUEST_FX_BASIS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_TRANSACTION_REQUEST_FX_BASIS_VALUES!r}")
