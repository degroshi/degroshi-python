from typing import Literal

UpsertAccountRequestTypeType0 = Literal[
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

UPSERT_ACCOUNT_REQUEST_TYPE_TYPE_0_VALUES: set[UpsertAccountRequestTypeType0] = {
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


def check_upsert_account_request_type_type_0(value: str) -> UpsertAccountRequestTypeType0:
    if value in UPSERT_ACCOUNT_REQUEST_TYPE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPSERT_ACCOUNT_REQUEST_TYPE_TYPE_0_VALUES!r}")
