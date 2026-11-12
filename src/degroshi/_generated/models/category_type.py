from typing import Literal

CategoryType = Literal["expense", "income", "transfer"]

CATEGORY_TYPE_VALUES: set[CategoryType] = {
    "expense",
    "income",
    "transfer",
}


def check_category_type(value: str) -> CategoryType:
    if value in CATEGORY_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATEGORY_TYPE_VALUES!r}")
