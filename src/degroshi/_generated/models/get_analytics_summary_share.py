from typing import Literal

GetAnalyticsSummaryShare = Literal["mine", "whole"]

GET_ANALYTICS_SUMMARY_SHARE_VALUES: set[GetAnalyticsSummaryShare] = {
    "mine",
    "whole",
}


def check_get_analytics_summary_share(value: str) -> GetAnalyticsSummaryShare:
    if value in GET_ANALYTICS_SUMMARY_SHARE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_SUMMARY_SHARE_VALUES!r}")
