from typing import Literal

GetAnalyticsNetWorthShare = Literal["mine", "whole"]

GET_ANALYTICS_NET_WORTH_SHARE_VALUES: set[GetAnalyticsNetWorthShare] = {
    "mine",
    "whole",
}


def check_get_analytics_net_worth_share(value: str) -> GetAnalyticsNetWorthShare:
    if value in GET_ANALYTICS_NET_WORTH_SHARE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_NET_WORTH_SHARE_VALUES!r}")
