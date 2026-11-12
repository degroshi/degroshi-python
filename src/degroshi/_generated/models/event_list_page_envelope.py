from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.event_cursor_meta import EventCursorMeta


T = TypeVar("T", bound="EventListPageEnvelope")


@_attrs_define
class EventListPageEnvelope:
    """
    Attributes:
        data (list[Event]):
        meta (EventCursorMeta):
        success (bool): Always true
    """

    data: list[Event]
    meta: EventCursorMeta
    success: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event import Event  # noqa: PLC0415
        from ..models.event_cursor_meta import EventCursorMeta  # noqa: PLC0415

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
                "success": success,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event import Event  # noqa: PLC0415
        from ..models.event_cursor_meta import EventCursorMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Event.from_dict(data_item_data)

            data.append(data_item)

        meta = EventCursorMeta.from_dict(d.pop("meta"))

        success = d.pop("success")

        event_list_page_envelope = cls(
            data=data,
            meta=meta,
            success=success,
        )

        event_list_page_envelope.additional_properties = d
        return event_list_page_envelope

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
