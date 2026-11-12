from typing import Literal

GetAnalyticsCashFlowShare = Literal["mine", "whole"]

GET_ANALYTICS_CASH_FLOW_SHARE_VALUES: set[GetAnalyticsCashFlowShare] = {
    "mine",
    "whole",
}


def check_get_analytics_cash_flow_share(value: str) -> GetAnalyticsCashFlowShare:
    if value in GET_ANALYTICS_CASH_FLOW_SHARE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_CASH_FLOW_SHARE_VALUES!r}")
