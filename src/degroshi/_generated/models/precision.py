from typing import Literal

Precision = Literal["city", "country", "exact"]

PRECISION_VALUES: set[Precision] = {
    "city",
    "country",
    "exact",
}


def check_precision(value: str) -> Precision:
    if value in PRECISION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRECISION_VALUES!r}")
