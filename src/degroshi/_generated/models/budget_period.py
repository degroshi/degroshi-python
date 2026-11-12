from typing import Literal

BudgetPeriod = Literal["custom", "monthly", "weekly", "yearly"]

BUDGET_PERIOD_VALUES: set[BudgetPeriod] = {
    "custom",
    "monthly",
    "weekly",
    "yearly",
}


def check_budget_period(value: str) -> BudgetPeriod:
    if value in BUDGET_PERIOD_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUDGET_PERIOD_VALUES!r}")
