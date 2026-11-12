from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.category_review_source import CategoryReviewSource
from ..models.category_review_source import check_category_review_source
from typing import cast


T = TypeVar("T", bound="CategoryReview")


@_attrs_define
class CategoryReview:
    """
    Attributes:
        confidence (float): Confidence of the choice in [0, 1].
        needs_review (bool): Deprecated and always false: nothing is marked for review since 2026-11-10, and the marks
            set before then are ignored.
        source (CategoryReviewSource): The step that chose it: rule, memory, brand, knn, profile, model or web.
    """

    confidence: float
    needs_review: bool
    source: CategoryReviewSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence

        needs_review = self.needs_review

        source: str = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "needs_review": needs_review,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confidence = d.pop("confidence")

        needs_review = d.pop("needs_review")

        source = check_category_review_source(d.pop("source"))

        category_review = cls(
            confidence=confidence,
            needs_review=needs_review,
            source=source,
        )

        category_review.additional_properties = d
        return category_review

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
