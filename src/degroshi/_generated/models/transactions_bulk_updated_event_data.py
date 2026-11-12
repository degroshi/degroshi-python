from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.transactions_bulk_updated_event_data_object import TransactionsBulkUpdatedEventDataObject


T = TypeVar("T", bound="TransactionsBulkUpdatedEventData")


@_attrs_define
class TransactionsBulkUpdatedEventData:
    """
    Attributes:
        object_ (TransactionsBulkUpdatedEventDataObject):
    """

    object_: TransactionsBulkUpdatedEventDataObject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transactions_bulk_updated_event_data_object import TransactionsBulkUpdatedEventDataObject  # noqa: PLC0415

        object_ = self.object_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transactions_bulk_updated_event_data_object import TransactionsBulkUpdatedEventDataObject  # noqa: PLC0415

        d = dict(src_dict)
        object_ = TransactionsBulkUpdatedEventDataObject.from_dict(d.pop("object"))

        transactions_bulk_updated_event_data = cls(
            object_=object_,
        )

        transactions_bulk_updated_event_data.additional_properties = d
        return transactions_bulk_updated_event_data

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
