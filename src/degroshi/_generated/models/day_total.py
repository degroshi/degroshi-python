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


T = TypeVar("T", bound="DayTotal")


@_attrs_define
class DayTotal:
    """
    Attributes:
        day (datetime.date):
        earned (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        spent (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        rate_pending (bool | None | Unset): `rate_pending` marks a day with a business row still waiting for its NBU
            rate: that row counts at the display rate, so the day's sum may change.
    """

    day: datetime.date
    earned: Decimal
    spent: Decimal
    rate_pending: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day.isoformat()

        earned = decimal_out(self.earned)

        spent = decimal_out(self.spent)

        rate_pending: bool | None | Unset
        if isinstance(self.rate_pending, Unset):
            rate_pending = UNSET
        else:
            rate_pending = self.rate_pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "earned": earned,
                "spent": spent,
            }
        )
        if rate_pending is not UNSET:
            field_dict["rate_pending"] = rate_pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = datetime.date.fromisoformat(d.pop("day"))

        earned = decimal_in(d.pop("earned"))

        spent = decimal_in(d.pop("spent"))

        def _parse_rate_pending(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        rate_pending = _parse_rate_pending(d.pop("rate_pending", UNSET))

        day_total = cls(
            day=day,
            earned=earned,
            spent=spent,
            rate_pending=rate_pending,
        )

        day_total.additional_properties = d
        return day_total

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
