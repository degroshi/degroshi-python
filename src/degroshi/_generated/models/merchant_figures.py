from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="MerchantFigures")


@_attrs_define
class MerchantFigures:
    """
    Attributes:
        amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        count (int):
        previous_amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        previous_count (int):
    """

    amount: Decimal
    count: int
    previous_amount: Decimal
    previous_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = decimal_out(self.amount)

        count = self.count

        previous_amount = decimal_out(self.previous_amount)

        previous_count = self.previous_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "count": count,
                "previous_amount": previous_amount,
                "previous_count": previous_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = decimal_in(d.pop("amount"))

        count = d.pop("count")

        previous_amount = decimal_in(d.pop("previous_amount"))

        previous_count = d.pop("previous_count")

        merchant_figures = cls(
            amount=amount,
            count=count,
            previous_amount=previous_amount,
            previous_count=previous_count,
        )

        merchant_figures.additional_properties = d
        return merchant_figures

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
