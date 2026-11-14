from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_type import AccountType
from ..models.account_type import check_account_type
from ..models.gradient_type import check_gradient_type
from ..models.gradient_type import GradientType
from ..models.interest_payout import check_interest_payout
from ..models.interest_payout import InterestPayout
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.account_brand import AccountBrand
    from ..models.account_connection import AccountConnection
    from ..models.account_response_metadata_type_0 import AccountResponseMetadataType0
    from ..models.account_source import AccountSource
    from ..models.accounts_currency_info import AccountsCurrencyInfo
    from ..models.grant_info import GrantInfo
    from ..models.shared_with import SharedWith


T = TypeVar("T", bound="AccountResponse")


@_attrs_define
class AccountResponse:
    """
    Attributes:
        created_at (datetime.datetime):
        currency_code (str):
        currency_info (AccountsCurrencyInfo):
        current_balance (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        display_order (int):
        grain_intensity (int):
        id (str):
        include_in_net_worth (bool):
        is_closed (bool):
        is_gradient (bool):
        is_liability (bool):
        is_shared (bool): Deprecated: always false.
        name (str):
        space_id (str):
        type_ (AccountType):
        updated_at (datetime.datetime):
        user_id (str):
        annual_rate (None | Decimal | Unset): The interest rate in percent a year (14.5 = 14.5% a year), at most 2 decimals,
            0–100: a deposit's or savings account's, a credit card's after its grace period, a credit line's, loan's or
            mortgage's.
        available_balance (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a
            JSON number.
        balance_version (int | None | Unset): The version of the account's balance.
        brand (AccountBrand | None | Unset):
        brand_domain (None | str | Unset): The bank's or service's site; Brand is its logo for the account mark, omitted
            without a domain.
        color (None | str | Unset):
        connection (AccountConnection | None | Unset): Set for an account fed by a bank, wallet or exchange: its balance
            is read-only. Absent for a manual account.
        credit_limit (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON
            number.
        goal_amount (None | Decimal | Unset): A savings goal in the account's currency (above 0).
        goal_date (datetime.date | None | Unset): The day the goal should be reached by.
        grace_period_days (int | None | Unset): The longest interest-free period the bank states (1–200). Descriptive:
            the due day sets the date.
        gradient_direction (int | None | Unset):
        gradient_type (GradientType | None | Unset):
        grant (GrantInfo | None | Unset): Reserved; not returned yet.
        icon (None | str | Unset):
        interest_payout (InterestPayout | None | Unset): When a deposit pays its interest: monthly, quarterly,
            at_maturity (with the deposit) or capitalized (added to it).
        metadata (AccountResponseMetadataType0 | None | Unset):
        minimum_payment_amount (None | Decimal | Unset): The least the minimum payment can be, in the account's currency.
            The minimum due is the larger of the percent of the debt and this, at most the debt.
        minimum_payment_percent (None | Decimal | Unset): A credit card's or line's minimum payment in percent of the debt
            (0–100, at most 2 decimals): «5%».
        overdraft_limit (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON
            number.
        payment_due_day (int | None | Unset): The day of the month by which the minimum payment is due and the grace
            period ends (1–31; in a shorter month, its last day).
        share_amount (None | Decimal | Unset): Reserved; not returned yet. Account sharing, “My part”: the part of
            current_balance that counts in this space's totals, in the same currency: the requester's capital on an account
            pooled with them, the balance less the grantees' capital on an account this space pools with others. Absent
            where the whole balance counts. Totals count include_in_net_worth ? (share_amount ?? current_balance) : 0, with
            the usual sign rules.
        shared_with (list[SharedWith] | None | Unset): Reserved; not returned yet.
        source (AccountSource | None | Unset): Set for an account a custom source pushes through the API; absent for
            others.
        term_end_date (datetime.date | None | Unset): The day the deposit, loan or credit line ends. Kept as entered: it
            isn't derived from term_months.
        term_months (int | None | Unset): The term in months (1–600).
        version (int | None | Unset): The account row version (also the ETag): send it as If-Match on PATCH / DELETE to
            detect concurrent edits (412).
    """

    created_at: datetime.datetime
    currency_code: str
    currency_info: AccountsCurrencyInfo
    current_balance: Decimal
    display_order: int
    grain_intensity: int
    id: str
    include_in_net_worth: bool
    is_closed: bool
    is_gradient: bool
    is_liability: bool
    is_shared: bool
    name: str
    space_id: str
    type_: AccountType
    updated_at: datetime.datetime
    user_id: str
    annual_rate: None | Decimal | Unset = UNSET
    available_balance: None | Decimal | Unset = UNSET
    balance_version: int | None | Unset = UNSET
    brand: AccountBrand | None | Unset = UNSET
    brand_domain: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    connection: AccountConnection | None | Unset = UNSET
    credit_limit: None | Decimal | Unset = UNSET
    goal_amount: None | Decimal | Unset = UNSET
    goal_date: datetime.date | None | Unset = UNSET
    grace_period_days: int | None | Unset = UNSET
    gradient_direction: int | None | Unset = UNSET
    gradient_type: GradientType | None | Unset = UNSET
    grant: GrantInfo | None | Unset = UNSET
    icon: None | str | Unset = UNSET
    interest_payout: InterestPayout | None | Unset = UNSET
    metadata: AccountResponseMetadataType0 | None | Unset = UNSET
    minimum_payment_amount: None | Decimal | Unset = UNSET
    minimum_payment_percent: None | Decimal | Unset = UNSET
    overdraft_limit: None | Decimal | Unset = UNSET
    payment_due_day: int | None | Unset = UNSET
    share_amount: None | Decimal | Unset = UNSET
    shared_with: list[SharedWith] | None | Unset = UNSET
    source: AccountSource | None | Unset = UNSET
    term_end_date: datetime.date | None | Unset = UNSET
    term_months: int | None | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.account_brand import AccountBrand  # noqa: PLC0415
        from ..models.account_connection import AccountConnection  # noqa: PLC0415
        from ..models.account_response_metadata_type_0 import AccountResponseMetadataType0  # noqa: PLC0415
        from ..models.account_source import AccountSource  # noqa: PLC0415
        from ..models.accounts_currency_info import AccountsCurrencyInfo  # noqa: PLC0415
        from ..models.grant_info import GrantInfo  # noqa: PLC0415
        from ..models.shared_with import SharedWith  # noqa: PLC0415

        created_at = self.created_at.isoformat()

        currency_code = self.currency_code

        currency_info = self.currency_info.to_dict()

        current_balance = decimal_out(self.current_balance)

        display_order = self.display_order

        grain_intensity = self.grain_intensity

        id = self.id

        include_in_net_worth = self.include_in_net_worth

        is_closed = self.is_closed

        is_gradient = self.is_gradient

        is_liability = self.is_liability

        is_shared = self.is_shared

        name = self.name

        space_id = self.space_id

        type_: str = self.type_

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        annual_rate: None | Decimal | Unset
        if isinstance(self.annual_rate, Unset):
            annual_rate = UNSET
        else:
            annual_rate = decimal_out(self.annual_rate)

        available_balance: None | Decimal | Unset
        if isinstance(self.available_balance, Unset):
            available_balance = UNSET
        else:
            available_balance = decimal_out(self.available_balance)

        balance_version: int | None | Unset
        if isinstance(self.balance_version, Unset):
            balance_version = UNSET
        else:
            balance_version = self.balance_version

        brand: dict[str, Any] | None | Unset
        if isinstance(self.brand, Unset):
            brand = UNSET
        elif isinstance(self.brand, AccountBrand):
            brand = self.brand.to_dict()
        else:
            brand = self.brand

        brand_domain: None | str | Unset
        if isinstance(self.brand_domain, Unset):
            brand_domain = UNSET
        else:
            brand_domain = self.brand_domain

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        connection: dict[str, Any] | None | Unset
        if isinstance(self.connection, Unset):
            connection = UNSET
        elif isinstance(self.connection, AccountConnection):
            connection = self.connection.to_dict()
        else:
            connection = self.connection

        credit_limit: None | Decimal | Unset
        if isinstance(self.credit_limit, Unset):
            credit_limit = UNSET
        else:
            credit_limit = decimal_out(self.credit_limit)

        goal_amount: None | Decimal | Unset
        if isinstance(self.goal_amount, Unset):
            goal_amount = UNSET
        else:
            goal_amount = decimal_out(self.goal_amount)

        goal_date: None | str | Unset
        if isinstance(self.goal_date, Unset):
            goal_date = UNSET
        elif isinstance(self.goal_date, datetime.date):
            goal_date = self.goal_date.isoformat()
        else:
            goal_date = self.goal_date

        grace_period_days: int | None | Unset
        if isinstance(self.grace_period_days, Unset):
            grace_period_days = UNSET
        else:
            grace_period_days = self.grace_period_days

        gradient_direction: int | None | Unset
        if isinstance(self.gradient_direction, Unset):
            gradient_direction = UNSET
        else:
            gradient_direction = self.gradient_direction

        gradient_type: None | str | Unset
        if isinstance(self.gradient_type, Unset):
            gradient_type = UNSET
        elif isinstance(self.gradient_type, str):
            gradient_type = self.gradient_type
        else:
            gradient_type = self.gradient_type

        grant: dict[str, Any] | None | Unset
        if isinstance(self.grant, Unset):
            grant = UNSET
        elif isinstance(self.grant, GrantInfo):
            grant = self.grant.to_dict()
        else:
            grant = self.grant

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        interest_payout: None | str | Unset
        if isinstance(self.interest_payout, Unset):
            interest_payout = UNSET
        elif isinstance(self.interest_payout, str):
            interest_payout = self.interest_payout
        else:
            interest_payout = self.interest_payout

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AccountResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        minimum_payment_amount: None | Decimal | Unset
        if isinstance(self.minimum_payment_amount, Unset):
            minimum_payment_amount = UNSET
        else:
            minimum_payment_amount = decimal_out(self.minimum_payment_amount)

        minimum_payment_percent: None | Decimal | Unset
        if isinstance(self.minimum_payment_percent, Unset):
            minimum_payment_percent = UNSET
        else:
            minimum_payment_percent = decimal_out(self.minimum_payment_percent)

        overdraft_limit: None | Decimal | Unset
        if isinstance(self.overdraft_limit, Unset):
            overdraft_limit = UNSET
        else:
            overdraft_limit = decimal_out(self.overdraft_limit)

        payment_due_day: int | None | Unset
        if isinstance(self.payment_due_day, Unset):
            payment_due_day = UNSET
        else:
            payment_due_day = self.payment_due_day

        share_amount: None | Decimal | Unset
        if isinstance(self.share_amount, Unset):
            share_amount = UNSET
        else:
            share_amount = decimal_out(self.share_amount)

        shared_with: list[dict[str, Any]] | None | Unset
        if isinstance(self.shared_with, Unset):
            shared_with = UNSET
        elif isinstance(self.shared_with, list):
            shared_with = []
            for shared_with_type_0_item_data in self.shared_with:
                shared_with_type_0_item = shared_with_type_0_item_data.to_dict()
                shared_with.append(shared_with_type_0_item)

        else:
            shared_with = self.shared_with

        source: dict[str, Any] | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, AccountSource):
            source = self.source.to_dict()
        else:
            source = self.source

        term_end_date: None | str | Unset
        if isinstance(self.term_end_date, Unset):
            term_end_date = UNSET
        elif isinstance(self.term_end_date, datetime.date):
            term_end_date = self.term_end_date.isoformat()
        else:
            term_end_date = self.term_end_date

        term_months: int | None | Unset
        if isinstance(self.term_months, Unset):
            term_months = UNSET
        else:
            term_months = self.term_months

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "currency_code": currency_code,
                "currency_info": currency_info,
                "current_balance": current_balance,
                "display_order": display_order,
                "grain_intensity": grain_intensity,
                "id": id,
                "include_in_net_worth": include_in_net_worth,
                "is_closed": is_closed,
                "is_gradient": is_gradient,
                "is_liability": is_liability,
                "is_shared": is_shared,
                "name": name,
                "space_id": space_id,
                "type": type_,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )
        if annual_rate is not UNSET:
            field_dict["annual_rate"] = annual_rate
        if available_balance is not UNSET:
            field_dict["available_balance"] = available_balance
        if balance_version is not UNSET:
            field_dict["balance_version"] = balance_version
        if brand is not UNSET:
            field_dict["brand"] = brand
        if brand_domain is not UNSET:
            field_dict["brand_domain"] = brand_domain
        if color is not UNSET:
            field_dict["color"] = color
        if connection is not UNSET:
            field_dict["connection"] = connection
        if credit_limit is not UNSET:
            field_dict["credit_limit"] = credit_limit
        if goal_amount is not UNSET:
            field_dict["goal_amount"] = goal_amount
        if goal_date is not UNSET:
            field_dict["goal_date"] = goal_date
        if grace_period_days is not UNSET:
            field_dict["grace_period_days"] = grace_period_days
        if gradient_direction is not UNSET:
            field_dict["gradient_direction"] = gradient_direction
        if gradient_type is not UNSET:
            field_dict["gradient_type"] = gradient_type
        if grant is not UNSET:
            field_dict["grant"] = grant
        if icon is not UNSET:
            field_dict["icon"] = icon
        if interest_payout is not UNSET:
            field_dict["interest_payout"] = interest_payout
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if minimum_payment_amount is not UNSET:
            field_dict["minimum_payment_amount"] = minimum_payment_amount
        if minimum_payment_percent is not UNSET:
            field_dict["minimum_payment_percent"] = minimum_payment_percent
        if overdraft_limit is not UNSET:
            field_dict["overdraft_limit"] = overdraft_limit
        if payment_due_day is not UNSET:
            field_dict["payment_due_day"] = payment_due_day
        if share_amount is not UNSET:
            field_dict["share_amount"] = share_amount
        if shared_with is not UNSET:
            field_dict["shared_with"] = shared_with
        if source is not UNSET:
            field_dict["source"] = source
        if term_end_date is not UNSET:
            field_dict["term_end_date"] = term_end_date
        if term_months is not UNSET:
            field_dict["term_months"] = term_months
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_brand import AccountBrand  # noqa: PLC0415
        from ..models.account_connection import AccountConnection  # noqa: PLC0415
        from ..models.account_response_metadata_type_0 import AccountResponseMetadataType0  # noqa: PLC0415
        from ..models.account_source import AccountSource  # noqa: PLC0415
        from ..models.accounts_currency_info import AccountsCurrencyInfo  # noqa: PLC0415
        from ..models.grant_info import GrantInfo  # noqa: PLC0415
        from ..models.shared_with import SharedWith  # noqa: PLC0415

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency_code = d.pop("currency_code")

        currency_info = AccountsCurrencyInfo.from_dict(d.pop("currency_info"))

        current_balance = decimal_in(d.pop("current_balance"))

        display_order = d.pop("display_order")

        grain_intensity = d.pop("grain_intensity")

        id = d.pop("id")

        include_in_net_worth = d.pop("include_in_net_worth")

        is_closed = d.pop("is_closed")

        is_gradient = d.pop("is_gradient")

        is_liability = d.pop("is_liability")

        is_shared = d.pop("is_shared")

        name = d.pop("name")

        space_id = d.pop("space_id")

        type_ = check_account_type(d.pop("type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        user_id = d.pop("user_id")

        def _parse_annual_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annual_rate = decimal_in(_parse_annual_rate(d.pop("annual_rate", UNSET)))

        def _parse_available_balance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        available_balance = decimal_in(_parse_available_balance(d.pop("available_balance", UNSET)))

        def _parse_balance_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        balance_version = _parse_balance_version(d.pop("balance_version", UNSET))

        def _parse_brand(data: object) -> AccountBrand | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                brand_type_0 = AccountBrand.from_dict(data)

                return brand_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountBrand | None | Unset, data)

        brand = _parse_brand(d.pop("brand", UNSET))

        def _parse_brand_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand_domain = _parse_brand_domain(d.pop("brand_domain", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_connection(data: object) -> AccountConnection | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connection_type_0 = AccountConnection.from_dict(data)

                return connection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountConnection | None | Unset, data)

        connection = _parse_connection(d.pop("connection", UNSET))

        def _parse_credit_limit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credit_limit = decimal_in(_parse_credit_limit(d.pop("credit_limit", UNSET)))

        def _parse_goal_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        goal_amount = decimal_in(_parse_goal_amount(d.pop("goal_amount", UNSET)))

        def _parse_goal_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                goal_date_type_0 = datetime.date.fromisoformat(data)

                return goal_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        goal_date = _parse_goal_date(d.pop("goal_date", UNSET))

        def _parse_grace_period_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grace_period_days = _parse_grace_period_days(d.pop("grace_period_days", UNSET))

        def _parse_gradient_direction(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gradient_direction = _parse_gradient_direction(d.pop("gradient_direction", UNSET))

        def _parse_gradient_type(data: object) -> GradientType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gradient_type_type_0 = check_gradient_type(data)

                return gradient_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GradientType | None | Unset, data)

        gradient_type = _parse_gradient_type(d.pop("gradient_type", UNSET))

        def _parse_grant(data: object) -> GrantInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grant_type_0 = GrantInfo.from_dict(data)

                return grant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GrantInfo | None | Unset, data)

        grant = _parse_grant(d.pop("grant", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_interest_payout(data: object) -> InterestPayout | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                interest_payout_type_0 = check_interest_payout(data)

                return interest_payout_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InterestPayout | None | Unset, data)

        interest_payout = _parse_interest_payout(d.pop("interest_payout", UNSET))

        def _parse_metadata(data: object) -> AccountResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AccountResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_minimum_payment_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_payment_amount = decimal_in(_parse_minimum_payment_amount(d.pop("minimum_payment_amount", UNSET)))

        def _parse_minimum_payment_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_payment_percent = decimal_in(_parse_minimum_payment_percent(d.pop("minimum_payment_percent", UNSET)))

        def _parse_overdraft_limit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overdraft_limit = decimal_in(_parse_overdraft_limit(d.pop("overdraft_limit", UNSET)))

        def _parse_payment_due_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        payment_due_day = _parse_payment_due_day(d.pop("payment_due_day", UNSET))

        def _parse_share_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        share_amount = decimal_in(_parse_share_amount(d.pop("share_amount", UNSET)))

        def _parse_shared_with(data: object) -> list[SharedWith] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                shared_with_type_0 = []
                _shared_with_type_0 = data
                for shared_with_type_0_item_data in _shared_with_type_0:
                    shared_with_type_0_item = SharedWith.from_dict(shared_with_type_0_item_data)

                    shared_with_type_0.append(shared_with_type_0_item)

                return shared_with_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SharedWith] | None | Unset, data)

        shared_with = _parse_shared_with(d.pop("shared_with", UNSET))

        def _parse_source(data: object) -> AccountSource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = AccountSource.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountSource | None | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_term_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                term_end_date_type_0 = datetime.date.fromisoformat(data)

                return term_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        term_end_date = _parse_term_end_date(d.pop("term_end_date", UNSET))

        def _parse_term_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        term_months = _parse_term_months(d.pop("term_months", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        account_response = cls(
            created_at=created_at,
            currency_code=currency_code,
            currency_info=currency_info,
            current_balance=current_balance,
            display_order=display_order,
            grain_intensity=grain_intensity,
            id=id,
            include_in_net_worth=include_in_net_worth,
            is_closed=is_closed,
            is_gradient=is_gradient,
            is_liability=is_liability,
            is_shared=is_shared,
            name=name,
            space_id=space_id,
            type_=type_,
            updated_at=updated_at,
            user_id=user_id,
            annual_rate=annual_rate,
            available_balance=available_balance,
            balance_version=balance_version,
            brand=brand,
            brand_domain=brand_domain,
            color=color,
            connection=connection,
            credit_limit=credit_limit,
            goal_amount=goal_amount,
            goal_date=goal_date,
            grace_period_days=grace_period_days,
            gradient_direction=gradient_direction,
            gradient_type=gradient_type,
            grant=grant,
            icon=icon,
            interest_payout=interest_payout,
            metadata=metadata,
            minimum_payment_amount=minimum_payment_amount,
            minimum_payment_percent=minimum_payment_percent,
            overdraft_limit=overdraft_limit,
            payment_due_day=payment_due_day,
            share_amount=share_amount,
            shared_with=shared_with,
            source=source,
            term_end_date=term_end_date,
            term_months=term_months,
            version=version,
        )

        account_response.additional_properties = d
        return account_response

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
