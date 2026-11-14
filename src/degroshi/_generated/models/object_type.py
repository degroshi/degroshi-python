from typing import Literal

ObjectType = Literal["account", "budget", "category", "recurring_transaction", "transaction"]

OBJECT_TYPE_VALUES: set[ObjectType] = {
    "account",
    "budget",
    "category",
    "recurring_transaction",
    "transaction",
}


def check_object_type(value: str) -> ObjectType:
    if value in OBJECT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OBJECT_TYPE_VALUES!r}")
