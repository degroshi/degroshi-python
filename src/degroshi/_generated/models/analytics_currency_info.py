from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="AnalyticsCurrencyInfo")


@_attrs_define
class AnalyticsCurrencyInfo:
    """
    Attributes:
        currency_code (str):
        currency_symbol (str):
        decimal_digits (int):
        decimal_places (int):
    """

    currency_code: str
    currency_symbol: str
    decimal_digits: int
    decimal_places: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        currency_symbol = self.currency_symbol

        decimal_digits = self.decimal_digits

        decimal_places = self.decimal_places

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyCode": currency_code,
                "currencySymbol": currency_symbol,
                "decimalDigits": decimal_digits,
                "decimalPlaces": decimal_places,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_code = d.pop("currencyCode")

        currency_symbol = d.pop("currencySymbol")

        decimal_digits = d.pop("decimalDigits")

        decimal_places = d.pop("decimalPlaces")

        analytics_currency_info = cls(
            currency_code=currency_code,
            currency_symbol=currency_symbol,
            decimal_digits=decimal_digits,
            decimal_places=decimal_places,
        )

        analytics_currency_info.additional_properties = d
        return analytics_currency_info

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
