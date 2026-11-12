from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.event_data_type_0 import EventDataType0


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        api_version (str):
        created (datetime.datetime):
        id (str):
        object_ (str):
        space_id (str):
        test (bool):
        type_ (str):
        data (EventDataType0 | None | Unset):
        source (None | str | Unset):
    """

    api_version: str
    created: datetime.datetime
    id: str
    object_: str
    space_id: str
    test: bool
    type_: str
    data: EventDataType0 | None | Unset = UNSET
    source: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_data_type_0 import EventDataType0  # noqa: PLC0415

        api_version = self.api_version

        created = self.created.isoformat()

        id = self.id

        object_ = self.object_

        space_id = self.space_id

        test = self.test

        type_ = self.type_

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, EventDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_version": api_version,
                "created": created,
                "id": id,
                "object": object_,
                "space_id": space_id,
                "test": test,
                "type": type_,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_data_type_0 import EventDataType0  # noqa: PLC0415

        d = dict(src_dict)
        api_version = d.pop("api_version")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = d.pop("id")

        object_ = d.pop("object")

        space_id = d.pop("space_id")

        test = d.pop("test")

        type_ = d.pop("type")

        def _parse_data(data: object) -> EventDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = EventDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        event = cls(
            api_version=api_version,
            created=created,
            id=id,
            object_=object_,
            space_id=space_id,
            test=test,
            type_=type_,
            data=data,
            source=source,
        )

        event.additional_properties = d
        return event

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
