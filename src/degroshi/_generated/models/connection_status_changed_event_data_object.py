from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="ConnectionStatusChangedEventDataObject")


@_attrs_define
class ConnectionStatusChangedEventDataObject:
    """
    Attributes:
        id (str | Unset):
        kind (str | Unset):
        object_ (str | Unset):
        provider (str | Unset):
        reason (str | Unset):
        status (str | Unset):
    """

    id: str | Unset = UNSET
    kind: str | Unset = UNSET
    object_: str | Unset = UNSET
    provider: str | Unset = UNSET
    reason: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        object_ = self.object_

        provider = self.provider

        reason = self.reason

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if object_ is not UNSET:
            field_dict["object"] = object_
        if provider is not UNSET:
            field_dict["provider"] = provider
        if reason is not UNSET:
            field_dict["reason"] = reason
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        object_ = d.pop("object", UNSET)

        provider = d.pop("provider", UNSET)

        reason = d.pop("reason", UNSET)

        status = d.pop("status", UNSET)

        connection_status_changed_event_data_object = cls(
            id=id,
            kind=kind,
            object_=object_,
            provider=provider,
            reason=reason,
            status=status,
        )

        connection_status_changed_event_data_object.additional_properties = d
        return connection_status_changed_event_data_object

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
