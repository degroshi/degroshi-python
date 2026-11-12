from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="AccountBalanceUpdatedEventDataObject")


@_attrs_define
class AccountBalanceUpdatedEventDataObject:
    """
    Attributes:
        account_id (str | Unset):
        as_of (str | Unset):
        balance (str | Unset):
        currency (str | Unset):
        object_ (str | Unset):
    """

    account_id: str | Unset = UNSET
    as_of: str | Unset = UNSET
    balance: str | Unset = UNSET
    currency: str | Unset = UNSET
    object_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        as_of = self.as_of

        balance = self.balance

        currency = self.currency

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if as_of is not UNSET:
            field_dict["as_of"] = as_of
        if balance is not UNSET:
            field_dict["balance"] = balance
        if currency is not UNSET:
            field_dict["currency"] = currency
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        as_of = d.pop("as_of", UNSET)

        balance = d.pop("balance", UNSET)

        currency = d.pop("currency", UNSET)

        object_ = d.pop("object", UNSET)

        account_balance_updated_event_data_object = cls(
            account_id=account_id,
            as_of=as_of,
            balance=balance,
            currency=currency,
            object_=object_,
        )

        account_balance_updated_event_data_object.additional_properties = d
        return account_balance_updated_event_data_object

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
