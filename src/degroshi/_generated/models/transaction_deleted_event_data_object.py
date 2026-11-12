from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="TransactionDeletedEventDataObject")


@_attrs_define
class TransactionDeletedEventDataObject:
    """
    Attributes:
        account_id (str | Unset):
        deleted (bool | Unset):
        id (str | Unset):
        object_ (str | Unset):
    """

    account_id: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    id: str | Unset = UNSET
    object_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        deleted = self.deleted

        id = self.id

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if id is not UNSET:
            field_dict["id"] = id
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        deleted = d.pop("deleted", UNSET)

        id = d.pop("id", UNSET)

        object_ = d.pop("object", UNSET)

        transaction_deleted_event_data_object = cls(
            account_id=account_id,
            deleted=deleted,
            id=id,
            object_=object_,
        )

        transaction_deleted_event_data_object.additional_properties = d
        return transaction_deleted_event_data_object

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
