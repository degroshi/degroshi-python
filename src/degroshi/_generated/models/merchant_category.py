from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="MerchantCategory")


@_attrs_define
class MerchantCategory:
    """
    Attributes:
        category_id (str):
        category_name (str): The display name in the request language.
        color (None | str | Unset):
        emoji (None | str | Unset):
        icon (None | str | Unset):
        parent_id (None | str | Unset):
    """

    category_id: str
    category_name: str
    color: None | str | Unset = UNSET
    emoji: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        category_name = self.category_name

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        emoji: None | str | Unset
        if isinstance(self.emoji, Unset):
            emoji = UNSET
        else:
            emoji = self.emoji

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_id": category_id,
                "category_name": category_name,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if icon is not UNSET:
            field_dict["icon"] = icon
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("category_id")

        category_name = d.pop("category_name")

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_emoji(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        emoji = _parse_emoji(d.pop("emoji", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        merchant_category = cls(
            category_id=category_id,
            category_name=category_name,
            color=color,
            emoji=emoji,
            icon=icon,
            parent_id=parent_id,
        )

        merchant_category.additional_properties = d
        return merchant_category

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
