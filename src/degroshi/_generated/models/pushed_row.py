from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pushed_row_status import check_pushed_row_status
from ..models.pushed_row_status import PushedRowStatus
from typing import cast
import datetime


T = TypeVar("T", bound="PushedRow")


@_attrs_define
class PushedRow:
    """
    Attributes:
        amount (str): Signed, in the account's currency (negative is money out).
        external_id (str):
        id (str):
        occurred_at (datetime.datetime):
        removed (bool): True for a deleted row: deleted by a push, or by the person in the app (a push never brings it
            back).
        status (PushedRowStatus): Booked, pending, or cancelled (a pending row never booked within 14 days).
        updated_at (datetime.datetime):
    """

    amount: str
    external_id: str
    id: str
    occurred_at: datetime.datetime
    removed: bool
    status: PushedRowStatus
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        external_id = self.external_id

        id = self.id

        occurred_at = self.occurred_at.isoformat()

        removed = self.removed

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "external_id": external_id,
                "id": id,
                "occurred_at": occurred_at,
                "removed": removed,
                "status": status,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        external_id = d.pop("external_id")

        id = d.pop("id")

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        removed = d.pop("removed")

        status = check_pushed_row_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        pushed_row = cls(
            amount=amount,
            external_id=external_id,
            id=id,
            occurred_at=occurred_at,
            removed=removed,
            status=status,
            updated_at=updated_at,
        )

        pushed_row.additional_properties = d
        return pushed_row

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
