from typing import Literal

InterestPayout = Literal["at_maturity", "capitalized", "monthly", "quarterly"]

INTEREST_PAYOUT_VALUES: set[InterestPayout] = {
    "at_maturity",
    "capitalized",
    "monthly",
    "quarterly",
}


def check_interest_payout(value: str) -> InterestPayout:
    if value in INTEREST_PAYOUT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTEREST_PAYOUT_VALUES!r}")
