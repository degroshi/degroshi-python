from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="BrandResponse")


@_attrs_define
class BrandResponse:
    """
    Attributes:
        id (str):
        name (str):
        domain (None | str | Unset):
        icon_url (None | str | Unset):
        logo_url_dark (None | str | Unset):
        logo_url_light (None | str | Unset):
    """

    id: str
    name: str
    domain: None | str | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    logo_url_dark: None | str | Unset = UNSET
    logo_url_light: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        logo_url_dark: None | str | Unset
        if isinstance(self.logo_url_dark, Unset):
            logo_url_dark = UNSET
        else:
            logo_url_dark = self.logo_url_dark

        logo_url_light: None | str | Unset
        if isinstance(self.logo_url_light, Unset):
            logo_url_light = UNSET
        else:
            logo_url_light = self.logo_url_light

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if logo_url_dark is not UNSET:
            field_dict["logo_url_dark"] = logo_url_dark
        if logo_url_light is not UNSET:
            field_dict["logo_url_light"] = logo_url_light

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("icon_url", UNSET))

        def _parse_logo_url_dark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url_dark = _parse_logo_url_dark(d.pop("logo_url_dark", UNSET))

        def _parse_logo_url_light(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url_light = _parse_logo_url_light(d.pop("logo_url_light", UNSET))

        brand_response = cls(
            id=id,
            name=name,
            domain=domain,
            icon_url=icon_url,
            logo_url_dark=logo_url_dark,
            logo_url_light=logo_url_light,
        )

        brand_response.additional_properties = d
        return brand_response

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
