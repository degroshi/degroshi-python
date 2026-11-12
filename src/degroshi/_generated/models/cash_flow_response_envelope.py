from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.cash_flow_response import CashFlowResponse


T = TypeVar("T", bound="CashFlowResponseEnvelope")


@_attrs_define
class CashFlowResponseEnvelope:
    """
    Attributes:
        data (CashFlowResponse):
        success (bool): Always true
    """

    data: CashFlowResponse
    success: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cash_flow_response import CashFlowResponse  # noqa: PLC0415

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
        from ..models.cash_flow_response import CashFlowResponse  # noqa: PLC0415

        d = dict(src_dict)
        data = CashFlowResponse.from_dict(d.pop("data"))

        success = d.pop("success")

        cash_flow_response_envelope = cls(
            data=data,
            success=success,
        )

        cash_flow_response_envelope.additional_properties = d
        return cash_flow_response_envelope

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
