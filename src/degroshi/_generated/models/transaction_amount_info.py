from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="TransactionAmountInfo")


@_attrs_define
class TransactionAmountInfo:
    """
    Attributes:
        currency_code (str):
        decimal_digits (int):
        decimal_places (int):
        symbol (str):
        value (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
    """

    currency_code: str
    decimal_digits: int
    decimal_places: int
    symbol: str
    value: Decimal
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        decimal_digits = self.decimal_digits

        decimal_places = self.decimal_places

        symbol = self.symbol

        value = decimal_out(self.value)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyCode": currency_code,
                "decimalDigits": decimal_digits,
                "decimalPlaces": decimal_places,
                "symbol": symbol,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_code = d.pop("currencyCode")

        decimal_digits = d.pop("decimalDigits")

        decimal_places = d.pop("decimalPlaces")

        symbol = d.pop("symbol")

        value = decimal_in(d.pop("value"))

        transaction_amount_info = cls(
            currency_code=currency_code,
            decimal_digits=decimal_digits,
            decimal_places=decimal_places,
            symbol=symbol,
            value=value,
        )

        transaction_amount_info.additional_properties = d
        return transaction_amount_info

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
