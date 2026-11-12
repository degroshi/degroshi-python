from typing import Literal

AccountType = Literal[
    "account",
    "bonus",
    "card",
    "checking",
    "credit",
    "credit_card",
    "debit_card",
    "ewallet",
    "insurance",
    "investment",
    "loan",
    "mortgage",
    "savings",
]

ACCOUNT_TYPE_VALUES: set[AccountType] = {
    "account",
    "bonus",
    "card",
    "checking",
    "credit",
    "credit_card",
    "debit_card",
    "ewallet",
    "insurance",
    "investment",
    "loan",
    "mortgage",
    "savings",
}


def check_account_type(value: str) -> AccountType:
    if value in ACCOUNT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_TYPE_VALUES!r}")
