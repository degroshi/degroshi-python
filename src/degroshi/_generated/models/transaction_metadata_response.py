from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.transactions_transaction_type import check_transactions_transaction_type
from ..models.transactions_transaction_type import TransactionsTransactionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.transaction_metadata_response_provider_data_type_0 import TransactionMetadataResponseProviderDataType0


T = TypeVar("T", bound="TransactionMetadataResponse")


@_attrs_define
class TransactionMetadataResponse:
    """
    Attributes:
        child_splits_total (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        has_child_splits (bool):
        is_income (bool):
        is_pending (bool):
        is_reconciled (bool):
        is_split (bool):
        is_transfer (bool):
        tax_deductible (bool):
        transaction_type (TransactionsTransactionType):
        unallocated_amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        description (None | str | Unset):
        merchant (None | str | Unset):
        notes (None | str | Unset):
        provider_data (None | TransactionMetadataResponseProviderDataType0 | Unset):
        tax_year (int | None | Unset):
    """

    child_splits_total: Decimal
    has_child_splits: bool
    is_income: bool
    is_pending: bool
    is_reconciled: bool
    is_split: bool
    is_transfer: bool
    tax_deductible: bool
    transaction_type: TransactionsTransactionType
    unallocated_amount: Decimal
    description: None | str | Unset = UNSET
    merchant: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    provider_data: None | TransactionMetadataResponseProviderDataType0 | Unset = UNSET
    tax_year: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_metadata_response_provider_data_type_0 import (
            TransactionMetadataResponseProviderDataType0,
        )  # noqa: PLC0415

        child_splits_total = decimal_out(self.child_splits_total)

        has_child_splits = self.has_child_splits

        is_income = self.is_income

        is_pending = self.is_pending

        is_reconciled = self.is_reconciled

        is_split = self.is_split

        is_transfer = self.is_transfer

        tax_deductible = self.tax_deductible

        transaction_type: str = self.transaction_type

        unallocated_amount = decimal_out(self.unallocated_amount)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        merchant: None | str | Unset
        if isinstance(self.merchant, Unset):
            merchant = UNSET
        else:
            merchant = self.merchant

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        provider_data: dict[str, Any] | None | Unset
        if isinstance(self.provider_data, Unset):
            provider_data = UNSET
        elif isinstance(self.provider_data, TransactionMetadataResponseProviderDataType0):
            provider_data = self.provider_data.to_dict()
        else:
            provider_data = self.provider_data

        tax_year: int | None | Unset
        if isinstance(self.tax_year, Unset):
            tax_year = UNSET
        else:
            tax_year = self.tax_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "childSplitsTotal": child_splits_total,
                "hasChildSplits": has_child_splits,
                "isIncome": is_income,
                "isPending": is_pending,
                "isReconciled": is_reconciled,
                "isSplit": is_split,
                "isTransfer": is_transfer,
                "taxDeductible": tax_deductible,
                "transactionType": transaction_type,
                "unallocatedAmount": unallocated_amount,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if notes is not UNSET:
            field_dict["notes"] = notes
        if provider_data is not UNSET:
            field_dict["providerData"] = provider_data
        if tax_year is not UNSET:
            field_dict["taxYear"] = tax_year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_metadata_response_provider_data_type_0 import (
            TransactionMetadataResponseProviderDataType0,
        )  # noqa: PLC0415

        d = dict(src_dict)
        child_splits_total = decimal_in(d.pop("childSplitsTotal"))

        has_child_splits = d.pop("hasChildSplits")

        is_income = d.pop("isIncome")

        is_pending = d.pop("isPending")

        is_reconciled = d.pop("isReconciled")

        is_split = d.pop("isSplit")

        is_transfer = d.pop("isTransfer")

        tax_deductible = d.pop("taxDeductible")

        transaction_type = check_transactions_transaction_type(d.pop("transactionType"))

        unallocated_amount = decimal_in(d.pop("unallocatedAmount"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_merchant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        merchant = _parse_merchant(d.pop("merchant", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_provider_data(data: object) -> None | TransactionMetadataResponseProviderDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_data_type_0 = TransactionMetadataResponseProviderDataType0.from_dict(data)

                return provider_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionMetadataResponseProviderDataType0 | Unset, data)

        provider_data = _parse_provider_data(d.pop("providerData", UNSET))

        def _parse_tax_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tax_year = _parse_tax_year(d.pop("taxYear", UNSET))

        transaction_metadata_response = cls(
            child_splits_total=child_splits_total,
            has_child_splits=has_child_splits,
            is_income=is_income,
            is_pending=is_pending,
            is_reconciled=is_reconciled,
            is_split=is_split,
            is_transfer=is_transfer,
            tax_deductible=tax_deductible,
            transaction_type=transaction_type,
            unallocated_amount=unallocated_amount,
            description=description,
            merchant=merchant,
            notes=notes,
            provider_data=provider_data,
            tax_year=tax_year,
        )

        transaction_metadata_response.additional_properties = d
        return transaction_metadata_response

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
