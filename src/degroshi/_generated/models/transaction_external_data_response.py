from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="TransactionExternalDataResponse")


@_attrs_define
class TransactionExternalDataResponse:
    """
    Attributes:
        banking_transaction_id (None | str | Unset):
        external_id (None | str | Unset):
        external_source (None | str | Unset):
        provider_type (None | str | Unset):
    """

    banking_transaction_id: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    external_source: None | str | Unset = UNSET
    provider_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        banking_transaction_id: None | str | Unset
        if isinstance(self.banking_transaction_id, Unset):
            banking_transaction_id = UNSET
        else:
            banking_transaction_id = self.banking_transaction_id

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_source: None | str | Unset
        if isinstance(self.external_source, Unset):
            external_source = UNSET
        else:
            external_source = self.external_source

        provider_type: None | str | Unset
        if isinstance(self.provider_type, Unset):
            provider_type = UNSET
        else:
            provider_type = self.provider_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if banking_transaction_id is not UNSET:
            field_dict["bankingTransactionId"] = banking_transaction_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if external_source is not UNSET:
            field_dict["externalSource"] = external_source
        if provider_type is not UNSET:
            field_dict["providerType"] = provider_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_banking_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        banking_transaction_id = _parse_banking_transaction_id(d.pop("bankingTransactionId", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_external_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_source = _parse_external_source(d.pop("externalSource", UNSET))

        def _parse_provider_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_type = _parse_provider_type(d.pop("providerType", UNSET))

        transaction_external_data_response = cls(
            banking_transaction_id=banking_transaction_id,
            external_id=external_id,
            external_source=external_source,
            provider_type=provider_type,
        )

        transaction_external_data_response.additional_properties = d
        return transaction_external_data_response

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
