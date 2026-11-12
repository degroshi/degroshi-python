from typing import Literal

GetAnalyticsMerchantsSide = Literal["expense", "income"]

GET_ANALYTICS_MERCHANTS_SIDE_VALUES: set[GetAnalyticsMerchantsSide] = {
    "expense",
    "income",
}


def check_get_analytics_merchants_side(value: str) -> GetAnalyticsMerchantsSide:
    if value in GET_ANALYTICS_MERCHANTS_SIDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_MERCHANTS_SIDE_VALUES!r}")
