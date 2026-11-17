from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="SandboxResetEventDataObject")


@_attrs_define
class SandboxResetEventDataObject:
    """
    Attributes:
        object_ (str | Unset):
        origin (str | Unset):
        seed_version (float | Unset):
        seeded_at (str | Unset):
        space_id (str | Unset):
    """

    object_: str | Unset = UNSET
    origin: str | Unset = UNSET
    seed_version: float | Unset = UNSET
    seeded_at: str | Unset = UNSET
    space_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        origin = self.origin

        seed_version = self.seed_version

        seeded_at = self.seeded_at

        space_id = self.space_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if origin is not UNSET:
            field_dict["origin"] = origin
        if seed_version is not UNSET:
            field_dict["seed_version"] = seed_version
        if seeded_at is not UNSET:
            field_dict["seeded_at"] = seeded_at
        if space_id is not UNSET:
            field_dict["space_id"] = space_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = d.pop("object", UNSET)

        origin = d.pop("origin", UNSET)

        seed_version = d.pop("seed_version", UNSET)

        seeded_at = d.pop("seeded_at", UNSET)

        space_id = d.pop("space_id", UNSET)

        sandbox_reset_event_data_object = cls(
            object_=object_,
            origin=origin,
            seed_version=seed_version,
            seeded_at=seeded_at,
            space_id=space_id,
        )

        sandbox_reset_event_data_object.additional_properties = d
        return sandbox_reset_event_data_object

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
