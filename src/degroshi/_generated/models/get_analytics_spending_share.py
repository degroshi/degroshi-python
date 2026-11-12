from typing import Literal

GetAnalyticsSpendingShare = Literal["mine", "whole"]

GET_ANALYTICS_SPENDING_SHARE_VALUES: set[GetAnalyticsSpendingShare] = {
    "mine",
    "whole",
}


def check_get_analytics_spending_share(value: str) -> GetAnalyticsSpendingShare:
    if value in GET_ANALYTICS_SPENDING_SHARE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_SPENDING_SHARE_VALUES!r}")
