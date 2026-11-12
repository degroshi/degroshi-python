from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.push_item_result import PushItemResult


T = TypeVar("T", bound="PushItemResultEnvelope")


@_attrs_define
class PushItemResultEnvelope:
    """
    Attributes:
        data (PushItemResult):
        success (bool): Always true
    """

    data: PushItemResult
    success: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.push_item_result import PushItemResult  # noqa: PLC0415

        data = self.data.to_dict()

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "success": success,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.push_item_result import PushItemResult  # noqa: PLC0415

        d = dict(src_dict)
        data = PushItemResult.from_dict(d.pop("data"))

        success = d.pop("success")

        push_item_result_envelope = cls(
            data=data,
            success=success,
        )

        push_item_result_envelope.additional_properties = d
        return push_item_result_envelope

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
