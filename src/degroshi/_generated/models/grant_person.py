from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.grant_person_role import check_grant_person_role
from ..models.grant_person_role import GrantPersonRole
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="GrantPerson")


@_attrs_define
class GrantPerson:
    """
    Attributes:
        first_name (str):
        is_owner (bool):
        name (str):
        role (GrantPersonRole): Owner for the account's owner, else the grant's role.
        user_id (str):
        avatar_url (None | str | Unset): An uploaded photo's API path (load it through the API) or a sign-in provider's
            photo; absent: the initials.
    """

    first_name: str
    is_owner: bool
    name: str
    role: GrantPersonRole
    user_id: str
    avatar_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        is_owner = self.is_owner

        name = self.name

        role: str = self.role

        user_id = self.user_id

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_name": first_name,
                "is_owner": is_owner,
                "name": name,
                "role": role,
                "user_id": user_id,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("first_name")

        is_owner = d.pop("is_owner")

        name = d.pop("name")

        role = check_grant_person_role(d.pop("role"))

        user_id = d.pop("user_id")

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        grant_person = cls(
            first_name=first_name,
            is_owner=is_owner,
            name=name,
            role=role,
            user_id=user_id,
            avatar_url=avatar_url,
        )

        grant_person.additional_properties = d
        return grant_person

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
