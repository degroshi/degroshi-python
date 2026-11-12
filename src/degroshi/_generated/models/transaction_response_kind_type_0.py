from typing import Literal

TransactionResponseKindType0 = Literal["portfolio_transfer"]

TRANSACTION_RESPONSE_KIND_TYPE_0_VALUES: set[TransactionResponseKindType0] = {
    "portfolio_transfer",
}


def check_transaction_response_kind_type_0(value: str) -> TransactionResponseKindType0:
    if value in TRANSACTION_RESPONSE_KIND_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_RESPONSE_KIND_TYPE_0_VALUES!r}")
