from typing import Literal

TransactionTreatmentSource = Literal["ai", "default_rule", "linker", "user", "user_rule"]

TRANSACTION_TREATMENT_SOURCE_VALUES: set[TransactionTreatmentSource] = {
    "ai",
    "default_rule",
    "linker",
    "user",
    "user_rule",
}


def check_transaction_treatment_source(value: str) -> TransactionTreatmentSource:
    if value in TRANSACTION_TREATMENT_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_TREATMENT_SOURCE_VALUES!r}")
