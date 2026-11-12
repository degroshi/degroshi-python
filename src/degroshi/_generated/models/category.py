from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.category_spending_kind_type_0 import CategorySpendingKindType0
from ..models.category_spending_kind_type_0 import check_category_spending_kind_type_0
from ..models.category_type import CategoryType
from ..models.category_type import check_category_type
from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="Category")


@_attrs_define
class Category:
    """
    Attributes:
        created_at (datetime.datetime):
        display_order (int):
        id (str):
        is_default (bool):
        name (str): The display name in the request language (Accept-Language, else the user's saved language, else uk).
            A built-in category that still has its seed name is translated ("Продукти" / "Groceries"); custom and renamed
            categories are returned as stored.
        space_id (str):
        type_ (CategoryType):
        updated_at (datetime.datetime):
        business_space_id (None | str | Unset): Marks the subcategory of a business under «Дохід» in its owner's
            personal space: the owner's money from that business lands here. Renaming or moving it keeps the link.
        children (list[Category] | None | Unset):
        color (None | str | Unset):
        depth (int | None | Unset):
        emoji (None | str | Unset): A single emoji for the category (native clients' icon set). Default categories get
            one from the seed; custom ones may have none.
        icon (None | str | Unset): The category's icon: a free Hugeicons slug from the brand category icon set
            (Packages/brand/icons.json), e.g. "shopping-cart-01". Omitted when the category has none (clients draw
            "tag-01").
        parent_id (None | str | Unset):
        spending_kind (CategorySpendingKindType0 | None | Unset): Subscription («Підписки») or mandatory
            («Обов’язкові»); omitted for any other category. The calendar's filter chips and the yearly subscriptions sum
            read it.
        system_key (None | str | Unset): Identifies a built-in (seeded) category, e.g. "food.groceries"; stable across
            languages and renames. Omitted for custom categories.
        version (int | None | Unset): The row version (also the ETag): send it as If-Match on PATCH / DELETE to detect
            concurrent edits (412).
    """

    created_at: datetime.datetime
    display_order: int
    id: str
    is_default: bool
    name: str
    space_id: str
    type_: CategoryType
    updated_at: datetime.datetime
    business_space_id: None | str | Unset = UNSET
    children: list[Category] | None | Unset = UNSET
    color: None | str | Unset = UNSET
    depth: int | None | Unset = UNSET
    emoji: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    spending_kind: CategorySpendingKindType0 | None | Unset = UNSET
    system_key: None | str | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        display_order = self.display_order

        id = self.id

        is_default = self.is_default

        name = self.name

        space_id = self.space_id

        type_: str = self.type_

        updated_at = self.updated_at.isoformat()

        business_space_id: None | str | Unset
        if isinstance(self.business_space_id, Unset):
            business_space_id = UNSET
        else:
            business_space_id = self.business_space_id

        children: list[dict[str, Any]] | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)

        else:
            children = self.children

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        depth: int | None | Unset
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

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

        spending_kind: None | str | Unset
        if isinstance(self.spending_kind, Unset):
            spending_kind = UNSET
        elif isinstance(self.spending_kind, str):
            spending_kind = self.spending_kind
        else:
            spending_kind = self.spending_kind

        system_key: None | str | Unset
        if isinstance(self.system_key, Unset):
            system_key = UNSET
        else:
            system_key = self.system_key

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "display_order": display_order,
                "id": id,
                "is_default": is_default,
                "name": name,
                "space_id": space_id,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if business_space_id is not UNSET:
            field_dict["business_space_id"] = business_space_id
        if children is not UNSET:
            field_dict["children"] = children
        if color is not UNSET:
            field_dict["color"] = color
        if depth is not UNSET:
            field_dict["depth"] = depth
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if icon is not UNSET:
            field_dict["icon"] = icon
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if spending_kind is not UNSET:
            field_dict["spending_kind"] = spending_kind
        if system_key is not UNSET:
            field_dict["system_key"] = system_key
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        display_order = d.pop("display_order")

        id = d.pop("id")

        is_default = d.pop("is_default")

        name = d.pop("name")

        space_id = d.pop("space_id")

        type_ = check_category_type(d.pop("type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_business_space_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_space_id = _parse_business_space_id(d.pop("business_space_id", UNSET))

        def _parse_children(data: object) -> list[Category] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:
                    children_type_0_item = Category.from_dict(children_type_0_item_data)

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Category] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_depth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        depth = _parse_depth(d.pop("depth", UNSET))

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

        def _parse_spending_kind(data: object) -> CategorySpendingKindType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                spending_kind_type_0 = check_category_spending_kind_type_0(data)

                return spending_kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CategorySpendingKindType0 | None | Unset, data)

        spending_kind = _parse_spending_kind(d.pop("spending_kind", UNSET))

        def _parse_system_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_key = _parse_system_key(d.pop("system_key", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        category = cls(
            created_at=created_at,
            display_order=display_order,
            id=id,
            is_default=is_default,
            name=name,
            space_id=space_id,
            type_=type_,
            updated_at=updated_at,
            business_space_id=business_space_id,
            children=children,
            color=color,
            depth=depth,
            emoji=emoji,
            icon=icon,
            parent_id=parent_id,
            spending_kind=spending_kind,
            system_key=system_key,
            version=version,
        )

        category.additional_properties = d
        return category

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
