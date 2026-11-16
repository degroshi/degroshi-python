from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_secret_request_overlap_hours import check_rotate_secret_request_overlap_hours
from ..models.rotate_secret_request_overlap_hours import RotateSecretRequestOverlapHours
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="RotateSecretRequest")


@_attrs_define
class RotateSecretRequest:
    """
    Attributes:
        overlap_hours (RotateSecretRequestOverlapHours | Unset):
    """

    overlap_hours: RotateSecretRequestOverlapHours | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overlap_hours: int | Unset = UNSET
        if not isinstance(self.overlap_hours, Unset):
            overlap_hours = self.overlap_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overlap_hours is not UNSET:
            field_dict["overlap_hours"] = overlap_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _overlap_hours = d.pop("overlap_hours", UNSET)
        overlap_hours: RotateSecretRequestOverlapHours | Unset
        if isinstance(_overlap_hours, Unset):
            overlap_hours = UNSET
        else:
            overlap_hours = check_rotate_secret_request_overlap_hours(_overlap_hours)

        rotate_secret_request = cls(
            overlap_hours=overlap_hours,
        )

        rotate_secret_request.additional_properties = d
        return rotate_secret_request

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
