from typing import Literal

TransactionsTransactionType = Literal["expense", "income", "transfer"]

TRANSACTIONS_TRANSACTION_TYPE_VALUES: set[TransactionsTransactionType] = {
    "expense",
    "income",
    "transfer",
}


def check_transactions_transaction_type(value: str) -> TransactionsTransactionType:
    if value in TRANSACTIONS_TRANSACTION_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTIONS_TRANSACTION_TYPE_VALUES!r}")
