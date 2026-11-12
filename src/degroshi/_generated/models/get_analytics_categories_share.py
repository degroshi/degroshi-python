from typing import Literal

GetAnalyticsCategoriesShare = Literal["mine", "whole"]

GET_ANALYTICS_CATEGORIES_SHARE_VALUES: set[GetAnalyticsCategoriesShare] = {
    "mine",
    "whole",
}


def check_get_analytics_categories_share(value: str) -> GetAnalyticsCategoriesShare:
    if value in GET_ANALYTICS_CATEGORIES_SHARE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_CATEGORIES_SHARE_VALUES!r}")
