from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.transaction_amount_info import TransactionAmountInfo


T = TypeVar("T", bound="TransactionAmountsResponse")


@_attrs_define
class TransactionAmountsResponse:
    """
    Attributes:
        in_account_currency (TransactionAmountInfo):
        in_base_currency (TransactionAmountInfo):
        in_transaction_currency (TransactionAmountInfo):
    """

    in_account_currency: TransactionAmountInfo
    in_base_currency: TransactionAmountInfo
    in_transaction_currency: TransactionAmountInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_amount_info import TransactionAmountInfo  # noqa: PLC0415

        in_account_currency = self.in_account_currency.to_dict()

        in_base_currency = self.in_base_currency.to_dict()

        in_transaction_currency = self.in_transaction_currency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inAccountCurrency": in_account_currency,
                "inBaseCurrency": in_base_currency,
                "inTransactionCurrency": in_transaction_currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_amount_info import TransactionAmountInfo  # noqa: PLC0415

        d = dict(src_dict)
        in_account_currency = TransactionAmountInfo.from_dict(d.pop("inAccountCurrency"))

        in_base_currency = TransactionAmountInfo.from_dict(d.pop("inBaseCurrency"))

        in_transaction_currency = TransactionAmountInfo.from_dict(d.pop("inTransactionCurrency"))

        transaction_amounts_response = cls(
            in_account_currency=in_account_currency,
            in_base_currency=in_base_currency,
            in_transaction_currency=in_transaction_currency,
        )

        transaction_amounts_response.additional_properties = d
        return transaction_amounts_response

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
