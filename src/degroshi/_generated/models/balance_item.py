from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="BalanceItem")


@_attrs_define
class BalanceItem:
    """
    Attributes:
        account (str | Unset): The external id of one of the source's accounts.
        as_of (str | Unset): When the source had this balance (RFC 3339 with offset); an older one than the last applied
            is skipped.
        balance (str | Unset): A signed decimal string in the account's currency (negative is money owed).
    """

    account: str | Unset = UNSET
    as_of: str | Unset = UNSET
    balance: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        as_of = self.as_of

        balance = self.balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if as_of is not UNSET:
            field_dict["as_of"] = as_of
        if balance is not UNSET:
            field_dict["balance"] = balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account", UNSET)

        as_of = d.pop("as_of", UNSET)

        balance = d.pop("balance", UNSET)

        balance_item = cls(
            account=account,
            as_of=as_of,
            balance=balance,
        )

        balance_item.additional_properties = d
        return balance_item

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
