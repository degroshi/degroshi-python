from typing import Literal

GetTransactionDayTotalsShare = Literal["mine", "whole"]

GET_TRANSACTION_DAY_TOTALS_SHARE_VALUES: set[GetTransactionDayTotalsShare] = {
    "mine",
    "whole",
}


def check_get_transaction_day_totals_share(value: str) -> GetTransactionDayTotalsShare:
    if value in GET_TRANSACTION_DAY_TOTALS_SHARE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TRANSACTION_DAY_TOTALS_SHARE_VALUES!r}")
