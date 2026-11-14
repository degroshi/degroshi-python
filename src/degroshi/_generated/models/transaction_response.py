from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.transaction_response_kind_type_0 import check_transaction_response_kind_type_0
from ..models.transaction_response_kind_type_0 import TransactionResponseKindType0
from ..models.transaction_response_place_source_type_0 import check_transaction_response_place_source_type_0
from ..models.transaction_response_place_source_type_0 import TransactionResponsePlaceSourceType0
from ..models.transaction_response_uah_status_type_0 import check_transaction_response_uah_status_type_0
from ..models.transaction_response_uah_status_type_0 import TransactionResponseUahStatusType0
from ..models.transaction_status import check_transaction_status
from ..models.transaction_status import TransactionStatus
from ..models.transactions_transaction_direction import check_transactions_transaction_direction
from ..models.transactions_transaction_direction import TransactionsTransactionDirection
from ..models.transactions_transaction_type import check_transactions_transaction_type
from ..models.transactions_transaction_type import TransactionsTransactionType
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.brand_response import BrandResponse
    from ..models.category_review import CategoryReview
    from ..models.linked_activity_response import LinkedActivityResponse
    from ..models.reactions_summary import ReactionsSummary
    from ..models.transaction_external_data_response import TransactionExternalDataResponse
    from ..models.transaction_financials_response import TransactionFinancialsResponse
    from ..models.transaction_metadata_response import TransactionMetadataResponse
    from ..models.transaction_place import TransactionPlace
    from ..models.transaction_relationships_response import TransactionRelationshipsResponse
    from ..models.transaction_tag import TransactionTag
    from ..models.transaction_timestamps_response import TransactionTimestampsResponse
    from ..models.transaction_treatment import TransactionTreatment
    from ..models.transfer_response import TransferResponse


T = TypeVar("T", bound="TransactionResponse")


