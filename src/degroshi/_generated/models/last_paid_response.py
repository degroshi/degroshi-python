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


T = TypeVar("T", bound="LastPaidResponse")


@_attrs_define
class LastPaidResponse:
    """
    Attributes:
        amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        date (datetime.date):
        transaction_id (str):
    """

    amount: Decimal
    date: datetime.date
    transaction_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = decimal_out(self.amount)

        date = self.date.isoformat()

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "date": date,
                "transaction_id": transaction_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = decimal_in(d.pop("amount"))

        date = datetime.date.fromisoformat(d.pop("date"))

        transaction_id = d.pop("transaction_id")

        last_paid_response = cls(
            amount=amount,
            date=date,
            transaction_id=transaction_id,
        )

        last_paid_response.additional_properties = d
        return last_paid_response

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
