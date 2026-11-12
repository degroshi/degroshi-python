from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.push_item_status import check_push_item_status
from ..models.push_item_status import PushItemStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.push_original import PushOriginal


T = TypeVar("T", bound="PushItem")


@_attrs_define
class PushItem:
    """
    Attributes:
        account (str | Unset): The external id of one of the source's accounts.
        amount (str | Unset): A signed decimal string in the account's currency: negative is money out. At most 4
            decimals; not 0.
        category_hint (str | Unset): A free word that helps categorize the row (groceries, taxi…).
        date (datetime.date | Unset): A calendar day (YYYY-MM-DD) when the time is unknown; send it or `occurred_at`.
        deleted (bool | Unset): True to remove the row (a cancelled operation).
        description (str | Unset):
        external_id (str | Unset): The row's id in your system, 1 to 200 characters, unique within its account.
        merchant (str | Unset): Where the money went. A later push changes it only while the row has none: the person's
            choice is kept.
        note (str | Unset): The row's note. A later push changes it only while the row has none: a note the person wrote
            is kept.
        occurred_at (str | Unset): A moment with its offset (RFC 3339); send it or `date`.
        original (PushOriginal | Unset):
        replaces (str | Unset): The external id of the pending row this booked row replaces, when your bank gives a
            booked row a new id.
        status (PushItemStatus | Unset): Booked (default) or pending; a pending row is replaced when the same external
            id comes booked.
    """

    account: str | Unset = UNSET
    amount: str | Unset = UNSET
    category_hint: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    deleted: bool | Unset = UNSET
    description: str | Unset = UNSET
    external_id: str | Unset = UNSET
    merchant: str | Unset = UNSET
    note: str | Unset = UNSET
    occurred_at: str | Unset = UNSET
    original: PushOriginal | Unset = UNSET
    replaces: str | Unset = UNSET
    status: PushItemStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.push_original import PushOriginal  # noqa: PLC0415

        account = self.account

        amount = self.amount

        category_hint = self.category_hint

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        deleted = self.deleted

        description = self.description

        external_id = self.external_id

        merchant = self.merchant

        note = self.note

        occurred_at = self.occurred_at

        original: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original, Unset):
            original = self.original.to_dict()

        replaces = self.replaces

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if amount is not UNSET:
            field_dict["amount"] = amount
        if category_hint is not UNSET:
            field_dict["category_hint"] = category_hint
        if date is not UNSET:
            field_dict["date"] = date
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if description is not UNSET:
            field_dict["description"] = description
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if note is not UNSET:
            field_dict["note"] = note
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at
        if original is not UNSET:
            field_dict["original"] = original
        if replaces is not UNSET:
            field_dict["replaces"] = replaces
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.push_original import PushOriginal  # noqa: PLC0415

        d = dict(src_dict)
        account = d.pop("account", UNSET)

        amount = d.pop("amount", UNSET)

        category_hint = d.pop("category_hint", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        deleted = d.pop("deleted", UNSET)

        description = d.pop("description", UNSET)

        external_id = d.pop("external_id", UNSET)

        merchant = d.pop("merchant", UNSET)

        note = d.pop("note", UNSET)

        occurred_at = d.pop("occurred_at", UNSET)

        _original = d.pop("original", UNSET)
        original: PushOriginal | Unset
        if isinstance(_original, Unset):
            original = UNSET
        else:
            original = PushOriginal.from_dict(_original)

        replaces = d.pop("replaces", UNSET)

        _status = d.pop("status", UNSET)
        status: PushItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_push_item_status(_status)

        push_item = cls(
            account=account,
            amount=amount,
            category_hint=category_hint,
            date=date,
            deleted=deleted,
            description=description,
            external_id=external_id,
            merchant=merchant,
            note=note,
            occurred_at=occurred_at,
            original=original,
            replaces=replaces,
            status=status,
        )

        push_item.additional_properties = d
        return push_item

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