@_attrs_define
class TransactionResponse:
    """
    Attributes:
        account_id (str):
        account_name (str):
        amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        created_at (datetime.datetime):
        description (str):
        direction (TransactionsTransactionDirection):
        external_data (TransactionExternalDataResponse):
        financials (TransactionFinancialsResponse):
        id (str):
        is_deleted (bool):
        is_split (bool):
        metadata (TransactionMetadataResponse):
        relationships (TransactionRelationshipsResponse):
        space_id (str):
        status (TransactionStatus):
        timestamps (TransactionTimestampsResponse):
        transaction_date (datetime.datetime):
        type_ (TransactionsTransactionType):
        updated_at (datetime.datetime):
        category_color (None | str | Unset):
        category_emoji (None | str | Unset): The category's emoji (native clients' icon set).
        category_icon (None | str | Unset): The category's icon, a slug from the category icon set.
        category_id (None | str | Unset):
        category_is_transfer (bool | None | Unset): The category is a transfer category (“Transfers” and its children,
            or a custom one of type transfer), so the row counts as neither income nor spending, linked or not. Absent when
            false.
        category_name (None | str | Unset): The category's display name in the request language: built-in categories
            that keep their seed name are translated ("Groceries" in English), custom and renamed ones are as stored.
        category_review (CategoryReview | None | Unset): How the background categorizer chose the row's category, when
            it did. Its needs_review is deprecated and always false.
        counterpart_account_id (None | str | Unset): `counterpart_account_id` and `counterpart_account_name` are the
            account of the other leg of a transfer ("Wise → PrivatBank"); omitted otherwise.
        counterpart_account_name (None | str | Unset):
        counterpart_hidden (bool | None | Unset): `counterpart_hidden` marks a transfer leg whose other side is on an
            account the caller can't see: clients show "Other account", and linked_transfer_id, counterpart_account_* and
            fee_transaction_id (when the fee is on that account) are omitted. direction stays transfer_in/transfer_out. Also
            true on a leg of a cross-space transfer: its other leg lives in another space (counterpart_space).
        counterpart_space (None | str | Unset): `counterpart_space` names the other leg's space of a cross-space
            transfer: its name, or "Other space" (in the request language) when the caller is not a member of it or can't
            see its account (counterpart_space_hidden). counterpart_space_id, counterpart_account_* and
            counterpart_transaction_id are set only when the caller can see it.
        counterpart_space_hidden (bool | None | Unset):
        counterpart_space_id (None | str | Unset):
        counterpart_transaction_id (None | str | Unset): The other leg of a cross-space transfer, in
            counterpart_space_id: switch to that space (X-Space-ID) to open it. Set only when the caller is a member there
            and can see its account.
        counterparty_id (None | str | Unset): The business counterparty the row is linked to; omitted when it has none.
        counts_as_income (bool | None | Unset): `counts_as_income` marks the personal leg of a cross-space transfer
            between a business and its owner's personal space: still a transfer, with the business's subcategory under
            “Income”, and counted in this space's income: an incoming leg adds its amount, an outgoing one (a top-up of the
            business) subtracts it; never in spending.
        created_by (None | str | Unset): The user id of the space member who added the row: a manual entry, transfer,
            split part, statement import, Suricate action or recurring posting. Omitted for bank, wallet and exchange
            imports and for rows whose author was never recorded.
        created_by_name (None | str | Unset): The author's first name (else the local part of their email), also for
            members who have left the space; omitted with created_by.
        cross_space_transfer_id (None | str | Unset): `cross_space_transfer_id` marks a leg of a cross-space transfer
            (money moved between two linked spaces of the same owner, e.g. a personal card and a sole proprietor's account):
            both legs carry it.
        exchange_rate (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON
            number.
        fee_for_transfer_id (None | str | Unset): `fee_for_transfer_id` marks a transfer fee: the id of the transfer's
            outgoing leg (the transfer's id). Omitted for other transactions.
        fee_transaction_id (None | str | Unset): The fee expense booked with this transfer (on the source account), on
            both legs; omitted when the transfer has no fee.
        kind (None | TransactionResponseKindType0 | Unset): "portfolio_transfer" for a transfer between two of the
            space's portfolio accounts (include_portfolio_transfers): its other fields are a list row's,
            `portfolio_transfer` carries the transfer, and it is read-only. Absent on a transaction.
        linked_activity (LinkedActivityResponse | None | Unset): The wallet or exchange activity it was recorded from:
            network, hash with its explorer link, what moved and the fee. Omitted when it wasn't recorded from one the
            caller can see.
        linked_transfer_id (None | str | Unset):
        merchant (None | str | Unset):
        merchant_brand (BrandResponse | None | Unset):
        not_income (bool | None | Unset): `not_income` marks money coming in that is the person's own: left out of
            income, budgets and recaps, still in the account's balance. Omitted when false.
        note (None | str | Unset):
        original_amount (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON
            number.
        original_currency (None | str | Unset):
        parent_id (None | str | Unset):
        place (None | TransactionPlace | Unset):
        place_id (None | str | Unset): `place_id`, `place_source` and Place are where the row happened: the place in the
            requester's language, as they may see it (another member's pin is its city); is_approximate for a place derived
            from a bank or CSV row. Omitted when none.
        place_source (None | TransactionResponsePlaceSourceType0 | Unset):
        portfolio_transfer (None | TransferResponse | Unset): The transfer of a row of kind "portfolio_transfer".
        project_id (None | str | Unset): The business project of the row or split part; omitted when it has none.
        reactions (None | ReactionsSummary | Unset): The badge of its reactions and comments in a shared space; omitted
            when it has neither.
        read_only (bool | None | Unset): `read_only` marks a row nothing may edit, delete or record (a portfolio
            transfer).
        recurring_rule_id (None | str | Unset): The recurring rule whose occurrence this row settles; omitted when none.
        service_period_from (datetime.date | None | Unset): `service_period_from` and `service_period_to` are the period
            a business operation pays for: the accrual P&L spreads it over these days.
        service_period_to (datetime.date | None | Unset):
        splits (list[TransactionResponse] | None | Unset):
        tags (list[TransactionTag] | None | Unset): The transaction's tags, by name; omitted when it has none.
        treatment (None | TransactionTreatment | Unset): The tax treatment of a business-space row (its class, who
            decided it, how sure and whether a person reviewed it); omitted in personal spaces and for rows without one (a
            split parent, a cancelled row, a row the worker has not reached yet).
        uah_amount (None | Decimal | Unset): UAHAmount is the legal hryvnia value of a business-space row: the amount at the
            official NBU rate of the account currency on the legal date (uah_rate_date, the Kyiv calendar day of
            transaction_date), rounded to kopecks and frozen; the amount itself on a UAH account. Omitted in personal spaces
            and while uah_status is pending_rate.
        uah_rate (None | Decimal | Unset): UAHRate is hryvnias per one unit of the account currency used for uah_amount (1
            on a UAH account).
        uah_rate_date (datetime.date | None | Unset): UAHRateDate is the legal date of the valuation.
        uah_status (None | TransactionResponseUahStatusType0 | Unset): UAHStatus is the valuation state of a business-
            space row: ok, pending_rate (no value yet: just written, or the NBU has not published the rate of that day;
            reports leave the row out and count it in pending_valuation) or locked (a declared or locked period, never
            recomputed). Omitted in personal spaces.
        version (int | None | Unset): The row version (also the ETag): send it back as If-Match on PATCH and DELETE to
            detect concurrent edits (412).
    """

    account_id: str
    account_name: str
    amount: Decimal
    created_at: datetime.datetime
    description: str
    direction: TransactionsTransactionDirection
    external_data: TransactionExternalDataResponse
    financials: TransactionFinancialsResponse
    id: str
    is_deleted: bool
    is_split: bool
    metadata: TransactionMetadataResponse
    relationships: TransactionRelationshipsResponse
    space_id: str
    status: TransactionStatus
    timestamps: TransactionTimestampsResponse
    transaction_date: datetime.datetime
    type_: TransactionsTransactionType
    updated_at: datetime.datetime
    category_color: None | str | Unset = UNSET
    category_emoji: None | str | Unset = UNSET
    category_icon: None | str | Unset = UNSET
    category_id: None | str | Unset = UNSET
    category_is_transfer: bool | None | Unset = UNSET
    category_name: None | str | Unset = UNSET
    category_review: CategoryReview | None | Unset = UNSET
    counterpart_account_id: None | str | Unset = UNSET
    counterpart_account_name: None | str | Unset = UNSET
    counterpart_hidden: bool | None | Unset = UNSET
    counterpart_space: None | str | Unset = UNSET
    counterpart_space_hidden: bool | None | Unset = UNSET
    counterpart_space_id: None | str | Unset = UNSET
    counterpart_transaction_id: None | str | Unset = UNSET
    counterparty_id: None | str | Unset = UNSET
    counts_as_income: bool | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    created_by_name: None | str | Unset = UNSET
    cross_space_transfer_id: None | str | Unset = UNSET
    exchange_rate: None | Decimal | Unset = UNSET
    fee_for_transfer_id: None | str | Unset = UNSET
    fee_transaction_id: None | str | Unset = UNSET
    kind: None | TransactionResponseKindType0 | Unset = UNSET
    linked_activity: LinkedActivityResponse | None | Unset = UNSET
    linked_transfer_id: None | str | Unset = UNSET
    merchant: None | str | Unset = UNSET
    merchant_brand: BrandResponse | None | Unset = UNSET
    not_income: bool | None | Unset = UNSET
    note: None | str | Unset = UNSET
    original_amount: None | Decimal | Unset = UNSET
    original_currency: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    place: None | TransactionPlace | Unset = UNSET
    place_id: None | str | Unset = UNSET
    place_source: None | TransactionResponsePlaceSourceType0 | Unset = UNSET
    portfolio_transfer: None | TransferResponse | Unset = UNSET
    project_id: None | str | Unset = UNSET
    reactions: None | ReactionsSummary | Unset = UNSET
    read_only: bool | None | Unset = UNSET
    recurring_rule_id: None | str | Unset = UNSET
    service_period_from: datetime.date | None | Unset = UNSET
    service_period_to: datetime.date | None | Unset = UNSET
    splits: list[TransactionResponse] | None | Unset = UNSET
    tags: list[TransactionTag] | None | Unset = UNSET
    treatment: None | TransactionTreatment | Unset = UNSET
    uah_amount: None | Decimal | Unset = UNSET
    uah_rate: None | Decimal | Unset = UNSET
    uah_rate_date: datetime.date | None | Unset = UNSET
    uah_status: None | TransactionResponseUahStatusType0 | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brand_response import BrandResponse  # noqa: PLC0415
        from ..models.category_review import CategoryReview  # noqa: PLC0415
        from ..models.linked_activity_response import LinkedActivityResponse  # noqa: PLC0415
        from ..models.reactions_summary import ReactionsSummary  # noqa: PLC0415
        from ..models.transaction_external_data_response import TransactionExternalDataResponse  # noqa: PLC0415
        from ..models.transaction_financials_response import TransactionFinancialsResponse  # noqa: PLC0415
        from ..models.transaction_metadata_response import TransactionMetadataResponse  # noqa: PLC0415
        from ..models.transaction_place import TransactionPlace  # noqa: PLC0415
        from ..models.transaction_relationships_response import TransactionRelationshipsResponse  # noqa: PLC0415
        from ..models.transaction_tag import TransactionTag  # noqa: PLC0415
        from ..models.transaction_timestamps_response import TransactionTimestampsResponse  # noqa: PLC0415
        from ..models.transaction_treatment import TransactionTreatment  # noqa: PLC0415
        from ..models.transfer_response import TransferResponse  # noqa: PLC0415

        account_id = self.account_id

        account_name = self.account_name

        amount = decimal_out(self.amount)

        created_at = self.created_at.isoformat()

        description = self.description

        direction: str = self.direction

        external_data = self.external_data.to_dict()

        financials = self.financials.to_dict()

        id = self.id

        is_deleted = self.is_deleted

        is_split = self.is_split

        metadata = self.metadata.to_dict()

        relationships = self.relationships.to_dict()

        space_id = self.space_id

        status: str = self.status

        timestamps = self.timestamps.to_dict()

        transaction_date = self.transaction_date.isoformat()

        type_: str = self.type_

        updated_at = self.updated_at.isoformat()

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

        category_is_transfer: bool | None | Unset
        if isinstance(self.category_is_transfer, Unset):
            category_is_transfer = UNSET
        else:
            category_is_transfer = self.category_is_transfer

        category_name: None | str | Unset
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        category_review: dict[str, Any] | None | Unset
        if isinstance(self.category_review, Unset):
            category_review = UNSET
        elif isinstance(self.category_review, CategoryReview):
            category_review = self.category_review.to_dict()
        else:
            category_review = self.category_review

        counterpart_account_id: None | str | Unset
        if isinstance(self.counterpart_account_id, Unset):
            counterpart_account_id = UNSET
        else:
            counterpart_account_id = self.counterpart_account_id

        counterpart_account_name: None | str | Unset
        if isinstance(self.counterpart_account_name, Unset):
            counterpart_account_name = UNSET
        else:
            counterpart_account_name = self.counterpart_account_name

        counterpart_hidden: bool | None | Unset
        if isinstance(self.counterpart_hidden, Unset):
            counterpart_hidden = UNSET
        else:
            counterpart_hidden = self.counterpart_hidden

        counterpart_space: None | str | Unset
        if isinstance(self.counterpart_space, Unset):
            counterpart_space = UNSET
        else:
            counterpart_space = self.counterpart_space

        counterpart_space_hidden: bool | None | Unset
        if isinstance(self.counterpart_space_hidden, Unset):
            counterpart_space_hidden = UNSET
        else:
            counterpart_space_hidden = self.counterpart_space_hidden

        counterpart_space_id: None | str | Unset
        if isinstance(self.counterpart_space_id, Unset):
            counterpart_space_id = UNSET
        else:
            counterpart_space_id = self.counterpart_space_id

        counterpart_transaction_id: None | str | Unset
        if isinstance(self.counterpart_transaction_id, Unset):
            counterpart_transaction_id = UNSET
        else:
            counterpart_transaction_id = self.counterpart_transaction_id

        counterparty_id: None | str | Unset
        if isinstance(self.counterparty_id, Unset):
            counterparty_id = UNSET
        else:
            counterparty_id = self.counterparty_id

        counts_as_income: bool | None | Unset
        if isinstance(self.counts_as_income, Unset):
            counts_as_income = UNSET
        else:
            counts_as_income = self.counts_as_income

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

        cross_space_transfer_id: None | str | Unset
        if isinstance(self.cross_space_transfer_id, Unset):
            cross_space_transfer_id = UNSET
        else:
            cross_space_transfer_id = self.cross_space_transfer_id

        exchange_rate: None | Decimal | Unset
        if isinstance(self.exchange_rate, Unset):
            exchange_rate = UNSET
        else:
            exchange_rate = decimal_out(self.exchange_rate)

        fee_for_transfer_id: None | str | Unset
        if isinstance(self.fee_for_transfer_id, Unset):
            fee_for_transfer_id = UNSET
        else:
            fee_for_transfer_id = self.fee_for_transfer_id

        fee_transaction_id: None | str | Unset
        if isinstance(self.fee_transaction_id, Unset):
            fee_transaction_id = UNSET
        else:
            fee_transaction_id = self.fee_transaction_id

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, str):
            kind = self.kind
        else:
            kind = self.kind

        linked_activity: dict[str, Any] | None | Unset
        if isinstance(self.linked_activity, Unset):
            linked_activity = UNSET
        elif isinstance(self.linked_activity, LinkedActivityResponse):
            linked_activity = self.linked_activity.to_dict()
        else:
            linked_activity = self.linked_activity

        linked_transfer_id: None | str | Unset
        if isinstance(self.linked_transfer_id, Unset):
            linked_transfer_id = UNSET
        else:
            linked_transfer_id = self.linked_transfer_id

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

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        place: dict[str, Any] | None | Unset
        if isinstance(self.place, Unset):
            place = UNSET
        elif isinstance(self.place, TransactionPlace):
            place = self.place.to_dict()
        else:
            place = self.place

        place_id: None | str | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        place_source: None | str | Unset
        if isinstance(self.place_source, Unset):
            place_source = UNSET
        elif isinstance(self.place_source, str):
            place_source = self.place_source
        else:
            place_source = self.place_source

        portfolio_transfer: dict[str, Any] | None | Unset
        if isinstance(self.portfolio_transfer, Unset):
            portfolio_transfer = UNSET
        elif isinstance(self.portfolio_transfer, TransferResponse):
            portfolio_transfer = self.portfolio_transfer.to_dict()
        else:
            portfolio_transfer = self.portfolio_transfer

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        reactions: dict[str, Any] | None | Unset
        if isinstance(self.reactions, Unset):
            reactions = UNSET
        elif isinstance(self.reactions, ReactionsSummary):
            reactions = self.reactions.to_dict()
        else:
            reactions = self.reactions

        read_only: bool | None | Unset
        if isinstance(self.read_only, Unset):
            read_only = UNSET
        else:
            read_only = self.read_only

        recurring_rule_id: None | str | Unset
        if isinstance(self.recurring_rule_id, Unset):
            recurring_rule_id = UNSET
        else:
            recurring_rule_id = self.recurring_rule_id

        service_period_from: None | str | Unset
        if isinstance(self.service_period_from, Unset):
            service_period_from = UNSET
        elif isinstance(self.service_period_from, datetime.date):
            service_period_from = self.service_period_from.isoformat()
        else:
            service_period_from = self.service_period_from

        service_period_to: None | str | Unset
        if isinstance(self.service_period_to, Unset):
            service_period_to = UNSET
        elif isinstance(self.service_period_to, datetime.date):
            service_period_to = self.service_period_to.isoformat()
        else:
            service_period_to = self.service_period_to

        splits: list[dict[str, Any]] | None | Unset
        if isinstance(self.splits, Unset):
            splits = UNSET
        elif isinstance(self.splits, list):
            splits = []
            for splits_type_0_item_data in self.splits:
                splits_type_0_item = splits_type_0_item_data.to_dict()
                splits.append(splits_type_0_item)

        else:
            splits = self.splits

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        treatment: dict[str, Any] | None | Unset
        if isinstance(self.treatment, Unset):
            treatment = UNSET
        elif isinstance(self.treatment, TransactionTreatment):
            treatment = self.treatment.to_dict()
        else:
            treatment = self.treatment

        uah_amount: None | Decimal | Unset
        if isinstance(self.uah_amount, Unset):
            uah_amount = UNSET
        else:
            uah_amount = decimal_out(self.uah_amount)

        uah_rate: None | Decimal | Unset
        if isinstance(self.uah_rate, Unset):
            uah_rate = UNSET
        else:
            uah_rate = decimal_out(self.uah_rate)

        uah_rate_date: None | str | Unset
        if isinstance(self.uah_rate_date, Unset):
            uah_rate_date = UNSET
        elif isinstance(self.uah_rate_date, datetime.date):
            uah_rate_date = self.uah_rate_date.isoformat()
        else:
            uah_rate_date = self.uah_rate_date

        uah_status: None | str | Unset
        if isinstance(self.uah_status, Unset):
            uah_status = UNSET
        elif isinstance(self.uah_status, str):
            uah_status = self.uah_status
        else:
            uah_status = self.uah_status

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
                "account_name": account_name,
                "amount": amount,
                "created_at": created_at,
                "description": description,
                "direction": direction,
                "externalData": external_data,
                "financials": financials,
                "id": id,
                "isDeleted": is_deleted,
                "is_split": is_split,
                "metadata": metadata,
                "relationships": relationships,
                "space_id": space_id,
                "status": status,
                "timestamps": timestamps,
                "transaction_date": transaction_date,
                "type": type_,
                "updated_at": updated_at,
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
        if category_is_transfer is not UNSET:
            field_dict["category_is_transfer"] = category_is_transfer
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if category_review is not UNSET:
            field_dict["category_review"] = category_review
        if counterpart_account_id is not UNSET:
            field_dict["counterpart_account_id"] = counterpart_account_id
        if counterpart_account_name is not UNSET:
            field_dict["counterpart_account_name"] = counterpart_account_name
        if counterpart_hidden is not UNSET:
            field_dict["counterpart_hidden"] = counterpart_hidden
        if counterpart_space is not UNSET:
            field_dict["counterpart_space"] = counterpart_space
        if counterpart_space_hidden is not UNSET:
            field_dict["counterpart_space_hidden"] = counterpart_space_hidden
        if counterpart_space_id is not UNSET:
            field_dict["counterpart_space_id"] = counterpart_space_id
        if counterpart_transaction_id is not UNSET:
            field_dict["counterpart_transaction_id"] = counterpart_transaction_id
        if counterparty_id is not UNSET:
            field_dict["counterparty_id"] = counterparty_id
        if counts_as_income is not UNSET:
            field_dict["counts_as_income"] = counts_as_income
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_name is not UNSET:
            field_dict["created_by_name"] = created_by_name
        if cross_space_transfer_id is not UNSET:
            field_dict["cross_space_transfer_id"] = cross_space_transfer_id
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if fee_for_transfer_id is not UNSET:
            field_dict["fee_for_transfer_id"] = fee_for_transfer_id
        if fee_transaction_id is not UNSET:
            field_dict["fee_transaction_id"] = fee_transaction_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if linked_activity is not UNSET:
            field_dict["linked_activity"] = linked_activity
        if linked_transfer_id is not UNSET:
            field_dict["linked_transfer_id"] = linked_transfer_id
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if merchant_brand is not UNSET:
            field_dict["merchant_brand"] = merchant_brand
        if not_income is not UNSET:
            field_dict["not_income"] = not_income
        if note is not UNSET:
            field_dict["note"] = note
        if original_amount is not UNSET:
            field_dict["original_amount"] = original_amount
        if original_currency is not UNSET:
            field_dict["original_currency"] = original_currency
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if place is not UNSET:
            field_dict["place"] = place
        if place_id is not UNSET:
            field_dict["place_id"] = place_id
        if place_source is not UNSET:
            field_dict["place_source"] = place_source
        if portfolio_transfer is not UNSET:
            field_dict["portfolio_transfer"] = portfolio_transfer
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if recurring_rule_id is not UNSET:
            field_dict["recurring_rule_id"] = recurring_rule_id
        if service_period_from is not UNSET:
            field_dict["service_period_from"] = service_period_from
        if service_period_to is not UNSET:
            field_dict["service_period_to"] = service_period_to
        if splits is not UNSET:
            field_dict["splits"] = splits
        if tags is not UNSET:
            field_dict["tags"] = tags
        if treatment is not UNSET:
            field_dict["treatment"] = treatment
        if uah_amount is not UNSET:
            field_dict["uah_amount"] = uah_amount
        if uah_rate is not UNSET:
            field_dict["uah_rate"] = uah_rate
        if uah_rate_date is not UNSET:
            field_dict["uah_rate_date"] = uah_rate_date
        if uah_status is not UNSET:
            field_dict["uah_status"] = uah_status
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand_response import BrandResponse  # noqa: PLC0415
        from ..models.category_review import CategoryReview  # noqa: PLC0415
        from ..models.linked_activity_response import LinkedActivityResponse  # noqa: PLC0415
        from ..models.reactions_summary import ReactionsSummary  # noqa: PLC0415
        from ..models.transaction_external_data_response import TransactionExternalDataResponse  # noqa: PLC0415
        from ..models.transaction_financials_response import TransactionFinancialsResponse  # noqa: PLC0415
        from ..models.transaction_metadata_response import TransactionMetadataResponse  # noqa: PLC0415
        from ..models.transaction_place import TransactionPlace  # noqa: PLC0415
        from ..models.transaction_relationships_response import TransactionRelationshipsResponse  # noqa: PLC0415
        from ..models.transaction_tag import TransactionTag  # noqa: PLC0415
        from ..models.transaction_timestamps_response import TransactionTimestampsResponse  # noqa: PLC0415
        from ..models.transaction_treatment import TransactionTreatment  # noqa: PLC0415
        from ..models.transfer_response import TransferResponse  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        account_name = d.pop("account_name")

        amount = decimal_in(d.pop("amount"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        direction = check_transactions_transaction_direction(d.pop("direction"))

        external_data = TransactionExternalDataResponse.from_dict(d.pop("externalData"))

        financials = TransactionFinancialsResponse.from_dict(d.pop("financials"))

        id = d.pop("id")

        is_deleted = d.pop("isDeleted")

        is_split = d.pop("is_split")

        metadata = TransactionMetadataResponse.from_dict(d.pop("metadata"))

        relationships = TransactionRelationshipsResponse.from_dict(d.pop("relationships"))

        space_id = d.pop("space_id")

        status = check_transaction_status(d.pop("status"))

        timestamps = TransactionTimestampsResponse.from_dict(d.pop("timestamps"))

        transaction_date = datetime.datetime.fromisoformat(d.pop("transaction_date"))

        type_ = check_transactions_transaction_type(d.pop("type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_category_is_transfer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        category_is_transfer = _parse_category_is_transfer(d.pop("category_is_transfer", UNSET))

        def _parse_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_name = _parse_category_name(d.pop("category_name", UNSET))

        def _parse_category_review(data: object) -> CategoryReview | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_review_type_0 = CategoryReview.from_dict(data)

                return category_review_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CategoryReview | None | Unset, data)

        category_review = _parse_category_review(d.pop("category_review", UNSET))

        def _parse_counterpart_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counterpart_account_id = _parse_counterpart_account_id(d.pop("counterpart_account_id", UNSET))

        def _parse_counterpart_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counterpart_account_name = _parse_counterpart_account_name(d.pop("counterpart_account_name", UNSET))

        def _parse_counterpart_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        counterpart_hidden = _parse_counterpart_hidden(d.pop("counterpart_hidden", UNSET))

        def _parse_counterpart_space(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counterpart_space = _parse_counterpart_space(d.pop("counterpart_space", UNSET))

        def _parse_counterpart_space_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        counterpart_space_hidden = _parse_counterpart_space_hidden(d.pop("counterpart_space_hidden", UNSET))

        def _parse_counterpart_space_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counterpart_space_id = _parse_counterpart_space_id(d.pop("counterpart_space_id", UNSET))

        def _parse_counterpart_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counterpart_transaction_id = _parse_counterpart_transaction_id(d.pop("counterpart_transaction_id", UNSET))

        def _parse_counterparty_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counterparty_id = _parse_counterparty_id(d.pop("counterparty_id", UNSET))

        def _parse_counts_as_income(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        counts_as_income = _parse_counts_as_income(d.pop("counts_as_income", UNSET))

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

        def _parse_cross_space_transfer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cross_space_transfer_id = _parse_cross_space_transfer_id(d.pop("cross_space_transfer_id", UNSET))

        def _parse_exchange_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_rate = decimal_in(_parse_exchange_rate(d.pop("exchange_rate", UNSET)))

        def _parse_fee_for_transfer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fee_for_transfer_id = _parse_fee_for_transfer_id(d.pop("fee_for_transfer_id", UNSET))

        def _parse_fee_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fee_transaction_id = _parse_fee_transaction_id(d.pop("fee_transaction_id", UNSET))

        def _parse_kind(data: object) -> None | TransactionResponseKindType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = check_transaction_response_kind_type_0(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionResponseKindType0 | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_linked_activity(data: object) -> LinkedActivityResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linked_activity_type_0 = LinkedActivityResponse.from_dict(data)

                return linked_activity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinkedActivityResponse | None | Unset, data)

        linked_activity = _parse_linked_activity(d.pop("linked_activity", UNSET))

        def _parse_linked_transfer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_transfer_id = _parse_linked_transfer_id(d.pop("linked_transfer_id", UNSET))

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

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_place(data: object) -> None | TransactionPlace | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_type_0 = TransactionPlace.from_dict(data)

                return place_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionPlace | Unset, data)

        place = _parse_place(d.pop("place", UNSET))

        def _parse_place_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_id = _parse_place_id(d.pop("place_id", UNSET))

        def _parse_place_source(data: object) -> None | TransactionResponsePlaceSourceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                place_source_type_0 = check_transaction_response_place_source_type_0(data)

                return place_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionResponsePlaceSourceType0 | Unset, data)

        place_source = _parse_place_source(d.pop("place_source", UNSET))

        def _parse_portfolio_transfer(data: object) -> None | TransferResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                portfolio_transfer_type_0 = TransferResponse.from_dict(data)

                return portfolio_transfer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransferResponse | Unset, data)

        portfolio_transfer = _parse_portfolio_transfer(d.pop("portfolio_transfer", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_reactions(data: object) -> None | ReactionsSummary | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reactions_type_0 = ReactionsSummary.from_dict(data)

                return reactions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReactionsSummary | Unset, data)

        reactions = _parse_reactions(d.pop("reactions", UNSET))

        def _parse_read_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_only = _parse_read_only(d.pop("read_only", UNSET))

        def _parse_recurring_rule_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recurring_rule_id = _parse_recurring_rule_id(d.pop("recurring_rule_id", UNSET))

        def _parse_service_period_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_period_from_type_0 = datetime.date.fromisoformat(data)

                return service_period_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        service_period_from = _parse_service_period_from(d.pop("service_period_from", UNSET))

        def _parse_service_period_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_period_to_type_0 = datetime.date.fromisoformat(data)

                return service_period_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        service_period_to = _parse_service_period_to(d.pop("service_period_to", UNSET))

        def _parse_splits(data: object) -> list[TransactionResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = TransactionResponse.from_dict(splits_type_0_item_data)

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TransactionResponse] | None | Unset, data)

        splits = _parse_splits(d.pop("splits", UNSET))

        def _parse_tags(data: object) -> list[TransactionTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = TransactionTag.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TransactionTag] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_treatment(data: object) -> None | TransactionTreatment | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                treatment_type_0 = TransactionTreatment.from_dict(data)

                return treatment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionTreatment | Unset, data)

        treatment = _parse_treatment(d.pop("treatment", UNSET))

        def _parse_uah_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uah_amount = decimal_in(_parse_uah_amount(d.pop("uah_amount", UNSET)))

        def _parse_uah_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uah_rate = decimal_in(_parse_uah_rate(d.pop("uah_rate", UNSET)))

        def _parse_uah_rate_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uah_rate_date_type_0 = datetime.date.fromisoformat(data)

                return uah_rate_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        uah_rate_date = _parse_uah_rate_date(d.pop("uah_rate_date", UNSET))

        def _parse_uah_status(data: object) -> None | TransactionResponseUahStatusType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uah_status_type_0 = check_transaction_response_uah_status_type_0(data)

                return uah_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionResponseUahStatusType0 | Unset, data)

        uah_status = _parse_uah_status(d.pop("uah_status", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        transaction_response = cls(
            account_id=account_id,
            account_name=account_name,
            amount=amount,
            created_at=created_at,
            description=description,
            direction=direction,
            external_data=external_data,
            financials=financials,
            id=id,
            is_deleted=is_deleted,
            is_split=is_split,
            metadata=metadata,
            relationships=relationships,
            space_id=space_id,
            status=status,
            timestamps=timestamps,
            transaction_date=transaction_date,
            type_=type_,
            updated_at=updated_at,
            category_color=category_color,
            category_emoji=category_emoji,
            category_icon=category_icon,
            category_id=category_id,
            category_is_transfer=category_is_transfer,
            category_name=category_name,
            category_review=category_review,
            counterpart_account_id=counterpart_account_id,
            counterpart_account_name=counterpart_account_name,
            counterpart_hidden=counterpart_hidden,
            counterpart_space=counterpart_space,
            counterpart_space_hidden=counterpart_space_hidden,
            counterpart_space_id=counterpart_space_id,
            counterpart_transaction_id=counterpart_transaction_id,
            counterparty_id=counterparty_id,
            counts_as_income=counts_as_income,
            created_by=created_by,
            created_by_name=created_by_name,
            cross_space_transfer_id=cross_space_transfer_id,
            exchange_rate=exchange_rate,
            fee_for_transfer_id=fee_for_transfer_id,
            fee_transaction_id=fee_transaction_id,
            kind=kind,
            linked_activity=linked_activity,
            linked_transfer_id=linked_transfer_id,
            merchant=merchant,
            merchant_brand=merchant_brand,
            not_income=not_income,
            note=note,
            original_amount=original_amount,
            original_currency=original_currency,
            parent_id=parent_id,
            place=place,
            place_id=place_id,
            place_source=place_source,
            portfolio_transfer=portfolio_transfer,
            project_id=project_id,
            reactions=reactions,
            read_only=read_only,
            recurring_rule_id=recurring_rule_id,
            service_period_from=service_period_from,
            service_period_to=service_period_to,
            splits=splits,
            tags=tags,
            treatment=treatment,
            uah_amount=uah_amount,
            uah_rate=uah_rate,
            uah_rate_date=uah_rate_date,
            uah_status=uah_status,
            version=version,
        )

        transaction_response.additional_properties = d
        return transaction_response

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
