from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.catalog_entry_sample_type_0 import CatalogEntrySampleType0


T = TypeVar("T", bound="CatalogEntry")


@_attrs_define
class CatalogEntry:
    """
    Attributes:
        group (str):
        type_ (str):
        sample (CatalogEntrySampleType0 | None | Unset):
    """

    group: str
    type_: str
    sample: CatalogEntrySampleType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_entry_sample_type_0 import CatalogEntrySampleType0  # noqa: PLC0415

        group = self.group

        type_ = self.type_

        sample: dict[str, Any] | None | Unset
        if isinstance(self.sample, Unset):
            sample = UNSET
        elif isinstance(self.sample, CatalogEntrySampleType0):
            sample = self.sample.to_dict()
        else:
            sample = self.sample

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "type": type_,
            }
        )
        if sample is not UNSET:
            field_dict["sample"] = sample

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_entry_sample_type_0 import CatalogEntrySampleType0  # noqa: PLC0415

        d = dict(src_dict)
        group = d.pop("group")

        type_ = d.pop("type")

        def _parse_sample(data: object) -> CatalogEntrySampleType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sample_type_0 = CatalogEntrySampleType0.from_dict(data)

                return sample_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogEntrySampleType0 | None | Unset, data)

        sample = _parse_sample(d.pop("sample", UNSET))

        catalog_entry = cls(
            group=group,
            type_=type_,
            sample=sample,
        )

        catalog_entry.additional_properties = d
        return catalog_entry

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
