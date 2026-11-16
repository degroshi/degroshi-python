from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.test_event_request_payload import TestEventRequestPayload


T = TypeVar("T", bound="TestEventRequest")


@_attrs_define
class TestEventRequest:
    """
    Attributes:
        payload (TestEventRequestPayload | Unset): The event's data to send instead of its sample, where test payloads
            are on: a JSON object of at most 64 KB with the event's shape (its sample's fields and types). Absent: the
            event's sample.
        type_ (str | Unset):
    """

    payload: TestEventRequestPayload | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_event_request_payload import TestEventRequestPayload  # noqa: PLC0415

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_event_request_payload import TestEventRequestPayload  # noqa: PLC0415

        d = dict(src_dict)
        _payload = d.pop("payload", UNSET)
        payload: TestEventRequestPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = TestEventRequestPayload.from_dict(_payload)

        type_ = d.pop("type", UNSET)

        test_event_request = cls(
            payload=payload,
            type_=type_,
        )

        test_event_request.additional_properties = d
        return test_event_request

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
