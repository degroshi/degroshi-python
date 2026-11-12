from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.connection_status_changed_event_data_object import ConnectionStatusChangedEventDataObject
    from ..models.connection_status_changed_event_data_previous_attributes import (
        ConnectionStatusChangedEventDataPreviousAttributes,
    )


T = TypeVar("T", bound="ConnectionStatusChangedEventData")


@_attrs_define
class ConnectionStatusChangedEventData:
    """
    Attributes:
        object_ (ConnectionStatusChangedEventDataObject):
        previous_attributes (ConnectionStatusChangedEventDataPreviousAttributes | Unset): The old values of what
            changed, by field.
    """

    object_: ConnectionStatusChangedEventDataObject
    previous_attributes: ConnectionStatusChangedEventDataPreviousAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_status_changed_event_data_object import ConnectionStatusChangedEventDataObject  # noqa: PLC0415
        from ..models.connection_status_changed_event_data_previous_attributes import (
            ConnectionStatusChangedEventDataPreviousAttributes,
        )  # noqa: PLC0415

        object_ = self.object_.to_dict()

        previous_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_attributes, Unset):
            previous_attributes = self.previous_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
            }
        )
        if previous_attributes is not UNSET:
            field_dict["previous_attributes"] = previous_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_status_changed_event_data_object import ConnectionStatusChangedEventDataObject  # noqa: PLC0415
        from ..models.connection_status_changed_event_data_previous_attributes import (
            ConnectionStatusChangedEventDataPreviousAttributes,
        )  # noqa: PLC0415

        d = dict(src_dict)
        object_ = ConnectionStatusChangedEventDataObject.from_dict(d.pop("object"))

        _previous_attributes = d.pop("previous_attributes", UNSET)
        previous_attributes: ConnectionStatusChangedEventDataPreviousAttributes | Unset
        if isinstance(_previous_attributes, Unset):
            previous_attributes = UNSET
        else:
            previous_attributes = ConnectionStatusChangedEventDataPreviousAttributes.from_dict(_previous_attributes)

        connection_status_changed_event_data = cls(
            object_=object_,
            previous_attributes=previous_attributes,
        )

        connection_status_changed_event_data.additional_properties = d
        return connection_status_changed_event_data

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
