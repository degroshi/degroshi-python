from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_transaction_request_place_source import check_create_transaction_request_place_source
from ..models.create_transaction_request_place_source import CreateTransactionRequestPlaceSource
from ..models.transaction_status import check_transaction_status
from ..models.transaction_status import TransactionStatus
from ..models.transactions_transaction_type import check_transactions_transaction_type
from ..models.transactions_transaction_type import TransactionsTransactionType
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.create_place_request import CreatePlaceRequest
    from ..models.create_transaction_request_provider_data import CreateTransactionRequestProviderData
    from ..models.recurring_occurrence_ref import RecurringOccurrenceRef


T = TypeVar("T", bound="CreateTransactionRequest")


@_attrs_define
class CreateTransactionRequest:
    """
    Attributes:
        account_id (str):
        amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        transaction_date (datetime.datetime):
        type_ (TransactionsTransactionType):
        category_id (str | Unset):
        description (str | Unset):
        exchange_rate (Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        external_source (str | Unset):
        id (str | Unset): An optional id you make up (any UUID), so a retried request doesn't create the row twice: the
            same id answers 200 with the stored row and the header Idempotent-Replayed: true.
        merchant (str | Unset):
        merchant_brand_id (str | Unset): Used by the Degroshi apps; leave it out.
        note (str | Unset):
        original_amount (Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON
            number.
        original_currency (str | Unset):
        place (CreatePlaceRequest | Unset):
        place_id (str | Unset): A place of the space, or Place a choice to store with the row in the same database
            transaction. `place_source` says how the row got it: device, picked, receipt, merchant (approximate) or ai.
            Ignored while places are off (feature_flags.places).
        place_source (CreateTransactionRequestPlaceSource | Unset):
        portfolio_activity_id (str | Unset): Used by the Degroshi apps; leave it out.
        post_date (datetime.datetime | Unset):
        project_id (str | Unset): A project of the business space; 422 TXN_PROJECT_INVALID otherwise.
        provider_data (CreateTransactionRequestProviderData | Unset):
        provider_ref (str | Unset):
        provider_type (str | Unset):
        recurring_occurrence (RecurringOccurrenceRef | Unset):
        status (TransactionStatus | Unset):
        tag_ids (list[str] | Unset): Tags of the space to put on the row.
    """

    account_id: str
    amount: Decimal
    transaction_date: datetime.datetime
    type_: TransactionsTransactionType
    category_id: str | Unset = UNSET
    description: str | Unset = UNSET
    exchange_rate: Decimal | Unset = UNSET
    external_source: str | Unset = UNSET
    id: str | Unset = UNSET
    merchant: str | Unset = UNSET
    merchant_brand_id: str | Unset = UNSET
    note: str | Unset = UNSET
    original_amount: Decimal | Unset = UNSET
    original_currency: str | Unset = UNSET
    place: CreatePlaceRequest | Unset = UNSET
    place_id: str | Unset = UNSET
    place_source: CreateTransactionRequestPlaceSource | Unset = UNSET
    portfolio_activity_id: str | Unset = UNSET
    post_date: datetime.datetime | Unset = UNSET
    project_id: str | Unset = UNSET
    provider_data: CreateTransactionRequestProviderData | Unset = UNSET
    provider_ref: str | Unset = UNSET
    provider_type: str | Unset = UNSET
    recurring_occurrence: RecurringOccurrenceRef | Unset = UNSET
    status: TransactionStatus | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_place_request import CreatePlaceRequest  # noqa: PLC0415
        from ..models.create_transaction_request_provider_data import CreateTransactionRequestProviderData  # noqa: PLC0415
        from ..models.recurring_occurrence_ref import RecurringOccurrenceRef  # noqa: PLC0415

        account_id = self.account_id

        amount = decimal_out(self.amount)

        transaction_date = self.transaction_date.isoformat()

        type_: str = self.type_

        category_id = self.category_id

        description = self.description

        exchange_rate = decimal_out(self.exchange_rate)

        external_source = self.external_source

        id = self.id

        merchant = self.merchant

        merchant_brand_id = self.merchant_brand_id

        note = self.note

        original_amount = decimal_out(self.original_amount)

        original_currency = self.original_currency

        place: dict[str, Any] | Unset = UNSET
        if not isinstance(self.place, Unset):
            place = self.place.to_dict()

        place_id = self.place_id

        place_source: str | Unset = UNSET
        if not isinstance(self.place_source, Unset):
            place_source = self.place_source

        portfolio_activity_id = self.portfolio_activity_id

        post_date: str | Unset = UNSET
        if not isinstance(self.post_date, Unset):
            post_date = self.post_date.isoformat()

        project_id = self.project_id

        provider_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_data, Unset):
            provider_data = self.provider_data.to_dict()

        provider_ref = self.provider_ref

        provider_type = self.provider_type

        recurring_occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurring_occurrence, Unset):
            recurring_occurrence = self.recurring_occurrence.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "amount": amount,
                "transaction_date": transaction_date,
                "type": type_,
            }
        )
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if description is not UNSET:
            field_dict["description"] = description
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if external_source is not UNSET:
            field_dict["external_source"] = external_source
        if id is not UNSET:
            field_dict["id"] = id
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if merchant_brand_id is not UNSET:
            field_dict["merchant_brand_id"] = merchant_brand_id
        if note is not UNSET:
            field_dict["note"] = note
        if original_amount is not UNSET:
            field_dict["original_amount"] = original_amount
        if original_currency is not UNSET:
            field_dict["original_currency"] = original_currency
        if place is not UNSET:
            field_dict["place"] = place
        if place_id is not UNSET:
            field_dict["place_id"] = place_id
        if place_source is not UNSET:
            field_dict["place_source"] = place_source
        if portfolio_activity_id is not UNSET:
            field_dict["portfolio_activity_id"] = portfolio_activity_id
        if post_date is not UNSET:
            field_dict["post_date"] = post_date
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if provider_data is not UNSET:
            field_dict["provider_data"] = provider_data
        if provider_ref is not UNSET:
            field_dict["provider_ref"] = provider_ref
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if recurring_occurrence is not UNSET:
            field_dict["recurring_occurrence"] = recurring_occurrence
        if status is not UNSET:
            field_dict["status"] = status
        if tag_ids is not UNSET:
            field_dict["tag_ids"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_place_request import CreatePlaceRequest  # noqa: PLC0415
        from ..models.create_transaction_request_provider_data import CreateTransactionRequestProviderData  # noqa: PLC0415
        from ..models.recurring_occurrence_ref import RecurringOccurrenceRef  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        amount = decimal_in(d.pop("amount"))

        transaction_date = datetime.datetime.fromisoformat(d.pop("transaction_date"))

        type_ = check_transactions_transaction_type(d.pop("type"))

        category_id = d.pop("category_id", UNSET)

        description = d.pop("description", UNSET)

        exchange_rate = decimal_in(d.pop("exchange_rate", UNSET))

        external_source = d.pop("external_source", UNSET)

        id = d.pop("id", UNSET)

        merchant = d.pop("merchant", UNSET)

        merchant_brand_id = d.pop("merchant_brand_id", UNSET)

        note = d.pop("note", UNSET)

        original_amount = decimal_in(d.pop("original_amount", UNSET))

        original_currency = d.pop("original_currency", UNSET)

        _place = d.pop("place", UNSET)
        place: CreatePlaceRequest | Unset
        if isinstance(_place, Unset):
            place = UNSET
        else:
            place = CreatePlaceRequest.from_dict(_place)

        place_id = d.pop("place_id", UNSET)

        _place_source = d.pop("place_source", UNSET)
        place_source: CreateTransactionRequestPlaceSource | Unset
        if isinstance(_place_source, Unset):
            place_source = UNSET
        else:
            place_source = check_create_transaction_request_place_source(_place_source)

        portfolio_activity_id = d.pop("portfolio_activity_id", UNSET)

        _post_date = d.pop("post_date", UNSET)
        post_date: datetime.datetime | Unset
        if isinstance(_post_date, Unset):
            post_date = UNSET
        else:
            post_date = datetime.datetime.fromisoformat(_post_date)

        project_id = d.pop("project_id", UNSET)

        _provider_data = d.pop("provider_data", UNSET)
        provider_data: CreateTransactionRequestProviderData | Unset
        if isinstance(_provider_data, Unset):
            provider_data = UNSET
        else:
            provider_data = CreateTransactionRequestProviderData.from_dict(_provider_data)

        provider_ref = d.pop("provider_ref", UNSET)

        provider_type = d.pop("provider_type", UNSET)

        _recurring_occurrence = d.pop("recurring_occurrence", UNSET)
        recurring_occurrence: RecurringOccurrenceRef | Unset
        if isinstance(_recurring_occurrence, Unset):
            recurring_occurrence = UNSET
        else:
            recurring_occurrence = RecurringOccurrenceRef.from_dict(_recurring_occurrence)

        _status = d.pop("status", UNSET)
        status: TransactionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_transaction_status(_status)

        tag_ids = cast(list[str], d.pop("tag_ids", UNSET))

        create_transaction_request = cls(
            account_id=account_id,
            amount=amount,
            transaction_date=transaction_date,
            type_=type_,
            category_id=category_id,
            description=description,
            exchange_rate=exchange_rate,
            external_source=external_source,
            id=id,
            merchant=merchant,
            merchant_brand_id=merchant_brand_id,
            note=note,
            original_amount=original_amount,
            original_currency=original_currency,
            place=place,
            place_id=place_id,
            place_source=place_source,
            portfolio_activity_id=portfolio_activity_id,
            post_date=post_date,
            project_id=project_id,
            provider_data=provider_data,
            provider_ref=provider_ref,
            provider_type=provider_type,
            recurring_occurrence=recurring_occurrence,
            status=status,
            tag_ids=tag_ids,
        )

        create_transaction_request.additional_properties = d
        return create_transaction_request

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
