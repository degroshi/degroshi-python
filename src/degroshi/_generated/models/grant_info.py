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

if TYPE_CHECKING:
    from ..models.grant_person import GrantPerson


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
        people (list[GrantPerson] | None | Unset): Everyone with access to the account, for its avatar group: the owner
            first, then every person with an active grant, the requester included, in the order they accepted. Never
            e-mails; invitations aren't people yet.
    """

    grant_id: str
    owner_first_name: str
    owner_name: str
    purpose: GrantInfoPurpose
    role: GrantInfoRole
    owner_first_name_genitive: None | str | Unset = UNSET
    people: list[GrantPerson] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.grant_person import GrantPerson  # noqa: PLC0415

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

        people: list[dict[str, Any]] | None | Unset
        if isinstance(self.people, Unset):
            people = UNSET
        elif isinstance(self.people, list):
            people = []
            for people_type_0_item_data in self.people:
                people_type_0_item = people_type_0_item_data.to_dict()
                people.append(people_type_0_item)

        else:
            people = self.people

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
        if people is not UNSET:
            field_dict["people"] = people

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grant_person import GrantPerson  # noqa: PLC0415

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

        def _parse_people(data: object) -> list[GrantPerson] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                people_type_0 = []
                _people_type_0 = data
                for people_type_0_item_data in _people_type_0:
                    people_type_0_item = GrantPerson.from_dict(people_type_0_item_data)

                    people_type_0.append(people_type_0_item)

                return people_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GrantPerson] | None | Unset, data)

        people = _parse_people(d.pop("people", UNSET))

        grant_info = cls(
            grant_id=grant_id,
            owner_first_name=owner_first_name,
            owner_name=owner_name,
            purpose=purpose,
            role=role,
            owner_first_name_genitive=owner_first_name_genitive,
            people=people,
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
