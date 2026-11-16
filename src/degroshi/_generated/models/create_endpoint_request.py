from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="CreateEndpointRequest")


@_attrs_define
class CreateEndpointRequest:
    """
    Attributes:
        events (list[str]): The types to send (GET /v1/webhooks/event-types).
        url (str): URL is where events go: HTTPS on a public address.
        description (str | Unset):
        space_ids (list[str] | Unset): The spaces whose events go to it; the person must be a member of each. With an
            API key it may be left out: the endpoint covers the request's space (X-Space-ID), the only one it may name.
    """

    events: list[str]
    url: str
    description: str | Unset = UNSET
    space_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = self.events

        url = self.url

        description = self.description

        space_ids: list[str] | Unset = UNSET
        if not isinstance(self.space_ids, Unset):
            space_ids = self.space_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if space_ids is not UNSET:
            field_dict["space_ids"] = space_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = cast(list[str], d.pop("events"))

        url = d.pop("url")

        description = d.pop("description", UNSET)

        space_ids = cast(list[str], d.pop("space_ids", UNSET))

        create_endpoint_request = cls(
            events=events,
            url=url,
            description=description,
            space_ids=space_ids,
        )

        create_endpoint_request.additional_properties = d
        return create_endpoint_request

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
