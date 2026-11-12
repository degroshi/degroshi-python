from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CashFlowPoint")


@_attrs_define
class CashFlowPoint:
    """
    Attributes:
        expenses (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        income (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        net (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        period (str):
    """

    expenses: Decimal
    income: Decimal
    net: Decimal
    period: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expenses = decimal_out(self.expenses)

        income = decimal_out(self.income)

        net = decimal_out(self.net)

        period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expenses": expenses,
                "income": income,
                "net": net,
                "period": period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expenses = decimal_in(d.pop("expenses"))

        income = decimal_in(d.pop("income"))

        net = decimal_in(d.pop("net"))

        period = d.pop("period")

        cash_flow_point = cls(
            expenses=expenses,
            income=income,
            net=net,
            period=period,
        )

        cash_flow_point.additional_properties = d
        return cash_flow_point

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
