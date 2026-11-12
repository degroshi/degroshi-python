from typing import Literal

GetAnalyticsTrendsShare = Literal["mine", "whole"]

GET_ANALYTICS_TRENDS_SHARE_VALUES: set[GetAnalyticsTrendsShare] = {
    "mine",
    "whole",
}


def check_get_analytics_trends_share(value: str) -> GetAnalyticsTrendsShare:
    if value in GET_ANALYTICS_TRENDS_SHARE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_TRENDS_SHARE_VALUES!r}")
