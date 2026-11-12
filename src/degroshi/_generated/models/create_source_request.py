from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sources_kind import check_sources_kind
from ..models.sources_kind import SourcesKind
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="CreateSourceRequest")


@_attrs_define
class CreateSourceRequest:
    """
    Attributes:
        name (str): How the source shows in Settings › Підключення, 1 to 80 characters.
        is_read_only (bool | Unset): True by default: the app then changes only its rows' category, merchant, note and
            tags (a row can still be deleted, and the source never brings it back), and adds no rows to its accounts. A
            writable source's accounts take manual rows too, and its rows can be edited; a later push of the same row
            overwrites the edit.
        kind (SourcesKind | Unset):
    """

    name: str
    is_read_only: bool | Unset = UNSET
    kind: SourcesKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_read_only = self.is_read_only

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if is_read_only is not UNSET:
            field_dict["is_read_only"] = is_read_only
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        is_read_only = d.pop("is_read_only", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: SourcesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_sources_kind(_kind)

        create_source_request = cls(
            name=name,
            is_read_only=is_read_only,
            kind=kind,
        )

        create_source_request.additional_properties = d
        return create_source_request

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
