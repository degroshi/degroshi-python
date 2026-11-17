from typing import Literal

TransactionResponseFxBasisType0 = Literal["bank", "card", "reference"]

TRANSACTION_RESPONSE_FX_BASIS_TYPE_0_VALUES: set[TransactionResponseFxBasisType0] = {
    "bank",
    "card",
    "reference",
}


def check_transaction_response_fx_basis_type_0(value: str) -> TransactionResponseFxBasisType0:
    if value in TRANSACTION_RESPONSE_FX_BASIS_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_RESPONSE_FX_BASIS_TYPE_0_VALUES!r}")
