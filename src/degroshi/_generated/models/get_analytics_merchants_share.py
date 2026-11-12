from typing import Literal

GetAnalyticsMerchantsShare = Literal["mine", "whole"]

GET_ANALYTICS_MERCHANTS_SHARE_VALUES: set[GetAnalyticsMerchantsShare] = {
    "mine",
    "whole",
}


def check_get_analytics_merchants_share(value: str) -> GetAnalyticsMerchantsShare:
    if value in GET_ANALYTICS_MERCHANTS_SHARE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_MERCHANTS_SHARE_VALUES!r}")
