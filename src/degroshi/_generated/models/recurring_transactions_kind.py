from typing import Literal

RecurringTransactionsKind = Literal["loan_payment", "standard"]

RECURRING_TRANSACTIONS_KIND_VALUES: set[RecurringTransactionsKind] = {
    "loan_payment",
    "standard",
}


def check_recurring_transactions_kind(value: str) -> RecurringTransactionsKind:
    if value in RECURRING_TRANSACTIONS_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECURRING_TRANSACTIONS_KIND_VALUES!r}")
