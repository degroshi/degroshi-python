from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="TransactionRelationshipsResponse")


@_attrs_define
class TransactionRelationshipsResponse:
    """
    Attributes:
        account_id (str):
        user_id (str):
        category_id (None | str | Unset):
        parent_transaction_id (None | str | Unset):
    """

    account_id: str
    user_id: str
    category_id: None | str | Unset = UNSET
    parent_transaction_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        user_id = self.user_id

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        parent_transaction_id: None | str | Unset
        if isinstance(self.parent_transaction_id, Unset):
            parent_transaction_id = UNSET
        else:
            parent_transaction_id = self.parent_transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "userId": user_id,
            }
        )
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if parent_transaction_id is not UNSET:
            field_dict["parentTransactionId"] = parent_transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        user_id = d.pop("userId")

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("categoryId", UNSET))

        def _parse_parent_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_transaction_id = _parse_parent_transaction_id(d.pop("parentTransactionId", UNSET))

        transaction_relationships_response = cls(
            account_id=account_id,
            user_id=user_id,
            category_id=category_id,
            parent_transaction_id=parent_transaction_id,
        )

        transaction_relationships_response.additional_properties = d
        return transaction_relationships_response

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
