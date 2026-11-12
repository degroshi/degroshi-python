from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="TrendComparison")


@_attrs_define
class TrendComparison:
    """
    Attributes:
        category_id (str):
        category_name (str): The display name in the request language (built-in categories translated, custom ones as
            stored).
        change (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        change_percent (float):
        current_period (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        previous_period (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        trend (str):
    """

    category_id: str
    category_name: str
    change: Decimal
    change_percent: float
    current_period: Decimal
    previous_period: Decimal
    trend: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        category_name = self.category_name

        change = decimal_out(self.change)

        change_percent = self.change_percent

        current_period = decimal_out(self.current_period)

        previous_period = decimal_out(self.previous_period)

        trend = self.trend

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_id": category_id,
                "category_name": category_name,
                "change": change,
                "change_percent": change_percent,
                "current_period": current_period,
                "previous_period": previous_period,
                "trend": trend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("category_id")

        category_name = d.pop("category_name")

        change = decimal_in(d.pop("change"))

        change_percent = d.pop("change_percent")

        current_period = decimal_in(d.pop("current_period"))

        previous_period = decimal_in(d.pop("previous_period"))

        trend = d.pop("trend")

        trend_comparison = cls(
            category_id=category_id,
            category_name=category_name,
            change=change,
            change_percent=change_percent,
            current_period=current_period,
            previous_period=previous_period,
            trend=trend,
        )

        trend_comparison.additional_properties = d
        return trend_comparison

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
