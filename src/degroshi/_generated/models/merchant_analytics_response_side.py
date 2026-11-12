from typing import Literal

MerchantAnalyticsResponseSide = Literal["expense", "income"]

MERCHANT_ANALYTICS_RESPONSE_SIDE_VALUES: set[MerchantAnalyticsResponseSide] = {
    "expense",
    "income",
}


def check_merchant_analytics_response_side(value: str) -> MerchantAnalyticsResponseSide:
    if value in MERCHANT_ANALYTICS_RESPONSE_SIDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MERCHANT_ANALYTICS_RESPONSE_SIDE_VALUES!r}")
