from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="Meta")


@_attrs_define
class Meta:
    """
    Attributes:
        has_next (bool):
        has_prev (bool):
        page (int):
        per_page (int):
        total (int):
        total_pages (int):
        next_cursor (None | str | Unset): The place after the page's last row on a list that pages by cursor (GET
            /v1/transactions): send it back as after for the next page. Absent on the last page and on lists that page by
            number only.
    """

    has_next: bool
    has_prev: bool
    page: int
    per_page: int
    total: int
    total_pages: int
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_next = self.has_next

        has_prev = self.has_prev

        page = self.page

        per_page = self.per_page

        total = self.total

        total_pages = self.total_pages

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_next": has_next,
                "has_prev": has_prev,
                "page": page,
                "per_page": per_page,
                "total": total,
                "total_pages": total_pages,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_next = d.pop("has_next")

        has_prev = d.pop("has_prev")

        page = d.pop("page")

        per_page = d.pop("per_page")

        total = d.pop("total")

        total_pages = d.pop("total_pages")

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        meta = cls(
            has_next=has_next,
            has_prev=has_prev,
            page=page,
            per_page=per_page,
            total=total,
            total_pages=total_pages,
            next_cursor=next_cursor,
        )

        meta.additional_properties = d
        return meta

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
