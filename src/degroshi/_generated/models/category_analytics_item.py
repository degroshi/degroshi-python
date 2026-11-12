from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="CategoryAnalyticsItem")


@_attrs_define
class CategoryAnalyticsItem:
    """
    Attributes:
        category_id (str):
        category_name (str): The display name in the request language (built-in categories translated, custom ones as
            stored).
        count (int):
        expenses (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        income (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        net (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        percentage_of_expenses (float):
        percentage_of_income (float):
        children (list[CategoryAnalyticsItem] | None | Unset):
        color (None | str | Unset):
        emoji (None | str | Unset):
        icon (None | str | Unset):
        parent_id (None | str | Unset):
    """

    category_id: str
    category_name: str
    count: int
    expenses: Decimal
    income: Decimal
    net: Decimal
    percentage_of_expenses: float
    percentage_of_income: float
    children: list[CategoryAnalyticsItem] | None | Unset = UNSET
    color: None | str | Unset = UNSET
    emoji: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        category_name = self.category_name

        count = self.count

        expenses = decimal_out(self.expenses)

        income = decimal_out(self.income)

        net = decimal_out(self.net)

        percentage_of_expenses = self.percentage_of_expenses

        percentage_of_income = self.percentage_of_income

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
                "count": count,
                "expenses": expenses,
                "income": income,
                "net": net,
                "percentage_of_expenses": percentage_of_expenses,
                "percentage_of_income": percentage_of_income,
            }
        )
        if children is not UNSET:
            field_dict["children"] = children
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

        count = d.pop("count")

        expenses = decimal_in(d.pop("expenses"))

        income = decimal_in(d.pop("income"))

        net = decimal_in(d.pop("net"))

        percentage_of_expenses = d.pop("percentage_of_expenses")

        percentage_of_income = d.pop("percentage_of_income")

        def _parse_children(data: object) -> list[CategoryAnalyticsItem] | None | Unset:
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
                    children_type_0_item = CategoryAnalyticsItem.from_dict(children_type_0_item_data)

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CategoryAnalyticsItem] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))

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

        category_analytics_item = cls(
            category_id=category_id,
            category_name=category_name,
            count=count,
            expenses=expenses,
            income=income,
            net=net,
            percentage_of_expenses=percentage_of_expenses,
            percentage_of_income=percentage_of_income,
            children=children,
            color=color,
            emoji=emoji,
            icon=icon,
            parent_id=parent_id,
        )

        category_analytics_item.additional_properties = d
        return category_analytics_item

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
