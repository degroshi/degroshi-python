from typing import Literal

Frequency = Literal["biweekly", "daily", "monthly", "weekly", "yearly"]

FREQUENCY_VALUES: set[Frequency] = {
    "biweekly",
    "daily",
    "monthly",
    "weekly",
    "yearly",
}


def check_frequency(value: str) -> Frequency:
    if value in FREQUENCY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREQUENCY_VALUES!r}")
