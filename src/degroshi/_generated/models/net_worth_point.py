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


T = TypeVar("T", bound="NetWorthPoint")


@_attrs_define
class NetWorthPoint:
    """
    Attributes:
        assets (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        date (datetime.datetime):
        liabilities (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        net_worth (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
    """

    assets: Decimal
    date: datetime.datetime
    liabilities: Decimal
    net_worth: Decimal
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets = decimal_out(self.assets)

        date = self.date.isoformat()

        liabilities = decimal_out(self.liabilities)

        net_worth = decimal_out(self.net_worth)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assets": assets,
                "date": date,
                "liabilities": liabilities,
                "net_worth": net_worth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assets = decimal_in(d.pop("assets"))

        date = datetime.datetime.fromisoformat(d.pop("date"))

        liabilities = decimal_in(d.pop("liabilities"))

        net_worth = decimal_in(d.pop("net_worth"))

        net_worth_point = cls(
            assets=assets,
            date=date,
            liabilities=liabilities,
            net_worth=net_worth,
        )

        net_worth_point.additional_properties = d
        return net_worth_point

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
