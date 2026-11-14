from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.frequency import check_frequency
from ..models.frequency import Frequency
from ..models.mode import check_mode
from ..models.mode import Mode
from ..models.recurring_transactions_kind import check_recurring_transactions_kind
from ..models.recurring_transactions_kind import RecurringTransactionsKind
from ..models.transactions_transaction_type import check_transactions_transaction_type
from ..models.transactions_transaction_type import TransactionsTransactionType
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.amount_change_response import AmountChangeResponse
    from ..models.brand_response import BrandResponse
    from ..models.last_paid_response import LastPaidResponse


T = TypeVar("T", bound="RecurringResponse")


@_attrs_define
class RecurringResponse:
    """
    Attributes:
        account_id (str):
        amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        created_at (datetime.datetime):
        description (str):
        frequency (Frequency):
        id (str):
        is_active (bool):
        is_variable (bool): The rule's amounts differ by more than 2% (show the average as approximate).
        mode (Mode):
        next_run_at (datetime.datetime):
        paid_count_3m (int):
        reminder_days_before (int):
        reminder_enabled (bool): `reminder_enabled` and `reminder_days_before` are the rule's reminder (0 = on the day,
            at 9:00).
        space_id (str):
        start_date (datetime.datetime):
        type_ (TransactionsTransactionType):
        updated_at (datetime.datetime):
        amount_changes (list[AmountChangeResponse] | None | Unset): The rule's amount from each day on, newest first
            (the last 12, the original included).
        category_id (None | str | Unset):
        created_by (None | str | Unset): The user id of the member who made the rule; omitted for older rules and when
            their account was deleted.
        created_by_name (None | str | Unset): The creator's first name (else the local part of their email), also for
            members who have left the space; omitted with created_by.
        end_date (datetime.datetime | None | Unset):
        kind (None | RecurringTransactionsKind | Unset): standard, or loan_payment for a loan's repayment.
        last_paid (LastPaidResponse | None | Unset):
        merchant (None | str | Unset):
        merchant_brand (BrandResponse | None | Unset):
        note (None | str | Unset):
        paid_average_3m (None | Decimal | Unset): The mean of the linked rows' amounts dated in the last 3 months; null
            without any.
        paused_at (datetime.datetime | None | Unset): When the rule was paused: set whenever is_active turns false (by a
            person, the processor or the account's archiving), omitted while active and for rules paused before 2026-11 (the
            day wasn't recorded).
        project_id (None | str | Unset): The business project the rule's operations get.
        to_account_id (None | str | Unset): The loan a loan_payment pays.
        version (int | None | Unset): The row version (also the ETag): send it as If-Match on PATCH / DELETE / resume /
            post / skip to detect concurrent edits (412).
    """

    account_id: str
    amount: Decimal
    created_at: datetime.datetime
    description: str
    frequency: Frequency
    id: str
    is_active: bool
    is_variable: bool
    mode: Mode
    next_run_at: datetime.datetime
    paid_count_3m: int
    reminder_days_before: int
    reminder_enabled: bool
    space_id: str
    start_date: datetime.datetime
    type_: TransactionsTransactionType
    updated_at: datetime.datetime
    amount_changes: list[AmountChangeResponse] | None | Unset = UNSET
    category_id: None | str | Unset = UNSET
    created_by: None | str | Unset = UNSET
    created_by_name: None | str | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    kind: None | RecurringTransactionsKind | Unset = UNSET
    last_paid: LastPaidResponse | None | Unset = UNSET
    merchant: None | str | Unset = UNSET
    merchant_brand: BrandResponse | None | Unset = UNSET
    note: None | str | Unset = UNSET
    paid_average_3m: None | Decimal | Unset = UNSET
    paused_at: datetime.datetime | None | Unset = UNSET
    project_id: None | str | Unset = UNSET
    to_account_id: None | str | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.amount_change_response import AmountChangeResponse  # noqa: PLC0415
        from ..models.brand_response import BrandResponse  # noqa: PLC0415
        from ..models.last_paid_response import LastPaidResponse  # noqa: PLC0415

        account_id = self.account_id

        amount = decimal_out(self.amount)

        created_at = self.created_at.isoformat()

        description = self.description

        frequency: str = self.frequency

        id = self.id

        is_active = self.is_active

        is_variable = self.is_variable

        mode: str = self.mode

        next_run_at = self.next_run_at.isoformat()

        paid_count_3m = self.paid_count_3m

        reminder_days_before = self.reminder_days_before

        reminder_enabled = self.reminder_enabled

        space_id = self.space_id

        start_date = self.start_date.isoformat()

        type_: str = self.type_

        updated_at = self.updated_at.isoformat()

        amount_changes: list[dict[str, Any]] | None | Unset
        if isinstance(self.amount_changes, Unset):
            amount_changes = UNSET
        elif isinstance(self.amount_changes, list):
            amount_changes = []
            for amount_changes_type_0_item_data in self.amount_changes:
                amount_changes_type_0_item = amount_changes_type_0_item_data.to_dict()
                amount_changes.append(amount_changes_type_0_item)

        else:
            amount_changes = self.amount_changes

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        created_by_name: None | str | Unset
        if isinstance(self.created_by_name, Unset):
            created_by_name = UNSET
        else:
            created_by_name = self.created_by_name

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, str):
            kind = self.kind
        else:
            kind = self.kind

        last_paid: dict[str, Any] | None | Unset
        if isinstance(self.last_paid, Unset):
            last_paid = UNSET
        elif isinstance(self.last_paid, LastPaidResponse):
            last_paid = self.last_paid.to_dict()
        else:
            last_paid = self.last_paid

        merchant: None | str | Unset
        if isinstance(self.merchant, Unset):
            merchant = UNSET
        else:
            merchant = self.merchant

        merchant_brand: dict[str, Any] | None | Unset
        if isinstance(self.merchant_brand, Unset):
            merchant_brand = UNSET
        elif isinstance(self.merchant_brand, BrandResponse):
            merchant_brand = self.merchant_brand.to_dict()
        else:
            merchant_brand = self.merchant_brand

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        paid_average_3m: None | Decimal | Unset
        if isinstance(self.paid_average_3m, Unset):
            paid_average_3m = UNSET
        else:
            paid_average_3m = decimal_out(self.paid_average_3m)

        paused_at: None | str | Unset
        if isinstance(self.paused_at, Unset):
            paused_at = UNSET
        elif isinstance(self.paused_at, datetime.datetime):
            paused_at = self.paused_at.isoformat()
        else:
            paused_at = self.paused_at

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        to_account_id: None | str | Unset
        if isinstance(self.to_account_id, Unset):
            to_account_id = UNSET
        else:
            to_account_id = self.to_account_id

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "amount": amount,
                "created_at": created_at,
                "description": description,
                "frequency": frequency,
                "id": id,
                "is_active": is_active,
                "is_variable": is_variable,
                "mode": mode,
                "next_run_at": next_run_at,
                "paid_count_3m": paid_count_3m,
                "reminder_days_before": reminder_days_before,
                "reminder_enabled": reminder_enabled,
                "space_id": space_id,
                "start_date": start_date,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if amount_changes is not UNSET:
            field_dict["amount_changes"] = amount_changes
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_name is not UNSET:
            field_dict["created_by_name"] = created_by_name
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if kind is not UNSET:
            field_dict["kind"] = kind
        if last_paid is not UNSET:
            field_dict["last_paid"] = last_paid
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if merchant_brand is not UNSET:
            field_dict["merchant_brand"] = merchant_brand
        if note is not UNSET:
            field_dict["note"] = note
        if paid_average_3m is not UNSET:
            field_dict["paid_average_3m"] = paid_average_3m
        if paused_at is not UNSET:
            field_dict["paused_at"] = paused_at
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if to_account_id is not UNSET:
            field_dict["to_account_id"] = to_account_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_change_response import AmountChangeResponse  # noqa: PLC0415
        from ..models.brand_response import BrandResponse  # noqa: PLC0415
        from ..models.last_paid_response import LastPaidResponse  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        amount = decimal_in(d.pop("amount"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        frequency = check_frequency(d.pop("frequency"))

        id = d.pop("id")

        is_active = d.pop("is_active")

        is_variable = d.pop("is_variable")

        mode = check_mode(d.pop("mode"))

        next_run_at = datetime.datetime.fromisoformat(d.pop("next_run_at"))

        paid_count_3m = d.pop("paid_count_3m")

        reminder_days_before = d.pop("reminder_days_before")

        reminder_enabled = d.pop("reminder_enabled")

        space_id = d.pop("space_id")

        start_date = datetime.datetime.fromisoformat(d.pop("start_date"))

        type_ = check_transactions_transaction_type(d.pop("type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_amount_changes(data: object) -> list[AmountChangeResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                amount_changes_type_0 = []
                _amount_changes_type_0 = data
                for amount_changes_type_0_item_data in _amount_changes_type_0:
                    amount_changes_type_0_item = AmountChangeResponse.from_dict(amount_changes_type_0_item_data)

                    amount_changes_type_0.append(amount_changes_type_0_item)

                return amount_changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AmountChangeResponse] | None | Unset, data)

        amount_changes = _parse_amount_changes(d.pop("amount_changes", UNSET))

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_created_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_name = _parse_created_by_name(d.pop("created_by_name", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.datetime.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_kind(data: object) -> None | RecurringTransactionsKind | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = check_recurring_transactions_kind(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecurringTransactionsKind | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_last_paid(data: object) -> LastPaidResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_paid_type_0 = LastPaidResponse.from_dict(data)

                return last_paid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LastPaidResponse | None | Unset, data)

        last_paid = _parse_last_paid(d.pop("last_paid", UNSET))

        def _parse_merchant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        merchant = _parse_merchant(d.pop("merchant", UNSET))

        def _parse_merchant_brand(data: object) -> BrandResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                merchant_brand_type_0 = BrandResponse.from_dict(data)

                return merchant_brand_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrandResponse | None | Unset, data)

        merchant_brand = _parse_merchant_brand(d.pop("merchant_brand", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_paid_average_3m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paid_average_3m = decimal_in(_parse_paid_average_3m(d.pop("paid_average_3m", UNSET)))

        def _parse_paused_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paused_at_type_0 = datetime.datetime.fromisoformat(data)

                return paused_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paused_at = _parse_paused_at(d.pop("paused_at", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_to_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_account_id = _parse_to_account_id(d.pop("to_account_id", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        recurring_response = cls(
            account_id=account_id,
            amount=amount,
            created_at=created_at,
            description=description,
            frequency=frequency,
            id=id,
            is_active=is_active,
            is_variable=is_variable,
            mode=mode,
            next_run_at=next_run_at,
            paid_count_3m=paid_count_3m,
            reminder_days_before=reminder_days_before,
            reminder_enabled=reminder_enabled,
            space_id=space_id,
            start_date=start_date,
            type_=type_,
            updated_at=updated_at,
            amount_changes=amount_changes,
            category_id=category_id,
            created_by=created_by,
            created_by_name=created_by_name,
            end_date=end_date,
            kind=kind,
            last_paid=last_paid,
            merchant=merchant,
            merchant_brand=merchant_brand,
            note=note,
            paid_average_3m=paid_average_3m,
            paused_at=paused_at,
            project_id=project_id,
            to_account_id=to_account_id,
            version=version,
        )

        recurring_response.additional_properties = d
        return recurring_response

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
