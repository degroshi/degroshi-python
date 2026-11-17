from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="NetWorthChange")


@_attrs_define
class NetWorthChange:
    """
    Attributes:
        amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        previous_net_worth (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        since (datetime.datetime):
        percent (None | Decimal | Unset): Percent of the previous capital's size, two places; absent when the previous
            capital was zero.
    """

    amount: Decimal
    previous_net_worth: Decimal
    since: datetime.datetime
    percent: None | Decimal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = decimal_out(self.amount)

        previous_net_worth = decimal_out(self.previous_net_worth)

        since = self.since.isoformat()

        percent: None | Decimal | Unset
        if isinstance(self.percent, Unset):
            percent = UNSET
        else:
            percent = decimal_out(self.percent)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "previous_net_worth": previous_net_worth,
                "since": since,
            }
        )
        if percent is not UNSET:
            field_dict["percent"] = percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = decimal_in(d.pop("amount"))

        previous_net_worth = decimal_in(d.pop("previous_net_worth"))

        since = datetime.datetime.fromisoformat(d.pop("since"))

        def _parse_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percent = decimal_in(_parse_percent(d.pop("percent", UNSET)))

        net_worth_change = cls(
            amount=amount,
            previous_net_worth=previous_net_worth,
            since=since,
            percent=percent,
        )

        net_worth_change.additional_properties = d
        return net_worth_change

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
