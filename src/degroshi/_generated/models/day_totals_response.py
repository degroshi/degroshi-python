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

if TYPE_CHECKING:
    from ..models.day_total import DayTotal


T = TypeVar("T", bound="DayTotalsResponse")


@_attrs_define
class DayTotalsResponse:
    """
    Attributes:
        currency (str): The display currency the amounts are in.
        earned (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        spent (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        days (list[DayTotal] | None | Unset): The days with any money, newest first.
        unconverted (list[str] | None | Unset): Unconverted names the account currencies left out of the sums for want
            of a rate to the display currency (empty when everything counted).
    """

    currency: str
    earned: Decimal
    spent: Decimal
    days: list[DayTotal] | None | Unset = UNSET
    unconverted: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.day_total import DayTotal  # noqa: PLC0415

        currency = self.currency

        earned = decimal_out(self.earned)

        spent = decimal_out(self.spent)

        days: list[dict[str, Any]] | None | Unset
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = []
            for days_type_0_item_data in self.days:
                days_type_0_item = days_type_0_item_data.to_dict()
                days.append(days_type_0_item)

        else:
            days = self.days

        unconverted: list[str] | None | Unset
        if isinstance(self.unconverted, Unset):
            unconverted = UNSET
        elif isinstance(self.unconverted, list):
            unconverted = self.unconverted

        else:
            unconverted = self.unconverted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "earned": earned,
                "spent": spent,
            }
        )
        if days is not UNSET:
            field_dict["days"] = days
        if unconverted is not UNSET:
            field_dict["unconverted"] = unconverted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.day_total import DayTotal  # noqa: PLC0415

        d = dict(src_dict)
        currency = d.pop("currency")

        earned = decimal_in(d.pop("earned"))

        spent = decimal_in(d.pop("spent"))

        def _parse_days(data: object) -> list[DayTotal] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = []
                _days_type_0 = data
                for days_type_0_item_data in _days_type_0:
                    days_type_0_item = DayTotal.from_dict(days_type_0_item_data)

                    days_type_0.append(days_type_0_item)

                return days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DayTotal] | None | Unset, data)

        days = _parse_days(d.pop("days", UNSET))

        def _parse_unconverted(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unconverted_type_0 = cast(list[str], data)

                return unconverted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        unconverted = _parse_unconverted(d.pop("unconverted", UNSET))

        day_totals_response = cls(
            currency=currency,
            earned=earned,
            spent=spent,
            days=days,
            unconverted=unconverted,
        )

        day_totals_response.additional_properties = d
        return day_totals_response

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
