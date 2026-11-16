from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime


T = TypeVar("T", bound="SandboxResponse")


@_attrs_define
class SandboxResponse:
    """
    Attributes:
        name (str):
        resets_left_today (int): `resets_left_today` counts the resets left in the last 24 hours (at most 20).
        seed_version (int): `seed_version` names the demo data's contents; it changes when the seed does.
        seeded_at (datetime.datetime): The last seed: the sandbox's creation or its last reset.
        space_id (str):
    """

    name: str
    resets_left_today: int
    seed_version: int
    seeded_at: datetime.datetime
    space_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resets_left_today = self.resets_left_today

        seed_version = self.seed_version

        seeded_at = self.seeded_at.isoformat()

        space_id = self.space_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resets_left_today": resets_left_today,
                "seed_version": seed_version,
                "seeded_at": seeded_at,
                "space_id": space_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        resets_left_today = d.pop("resets_left_today")

        seed_version = d.pop("seed_version")

        seeded_at = datetime.datetime.fromisoformat(d.pop("seeded_at"))

        space_id = d.pop("space_id")

        sandbox_response = cls(
            name=name,
            resets_left_today=resets_left_today,
            seed_version=seed_version,
            seeded_at=seeded_at,
            space_id=space_id,
        )

        sandbox_response.additional_properties = d
        return sandbox_response

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
