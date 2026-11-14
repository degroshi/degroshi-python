from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.places_kind import check_places_kind
from ..models.places_kind import PlacesKind
from ..models.precision import check_precision
from ..models.precision import Precision
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="TransactionPlace")


@_attrs_define
class TransactionPlace:
    """
    Attributes:
        id (str):
        is_approximate (bool):
        kind (PlacesKind):
        precision (Precision):
        title (str):
        city (None | str | Unset):
        country_code (None | str | Unset):
    """

    id: str
    is_approximate: bool
    kind: PlacesKind
    precision: Precision
    title: str
    city: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_approximate = self.is_approximate

        kind: str = self.kind

        precision: str = self.precision

        title = self.title

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "is_approximate": is_approximate,
                "kind": kind,
                "precision": precision,
                "title": title,
            }
        )
        if city is not UNSET:
            field_dict["city"] = city
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_approximate = d.pop("is_approximate")

        kind = check_places_kind(d.pop("kind"))

        precision = check_precision(d.pop("precision"))

        title = d.pop("title")

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        transaction_place = cls(
            id=id,
            is_approximate=is_approximate,
            kind=kind,
            precision=precision,
            title=title,
            city=city,
            country_code=country_code,
        )

        transaction_place.additional_properties = d
        return transaction_place

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
