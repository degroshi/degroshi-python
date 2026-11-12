from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.meta import Meta
    from ..models.transaction_response import TransactionResponse


T = TypeVar("T", bound="TransactionListResponse")


@_attrs_define
class TransactionListResponse:
    """
    Attributes:
        meta (Meta):
        data (list[TransactionResponse] | None | Unset):
    """

    meta: Meta
    data: list[TransactionResponse] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meta import Meta  # noqa: PLC0415
        from ..models.transaction_response import TransactionResponse  # noqa: PLC0415

        meta = self.meta.to_dict()

        data: list[dict[str, Any]] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta import Meta  # noqa: PLC0415
        from ..models.transaction_response import TransactionResponse  # noqa: PLC0415

        d = dict(src_dict)
        meta = Meta.from_dict(d.pop("meta"))

        def _parse_data(data: object) -> list[TransactionResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = TransactionResponse.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TransactionResponse] | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        transaction_list_response = cls(
            meta=meta,
            data=data,
        )

        transaction_list_response.additional_properties = d
        return transaction_list_response

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
