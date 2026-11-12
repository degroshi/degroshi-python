from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.grant_info_purpose import check_grant_info_purpose
from ..models.grant_info_purpose import GrantInfoPurpose
from ..models.grant_info_role import check_grant_info_role
from ..models.grant_info_role import GrantInfoRole
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="GrantInfo")


@_attrs_define
class GrantInfo:
    """
    Attributes:
        grant_id (str):
        owner_first_name (str):
        owner_name (str):
        purpose (GrantInfoPurpose):
        role (GrantInfoRole):
        owner_first_name_genitive (None | str | Unset):
    """

    grant_id: str
    owner_first_name: str
    owner_name: str
    purpose: GrantInfoPurpose
    role: GrantInfoRole
    owner_first_name_genitive: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_id = self.grant_id

        owner_first_name = self.owner_first_name

        owner_name = self.owner_name

        purpose: str = self.purpose

        role: str = self.role

        owner_first_name_genitive: None | str | Unset
        if isinstance(self.owner_first_name_genitive, Unset):
            owner_first_name_genitive = UNSET
        else:
            owner_first_name_genitive = self.owner_first_name_genitive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_id": grant_id,
                "owner_first_name": owner_first_name,
                "owner_name": owner_name,
                "purpose": purpose,
                "role": role,
            }
        )
        if owner_first_name_genitive is not UNSET:
            field_dict["owner_first_name_genitive"] = owner_first_name_genitive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_id = d.pop("grant_id")

        owner_first_name = d.pop("owner_first_name")

        owner_name = d.pop("owner_name")

        purpose = check_grant_info_purpose(d.pop("purpose"))

        role = check_grant_info_role(d.pop("role"))

        def _parse_owner_first_name_genitive(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_first_name_genitive = _parse_owner_first_name_genitive(d.pop("owner_first_name_genitive", UNSET))

        grant_info = cls(
            grant_id=grant_id,
            owner_first_name=owner_first_name,
            owner_name=owner_name,
            purpose=purpose,
            role=role,
            owner_first_name_genitive=owner_first_name_genitive,
        )

        grant_info.additional_properties = d
        return grant_info

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
