from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.upsert_account_request_type_type_0 import check_upsert_account_request_type_type_0
from ..models.upsert_account_request_type_type_0 import UpsertAccountRequestTypeType0
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="UpsertAccountRequest")


@_attrs_define
class UpsertAccountRequest:
    """
    Attributes:
        currency (str): An ISO 4217 code; it can't change after the account is created (409 SRC_004).
        name (str): The account's name in the app, 1 to 100 characters.
        is_liability (bool | None | Unset): `is_liability` marks money owed (a loan, a credit line); default false.
        type_ (None | Unset | UpsertAccountRequestTypeType0): The account's type; without it the source's kind picks one
            (bank: checking, card: debit_card, broker: investment, crypto: ewallet, else account).
    """

    currency: str
    name: str
    is_liability: bool | None | Unset = UNSET
    type_: None | Unset | UpsertAccountRequestTypeType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        name = self.name

        is_liability: bool | None | Unset
        if isinstance(self.is_liability, Unset):
            is_liability = UNSET
        else:
            is_liability = self.is_liability

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, str):
            type_ = self.type_
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "name": name,
            }
        )
        if is_liability is not UNSET:
            field_dict["is_liability"] = is_liability
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        name = d.pop("name")

        def _parse_is_liability(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_liability = _parse_is_liability(d.pop("is_liability", UNSET))

        def _parse_type_(data: object) -> None | Unset | UpsertAccountRequestTypeType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = check_upsert_account_request_type_type_0(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpsertAccountRequestTypeType0, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        upsert_account_request = cls(
            currency=currency,
            name=name,
            is_liability=is_liability,
            type_=type_,
        )

        upsert_account_request.additional_properties = d
        return upsert_account_request

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
