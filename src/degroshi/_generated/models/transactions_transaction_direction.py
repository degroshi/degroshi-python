from typing import Literal

TransactionsTransactionDirection = Literal["expense", "income", "transfer_in", "transfer_out"]

TRANSACTIONS_TRANSACTION_DIRECTION_VALUES: set[TransactionsTransactionDirection] = {
    "expense",
    "income",
    "transfer_in",
    "transfer_out",
}


def check_transactions_transaction_direction(value: str) -> TransactionsTransactionDirection:
    if value in TRANSACTIONS_TRANSACTION_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTIONS_TRANSACTION_DIRECTION_VALUES!r}")
