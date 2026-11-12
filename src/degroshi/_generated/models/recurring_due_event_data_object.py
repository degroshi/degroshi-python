from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="RecurringDueEventDataObject")


@_attrs_define
class RecurringDueEventDataObject:
    """
    Attributes:
        account_id (str | Unset):
        amount (str | Unset):
        date (str | Unset):
        object_ (str | Unset):
        rule_id (str | Unset):
        transaction_id (str | Unset):
        type_ (str | Unset):
    """

    account_id: str | Unset = UNSET
    amount: str | Unset = UNSET
    date: str | Unset = UNSET
    object_: str | Unset = UNSET
    rule_id: str | Unset = UNSET
    transaction_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        amount = self.amount

        date = self.date

        object_ = self.object_

        rule_id = self.rule_id

        transaction_id = self.transaction_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if date is not UNSET:
            field_dict["date"] = date
        if object_ is not UNSET:
            field_dict["object"] = object_
        if rule_id is not UNSET:
            field_dict["rule_id"] = rule_id
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        amount = d.pop("amount", UNSET)

        date = d.pop("date", UNSET)

        object_ = d.pop("object", UNSET)

        rule_id = d.pop("rule_id", UNSET)

        transaction_id = d.pop("transaction_id", UNSET)

        type_ = d.pop("type", UNSET)

        recurring_due_event_data_object = cls(
            account_id=account_id,
            amount=amount,
            date=date,
            object_=object_,
            rule_id=rule_id,
            transaction_id=transaction_id,
            type_=type_,
        )

        recurring_due_event_data_object.additional_properties = d
        return recurring_due_event_data_object

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
