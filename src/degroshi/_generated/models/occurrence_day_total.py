from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime


T = TypeVar("T", bound="OccurrenceDayTotal")


@_attrs_define
class OccurrenceDayTotal:
    """
    Attributes:
        date (datetime.date):
        expense (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        income (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        net (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
    """

    date: datetime.date
    expense: Decimal
    income: Decimal
    net: Decimal
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        expense = decimal_out(self.expense)

        income = decimal_out(self.income)

        net = decimal_out(self.net)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "expense": expense,
                "income": income,
                "net": net,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        expense = decimal_in(d.pop("expense"))

        income = decimal_in(d.pop("income"))

        net = decimal_in(d.pop("net"))

        occurrence_day_total = cls(
            date=date,
            expense=expense,
            income=income,
            net=net,
        )

        occurrence_day_total.additional_properties = d
        return occurrence_day_total

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
