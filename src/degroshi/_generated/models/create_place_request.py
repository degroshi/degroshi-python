from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.point_name import PointName


T = TypeVar("T", bound="CreatePlaceRequest")


@_attrs_define
class CreatePlaceRequest:
    """
    Attributes:
        city_ref (None | str | Unset): `city_ref` keeps a live pick's city under the person's Name; `provider_ref` is an
            Apple Place ID ("apple:…").
        device (PointName | Unset):
        name (None | str | Unset):
        pin (PointName | Unset):
        provider_ref (None | str | Unset):
        ref (None | str | Unset): Ref stores a result of ours: "gers:…" or "city:…".
    """

    city_ref: None | str | Unset = UNSET
    device: PointName | Unset = UNSET
    name: None | str | Unset = UNSET
    pin: PointName | Unset = UNSET
    provider_ref: None | str | Unset = UNSET
    ref: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.point_name import PointName  # noqa: PLC0415

        city_ref: None | str | Unset
        if isinstance(self.city_ref, Unset):
            city_ref = UNSET
        else:
            city_ref = self.city_ref

        device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device, Unset):
            device = self.device.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        pin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pin, Unset):
            pin = self.pin.to_dict()

        provider_ref: None | str | Unset
        if isinstance(self.provider_ref, Unset):
            provider_ref = UNSET
        else:
            provider_ref = self.provider_ref

        ref: None | str | Unset
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city_ref is not UNSET:
            field_dict["city_ref"] = city_ref
        if device is not UNSET:
            field_dict["device"] = device
        if name is not UNSET:
            field_dict["name"] = name
        if pin is not UNSET:
            field_dict["pin"] = pin
        if provider_ref is not UNSET:
            field_dict["provider_ref"] = provider_ref
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point_name import PointName  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_city_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city_ref = _parse_city_ref(d.pop("city_ref", UNSET))

        _device = d.pop("device", UNSET)
        device: PointName | Unset
        if isinstance(_device, Unset):
            device = UNSET
        else:
            device = PointName.from_dict(_device)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _pin = d.pop("pin", UNSET)
        pin: PointName | Unset
        if isinstance(_pin, Unset):
            pin = UNSET
        else:
            pin = PointName.from_dict(_pin)

        def _parse_provider_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_ref = _parse_provider_ref(d.pop("provider_ref", UNSET))

        def _parse_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref = _parse_ref(d.pop("ref", UNSET))

        create_place_request = cls(
            city_ref=city_ref,
            device=device,
            name=name,
            pin=pin,
            provider_ref=provider_ref,
            ref=ref,
        )

        create_place_request.additional_properties = d
        return create_place_request

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
