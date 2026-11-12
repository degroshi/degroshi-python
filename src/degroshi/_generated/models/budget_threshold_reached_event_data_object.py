from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="BudgetThresholdReachedEventDataObject")


@_attrs_define
class BudgetThresholdReachedEventDataObject:
    """
    Attributes:
        budget_id (str | Unset):
        currency (str | Unset):
        limit (str | Unset):
        object_ (str | Unset):
        period_end (str | Unset):
        period_start (str | Unset):
        spent (str | Unset):
        threshold (float | Unset):
    """

    budget_id: str | Unset = UNSET
    currency: str | Unset = UNSET
    limit: str | Unset = UNSET
    object_: str | Unset = UNSET
    period_end: str | Unset = UNSET
    period_start: str | Unset = UNSET
    spent: str | Unset = UNSET
    threshold: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_id = self.budget_id

        currency = self.currency

        limit = self.limit

        object_ = self.object_

        period_end = self.period_end

        period_start = self.period_start

        spent = self.spent

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if limit is not UNSET:
            field_dict["limit"] = limit
        if object_ is not UNSET:
            field_dict["object"] = object_
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if spent is not UNSET:
            field_dict["spent"] = spent
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_id = d.pop("budget_id", UNSET)

        currency = d.pop("currency", UNSET)

        limit = d.pop("limit", UNSET)

        object_ = d.pop("object", UNSET)

        period_end = d.pop("period_end", UNSET)

        period_start = d.pop("period_start", UNSET)

        spent = d.pop("spent", UNSET)

        threshold = d.pop("threshold", UNSET)

        budget_threshold_reached_event_data_object = cls(
            budget_id=budget_id,
            currency=currency,
            limit=limit,
            object_=object_,
            period_end=period_end,
            period_start=period_start,
            spent=spent,
            threshold=threshold,
        )

        budget_threshold_reached_event_data_object.additional_properties = d
        return budget_threshold_reached_event_data_object

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
