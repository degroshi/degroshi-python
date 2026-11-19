from typing import Literal

GetAnalyticsMerchantsGroupBy = Literal["category"]

GET_ANALYTICS_MERCHANTS_GROUP_BY_VALUES: set[GetAnalyticsMerchantsGroupBy] = {
    "category",
}


def check_get_analytics_merchants_group_by(value: str) -> GetAnalyticsMerchantsGroupBy:
    if value in GET_ANALYTICS_MERCHANTS_GROUP_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_MERCHANTS_GROUP_BY_VALUES!r}")
