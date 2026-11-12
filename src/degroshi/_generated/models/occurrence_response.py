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
from ..models.occurrence_status import check_occurrence_status
from ..models.occurrence_status import OccurrenceStatus
from ..models.transactions_transaction_direction import check_transactions_transaction_direction
from ..models.transactions_transaction_direction import TransactionsTransactionDirection
from ..models.transactions_transaction_type import check_transactions_transaction_type
from ..models.transactions_transaction_type import TransactionsTransactionType
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.brand_response import BrandResponse
    from ..models.occurrence_display import OccurrenceDisplay


T = TypeVar("T", bound="OccurrenceResponse")


@_attrs_define
class OccurrenceResponse:
    """
    Attributes:
        account_id (str):
        account_name (str):
        amount (Decimal): Always positive, in the account currency; Direction gives its sign (income adds to the balance,
            expense subtracts).
        currency_code (str):
        date (datetime.date): The scheduled calendar day in the user's zone. When posted, the transaction is dated at
            local noon of that day.
        description (str):
        direction (TransactionsTransactionDirection):
        frequency (Frequency):
        is_due (bool): True when the date is today or earlier in the user's zone: the hourly processor posts the
            occurrence on its next run.
        mode (Mode):
        rule_id (str):
        status (OccurrenceStatus):
        type_ (TransactionsTransactionType):
        category_color (None | str | Unset):
        category_emoji (None | str | Unset):
        category_icon (None | str | Unset): The category's icon, a slug from the category icon set.
        category_id (None | str | Unset):
        category_name (None | str | Unset): The category's display name in the request language (built-in categories
            translated, custom ones as stored).
        display (None | OccurrenceDisplay | Unset): The amount in the display currency the device sent (X-Display-
            Currency), converted at today's rate and rounded to cents; null when that is the account currency, none was sent
            or there is no rate. Clients show it first and amount as the second line.
        merchant (None | str | Unset):
        merchant_brand (BrandResponse | None | Unset): The enriched merchant identity of the rule, when known.
        note (None | str | Unset):
        project_id (None | str | Unset): The business project the rule's operations get.
        transaction_id (None | str | Unset): The row that settled the occurrence (paid), when known.
        wait_until (datetime.date | None | Unset): The last day a track_only rule waits for the row (null for post).
    """

    account_id: str
    account_name: str
    amount: Decimal
    currency_code: str
    date: datetime.date
    description: str
    direction: TransactionsTransactionDirection
    frequency: Frequency
    is_due: bool
    mode: Mode
    rule_id: str
    status: OccurrenceStatus
    type_: TransactionsTransactionType
    category_color: None | str | Unset = UNSET
    category_emoji: None | str | Unset = UNSET
    category_icon: None | str | Unset = UNSET
    category_id: None | str | Unset = UNSET
    category_name: None | str | Unset = UNSET
    display: None | OccurrenceDisplay | Unset = UNSET
    merchant: None | str | Unset = UNSET
    merchant_brand: BrandResponse | None | Unset = UNSET
    note: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    transaction_id: None | str | Unset = UNSET
    wait_until: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brand_response import BrandResponse  # noqa: PLC0415
        from ..models.occurrence_display import OccurrenceDisplay  # noqa: PLC0415

        account_id = self.account_id

        account_name = self.account_name

        amount = decimal_out(self.amount)

        currency_code = self.currency_code

        date = self.date.isoformat()

        description = self.description

        direction: str = self.direction

        frequency: str = self.frequency

        is_due = self.is_due

        mode: str = self.mode

        rule_id = self.rule_id

        status: str = self.status

        type_: str = self.type_

        category_color: None | str | Unset
        if isinstance(self.category_color, Unset):
            category_color = UNSET
        else:
            category_color = self.category_color

        category_emoji: None | str | Unset
        if isinstance(self.category_emoji, Unset):
            category_emoji = UNSET
        else:
            category_emoji = self.category_emoji

        category_icon: None | str | Unset
        if isinstance(self.category_icon, Unset):
            category_icon = UNSET
        else:
            category_icon = self.category_icon

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        category_name: None | str | Unset
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        display: dict[str, Any] | None | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        elif isinstance(self.display, OccurrenceDisplay):
            display = self.display.to_dict()
        else:
            display = self.display

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

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        transaction_id: None | str | Unset
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        else:
            transaction_id = self.transaction_id

        wait_until: None | str | Unset
        if isinstance(self.wait_until, Unset):
            wait_until = UNSET
        elif isinstance(self.wait_until, datetime.date):
            wait_until = self.wait_until.isoformat()
        else:
            wait_until = self.wait_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "account_name": account_name,
                "amount": amount,
                "currency_code": currency_code,
                "date": date,
                "description": description,
                "direction": direction,
                "frequency": frequency,
                "is_due": is_due,
                "mode": mode,
                "rule_id": rule_id,
                "status": status,
                "type": type_,
            }
        )
        if category_color is not UNSET:
            field_dict["category_color"] = category_color
        if category_emoji is not UNSET:
            field_dict["category_emoji"] = category_emoji
        if category_icon is not UNSET:
            field_dict["category_icon"] = category_icon
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if display is not UNSET:
            field_dict["display"] = display
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if merchant_brand is not UNSET:
            field_dict["merchant_brand"] = merchant_brand
        if note is not UNSET:
            field_dict["note"] = note
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if wait_until is not UNSET:
            field_dict["wait_until"] = wait_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand_response import BrandResponse  # noqa: PLC0415
        from ..models.occurrence_display import OccurrenceDisplay  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        account_name = d.pop("account_name")

        amount = decimal_in(d.pop("amount"))

        currency_code = d.pop("currency_code")

        date = datetime.date.fromisoformat(d.pop("date"))

        description = d.pop("description")

        direction = check_transactions_transaction_direction(d.pop("direction"))

        frequency = check_frequency(d.pop("frequency"))

        is_due = d.pop("is_due")

        mode = check_mode(d.pop("mode"))

        rule_id = d.pop("rule_id")

        status = check_occurrence_status(d.pop("status"))

        type_ = check_transactions_transaction_type(d.pop("type"))

        def _parse_category_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_color = _parse_category_color(d.pop("category_color", UNSET))

        def _parse_category_emoji(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_emoji = _parse_category_emoji(d.pop("category_emoji", UNSET))

        def _parse_category_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_icon = _parse_category_icon(d.pop("category_icon", UNSET))

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        def _parse_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_name = _parse_category_name(d.pop("category_name", UNSET))

        def _parse_display(data: object) -> None | OccurrenceDisplay | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_type_0 = OccurrenceDisplay.from_dict(data)

                return display_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OccurrenceDisplay | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

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

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transaction_id = _parse_transaction_id(d.pop("transaction_id", UNSET))

        def _parse_wait_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wait_until_type_0 = datetime.date.fromisoformat(data)

                return wait_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        wait_until = _parse_wait_until(d.pop("wait_until", UNSET))

        occurrence_response = cls(
            account_id=account_id,
            account_name=account_name,
            amount=amount,
            currency_code=currency_code,
            date=date,
            description=description,
            direction=direction,
            frequency=frequency,
            is_due=is_due,
            mode=mode,
            rule_id=rule_id,
            status=status,
            type_=type_,
            category_color=category_color,
            category_emoji=category_emoji,
            category_icon=category_icon,
            category_id=category_id,
            category_name=category_name,
            display=display,
            merchant=merchant,
            merchant_brand=merchant_brand,
            note=note,
            project_id=project_id,
            transaction_id=transaction_id,
            wait_until=wait_until,
        )

        occurrence_response.additional_properties = d
        return occurrence_response

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
