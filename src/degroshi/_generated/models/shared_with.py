from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.shared_with_purpose import check_shared_with_purpose
from ..models.shared_with_purpose import SharedWithPurpose
from ..models.shared_with_role import check_shared_with_role
from ..models.shared_with_role import SharedWithRole
from ..models.shared_with_status import check_shared_with_status
from ..models.shared_with_status import SharedWithStatus
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="SharedWith")


@_attrs_define
class SharedWith:
    """
    Attributes:
        grant_id (str):
        purpose (SharedWithPurpose):
        role (SharedWithRole):
        status (SharedWithStatus):
        email (None | str | Unset):
        first_name (None | str | Unset):
        name (None | str | Unset):
    """

    grant_id: str
    purpose: SharedWithPurpose
    role: SharedWithRole
    status: SharedWithStatus
    email: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_id = self.grant_id

        purpose: str = self.purpose

        role: str = self.role

        status: str = self.status

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_id": grant_id,
                "purpose": purpose,
                "role": role,
                "status": status,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_id = d.pop("grant_id")

        purpose = check_shared_with_purpose(d.pop("purpose"))

        role = check_shared_with_role(d.pop("role"))

        status = check_shared_with_status(d.pop("status"))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        shared_with = cls(
            grant_id=grant_id,
            purpose=purpose,
            role=role,
            status=status,
            email=email,
            first_name=first_name,
            name=name,
        )

        shared_with.additional_properties = d
        return shared_with

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
