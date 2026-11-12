from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.my_space_response_kind import check_my_space_response_kind
from ..models.my_space_response_kind import MySpaceResponseKind
from ..models.my_space_response_role import check_my_space_response_role
from ..models.my_space_response_role import MySpaceResponseRole
from typing import cast


T = TypeVar("T", bound="MySpaceResponse")


@_attrs_define
class MySpaceResponse:
    """
    Attributes:
        id (str):
        is_default (bool):
        kind (MySpaceResponseKind):
        name (str):
        role (MySpaceResponseRole):
    """

    id: str
    is_default: bool
    kind: MySpaceResponseKind
    name: str
    role: MySpaceResponseRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_default = self.is_default

        kind: str = self.kind

        name = self.name

        role: str = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "is_default": is_default,
                "kind": kind,
                "name": name,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_default = d.pop("is_default")

        kind = check_my_space_response_kind(d.pop("kind"))

        name = d.pop("name")

        role = check_my_space_response_role(d.pop("role"))

        my_space_response = cls(
            id=id,
            is_default=is_default,
            kind=kind,
            name=name,
            role=role,
        )

        my_space_response.additional_properties = d
        return my_space_response

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
