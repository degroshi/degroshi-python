from typing import Literal

CategorySpendingKindType0 = Literal["mandatory", "subscription"]

CATEGORY_SPENDING_KIND_TYPE_0_VALUES: set[CategorySpendingKindType0] = {
    "mandatory",
    "subscription",
}


def check_category_spending_kind_type_0(value: str) -> CategorySpendingKindType0:
    if value in CATEGORY_SPENDING_KIND_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATEGORY_SPENDING_KIND_TYPE_0_VALUES!r}")
