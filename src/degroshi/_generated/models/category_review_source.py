from typing import Literal

CategoryReviewSource = Literal["brand", "knn", "memory", "model", "profile", "rule", "web"]

CATEGORY_REVIEW_SOURCE_VALUES: set[CategoryReviewSource] = {
    "brand",
    "knn",
    "memory",
    "model",
    "profile",
    "rule",
    "web",
}


def check_category_review_source(value: str) -> CategoryReviewSource:
    if value in CATEGORY_REVIEW_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATEGORY_REVIEW_SOURCE_VALUES!r}")
