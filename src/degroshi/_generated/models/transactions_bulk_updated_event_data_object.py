from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="TransactionsBulkUpdatedEventDataObject")


@_attrs_define
class TransactionsBulkUpdatedEventDataObject:
    """
    Attributes:
        batch_id (str | Unset):
        category_id (str | Unset):
        count (float | Unset):
        object_ (str | Unset):
        reason (str | Unset):
    """

    batch_id: str | Unset = UNSET
    category_id: str | Unset = UNSET
    count: float | Unset = UNSET
    object_: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_id = self.batch_id

        category_id = self.category_id

        count = self.count

        object_ = self.object_

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if count is not UNSET:
            field_dict["count"] = count
        if object_ is not UNSET:
            field_dict["object"] = object_
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        batch_id = d.pop("batch_id", UNSET)

        category_id = d.pop("category_id", UNSET)

        count = d.pop("count", UNSET)

        object_ = d.pop("object", UNSET)

        reason = d.pop("reason", UNSET)

        transactions_bulk_updated_event_data_object = cls(
            batch_id=batch_id,
            category_id=category_id,
            count=count,
            object_=object_,
            reason=reason,
        )

        transactions_bulk_updated_event_data_object.additional_properties = d
        return transactions_bulk_updated_event_data_object

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
