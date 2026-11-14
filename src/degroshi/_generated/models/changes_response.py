from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.change import Change


T = TypeVar("T", bound="ChangesResponse")


@_attrs_define
class ChangesResponse:
    """
    Attributes:
        has_more (bool): More changes are waiting now; read again with next_cursor right away.
        items (list[Change]):
        next_cursor (str): `next_cursor` continues after this page: keep it and send it next time, even when items is
            empty.
    """

    has_more: bool
    items: list[Change]
    next_cursor: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.change import Change  # noqa: PLC0415

        has_more = self.has_more

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_more": has_more,
                "items": items,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change import Change  # noqa: PLC0415

        d = dict(src_dict)
        has_more = d.pop("has_more")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Change.from_dict(items_item_data)

            items.append(items_item)

        next_cursor = d.pop("next_cursor")

        changes_response = cls(
            has_more=has_more,
            items=items,
            next_cursor=next_cursor,
        )

        changes_response.additional_properties = d
        return changes_response

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
