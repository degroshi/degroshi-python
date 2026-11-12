from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="BudgetDisplay")


@_attrs_define
class BudgetDisplay:
    """
    Attributes:
        currency (str):
        remaining (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        total_budget (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        total_spent (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
    """

    currency: str
    remaining: Decimal
    total_budget: Decimal
    total_spent: Decimal
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        remaining = decimal_out(self.remaining)

        total_budget = decimal_out(self.total_budget)

        total_spent = decimal_out(self.total_spent)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "remaining": remaining,
                "total_budget": total_budget,
                "total_spent": total_spent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        remaining = decimal_in(d.pop("remaining"))

        total_budget = decimal_in(d.pop("total_budget"))

        total_spent = decimal_in(d.pop("total_spent"))

        budget_display = cls(
            currency=currency,
            remaining=remaining,
            total_budget=total_budget,
            total_spent=total_spent,
        )

        budget_display.additional_properties = d
        return budget_display

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
