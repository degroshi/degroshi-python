from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.transaction_status import check_transaction_status
from ..models.transaction_status import TransactionStatus
from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="UpdateTransactionRequest")


@_attrs_define
class UpdateTransactionRequest:
    """
    Attributes:
        account_id (None | str | Unset): Moves a plain income or expense to another open, manual account of the space in
            the same currency; its balance effect moves with it (422 TXN_ACCOUNT_CURRENCY_MISMATCH for another currency,
            TXN_ACCOUNT_CHANGE_NOT_ALLOWED for transfer legs, transfer fees and splits, TXN_ACCOUNT_NOT_MANUAL for bank-
            synced accounts).
        amount (None | Decimal | Unset): The edited row's amount; on a transfer with to_amount or fee_amount it is the total
            that leaves the source account, fee included (see ToAmount).
        category_id (None | str | Unset): Sets the category (a category of the space); null clears it.
        description (None | str | Unset): Description and Merchant: a change (ignoring surrounding whitespace) unlinks
            the merchant brand, which is looked up again; an unchanged echo keeps it.
        exchange_rate (None | Decimal | Unset): Replaces the stored exchange rate; balances don't change. Positive (400
            TXN_061); refused on transfer legs, whose rate follows their two amounts (422 TXN_011).
        fee_amount (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON
            number.
        fee_category_id (None | str | Unset): The category of a fee this edit creates (default: the space's Bank Fees
            category); an existing fee keeps its category.
        fee_id (None | str | Unset): The client id of the fee expense when this edit creates one (ignored when the
            transfer already has a fee).
        merchant (None | str | Unset): Merchant: null clears it, as "" empties it.
        merchant_brand_id (None | str | Unset): Used by the Degroshi apps; leave it out.
        not_income (bool | None | Unset): Marks an income row as the person's own money coming in (true, «Не дохід»: out
            of income, budgets and recaps, still in the balance) or counts it as income again (false). Only an income row
            that isn't a transfer leg takes true (422 VAL_001 otherwise).
        note (None | str | Unset): Note: null clears it, as "" empties it.
        original_amount (None | Decimal | Unset): And OriginalCurrency record what a plain income or expense was paid in
            another currency (a card purchase abroad): original_currency sets or changes the currency (the account's own
            currency or "" clears both), original_amount the paid amount (default: the current paid amount, else the current
            amount). Without amount the charged amount is recomputed from the paid amount at the current exchange rate (422
            TXN_063 when there is none); with amount it is kept as the bank's own figure. exchange_rate follows the two
            amounts. Values equal to the stored ones (amounts by value, the currency ignoring case) are echoes and change
            nothing: no re-conversion. null on either clears the paid amount, its currency and the rate like
            original_currency "", unless the other one sends a new value, which wins. Transfer legs and fees, splits and
            connected accounts' rows are refused (422 TXN_011 / TXN_ACCOUNT_CONNECTED).
        original_currency (None | str | Unset): "" passes binding (the clear sentinel); any other value must be an ISO
            4217 code (400 VAL_001, checked by the service).
        status (TransactionStatus | Unset):
        tag_ids (list[str] | None | Unset): Replaces the transaction's tags (tags of the space, at most 20); [] removes
            them all, absent keeps them. On a transfer it applies to the edited leg.
        to_amount (None | Decimal | Unset): And FeeAmount edit the amounts of a transfer (either leg's id): with either of
            them the request reads like a transfer create — amount is the total that leaves the source account (fee
            included, default: the current one), to_amount what arrives, fee_amount the fee in the source currency (0
            removes it). Absent fields keep their current value; a same-currency to_amount below amount books the difference
            as the fee. The fee expense is created, changed or removed to match. Rejected on transactions that are not
            transfer legs. Without either of them amount is the edited leg's own amount.
        transaction_date (datetime.datetime | None | Unset):
    """

    account_id: None | str | Unset = UNSET
    amount: None | Decimal | Unset = UNSET
    category_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    exchange_rate: None | Decimal | Unset = UNSET
    fee_amount: None | Decimal | Unset = UNSET
    fee_category_id: None | str | Unset = UNSET
    fee_id: None | str | Unset = UNSET
    merchant: None | str | Unset = UNSET
    merchant_brand_id: None | str | Unset = UNSET
    not_income: bool | None | Unset = UNSET
    note: None | str | Unset = UNSET
    original_amount: None | Decimal | Unset = UNSET
    original_currency: None | str | Unset = UNSET
    status: TransactionStatus | Unset = UNSET
    tag_ids: list[str] | None | Unset = UNSET
    to_amount: None | Decimal | Unset = UNSET
    transaction_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        amount: None | Decimal | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = decimal_out(self.amount)

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        exchange_rate: None | Decimal | Unset
        if isinstance(self.exchange_rate, Unset):
            exchange_rate = UNSET
        else:
            exchange_rate = decimal_out(self.exchange_rate)

        fee_amount: None | Decimal | Unset
        if isinstance(self.fee_amount, Unset):
            fee_amount = UNSET
        else:
            fee_amount = decimal_out(self.fee_amount)

        fee_category_id: None | str | Unset
        if isinstance(self.fee_category_id, Unset):
            fee_category_id = UNSET
        else:
            fee_category_id = self.fee_category_id

        fee_id: None | str | Unset
        if isinstance(self.fee_id, Unset):
            fee_id = UNSET
        else:
            fee_id = self.fee_id

        merchant: None | str | Unset
        if isinstance(self.merchant, Unset):
            merchant = UNSET
        else:
            merchant = self.merchant

        merchant_brand_id: None | str | Unset
        if isinstance(self.merchant_brand_id, Unset):
            merchant_brand_id = UNSET
        else:
            merchant_brand_id = self.merchant_brand_id

        not_income: bool | None | Unset
        if isinstance(self.not_income, Unset):
            not_income = UNSET
        else:
            not_income = self.not_income

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        original_amount: None | Decimal | Unset
        if isinstance(self.original_amount, Unset):
            original_amount = UNSET
        else:
            original_amount = decimal_out(self.original_amount)

        original_currency: None | str | Unset
        if isinstance(self.original_currency, Unset):
            original_currency = UNSET
        else:
            original_currency = self.original_currency

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        tag_ids: list[str] | None | Unset
        if isinstance(self.tag_ids, Unset):
            tag_ids = UNSET
        elif isinstance(self.tag_ids, list):
            tag_ids = self.tag_ids

        else:
            tag_ids = self.tag_ids

        to_amount: None | Decimal | Unset
        if isinstance(self.to_amount, Unset):
            to_amount = UNSET
        else:
            to_amount = decimal_out(self.to_amount)

        transaction_date: None | str | Unset
        if isinstance(self.transaction_date, Unset):
            transaction_date = UNSET
        elif isinstance(self.transaction_date, datetime.datetime):
            transaction_date = self.transaction_date.isoformat()
        else:
            transaction_date = self.transaction_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if description is not UNSET:
            field_dict["description"] = description
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if fee_amount is not UNSET:
            field_dict["fee_amount"] = fee_amount
        if fee_category_id is not UNSET:
            field_dict["fee_category_id"] = fee_category_id
        if fee_id is not UNSET:
            field_dict["fee_id"] = fee_id
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if merchant_brand_id is not UNSET:
            field_dict["merchant_brand_id"] = merchant_brand_id
        if not_income is not UNSET:
            field_dict["not_income"] = not_income
        if note is not UNSET:
            field_dict["note"] = note
        if original_amount is not UNSET:
            field_dict["original_amount"] = original_amount
        if original_currency is not UNSET:
            field_dict["original_currency"] = original_currency
        if status is not UNSET:
            field_dict["status"] = status
        if tag_ids is not UNSET:
            field_dict["tag_ids"] = tag_ids
        if to_amount is not UNSET:
            field_dict["to_amount"] = to_amount
        if transaction_date is not UNSET:
            field_dict["transaction_date"] = transaction_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = decimal_in(_parse_amount(d.pop("amount", UNSET)))

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_exchange_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_rate = decimal_in(_parse_exchange_rate(d.pop("exchange_rate", UNSET)))

        def _parse_fee_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fee_amount = decimal_in(_parse_fee_amount(d.pop("fee_amount", UNSET)))

        def _parse_fee_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fee_category_id = _parse_fee_category_id(d.pop("fee_category_id", UNSET))

        def _parse_fee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fee_id = _parse_fee_id(d.pop("fee_id", UNSET))

        def _parse_merchant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        merchant = _parse_merchant(d.pop("merchant", UNSET))

        def _parse_merchant_brand_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        merchant_brand_id = _parse_merchant_brand_id(d.pop("merchant_brand_id", UNSET))

        def _parse_not_income(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        not_income = _parse_not_income(d.pop("not_income", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_original_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_amount = decimal_in(_parse_original_amount(d.pop("original_amount", UNSET)))

        def _parse_original_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_currency = _parse_original_currency(d.pop("original_currency", UNSET))

        _status = d.pop("status", UNSET)
        status: TransactionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_transaction_status(_status)

        def _parse_tag_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tag_ids_type_0 = cast(list[str], data)

                return tag_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tag_ids = _parse_tag_ids(d.pop("tag_ids", UNSET))

        def _parse_to_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_amount = decimal_in(_parse_to_amount(d.pop("to_amount", UNSET)))

        def _parse_transaction_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transaction_date_type_0 = datetime.datetime.fromisoformat(data)

                return transaction_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        transaction_date = _parse_transaction_date(d.pop("transaction_date", UNSET))

        update_transaction_request = cls(
            account_id=account_id,
            amount=amount,
            category_id=category_id,
            description=description,
            exchange_rate=exchange_rate,
            fee_amount=fee_amount,
            fee_category_id=fee_category_id,
            fee_id=fee_id,
            merchant=merchant,
            merchant_brand_id=merchant_brand_id,
            not_income=not_income,
            note=note,
            original_amount=original_amount,
            original_currency=original_currency,
            status=status,
            tag_ids=tag_ids,
            to_amount=to_amount,
            transaction_date=transaction_date,
        )

        update_transaction_request.additional_properties = d
        return update_transaction_request

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
