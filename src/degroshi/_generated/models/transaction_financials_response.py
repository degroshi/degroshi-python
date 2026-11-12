from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.transaction_amounts_response import TransactionAmountsResponse


T = TypeVar("T", bound="TransactionFinancialsResponse")


@_attrs_define
class TransactionFinancialsResponse:
    """
    Attributes:
        amounts (TransactionAmountsResponse):
        transaction_date (datetime.datetime):
        credit_breakdown (Any | None | Unset):
        credit_money_used (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a
            JSON number.
        currency_conversion_date (datetime.datetime | None | Unset):
        currency_conversion_rate (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600");
            never a JSON number.
        exchange_rate (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON
            number.
        own_money_used (None | Decimal | Unset): Decimal number encoded as a string (for example "1234.5600"); never a JSON
            number.
        post_date (datetime.datetime | None | Unset):
    """

    amounts: TransactionAmountsResponse
    transaction_date: datetime.datetime
    credit_breakdown: Any | None | Unset = UNSET
    credit_money_used: None | Decimal | Unset = UNSET
    currency_conversion_date: datetime.datetime | None | Unset = UNSET
    currency_conversion_rate: None | Decimal | Unset = UNSET
    exchange_rate: None | Decimal | Unset = UNSET
    own_money_used: None | Decimal | Unset = UNSET
    post_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_amounts_response import TransactionAmountsResponse  # noqa: PLC0415

        amounts = self.amounts.to_dict()

        transaction_date = self.transaction_date.isoformat()

        credit_breakdown: Any | None | Unset
        if isinstance(self.credit_breakdown, Unset):
            credit_breakdown = UNSET
        else:
            credit_breakdown = self.credit_breakdown

        credit_money_used: None | Decimal | Unset
        if isinstance(self.credit_money_used, Unset):
            credit_money_used = UNSET
        else:
            credit_money_used = decimal_out(self.credit_money_used)

        currency_conversion_date: None | str | Unset
        if isinstance(self.currency_conversion_date, Unset):
            currency_conversion_date = UNSET
        elif isinstance(self.currency_conversion_date, datetime.datetime):
            currency_conversion_date = self.currency_conversion_date.isoformat()
        else:
            currency_conversion_date = self.currency_conversion_date

        currency_conversion_rate: None | Decimal | Unset
        if isinstance(self.currency_conversion_rate, Unset):
            currency_conversion_rate = UNSET
        else:
            currency_conversion_rate = decimal_out(self.currency_conversion_rate)

        exchange_rate: None | Decimal | Unset
        if isinstance(self.exchange_rate, Unset):
            exchange_rate = UNSET
        else:
            exchange_rate = decimal_out(self.exchange_rate)

        own_money_used: None | Decimal | Unset
        if isinstance(self.own_money_used, Unset):
            own_money_used = UNSET
        else:
            own_money_used = decimal_out(self.own_money_used)

        post_date: None | str | Unset
        if isinstance(self.post_date, Unset):
            post_date = UNSET
        elif isinstance(self.post_date, datetime.datetime):
            post_date = self.post_date.isoformat()
        else:
            post_date = self.post_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amounts": amounts,
                "transactionDate": transaction_date,
            }
        )
        if credit_breakdown is not UNSET:
            field_dict["creditBreakdown"] = credit_breakdown
        if credit_money_used is not UNSET:
            field_dict["creditMoneyUsed"] = credit_money_used
        if currency_conversion_date is not UNSET:
            field_dict["currencyConversionDate"] = currency_conversion_date
        if currency_conversion_rate is not UNSET:
            field_dict["currencyConversionRate"] = currency_conversion_rate
        if exchange_rate is not UNSET:
            field_dict["exchangeRate"] = exchange_rate
        if own_money_used is not UNSET:
            field_dict["ownMoneyUsed"] = own_money_used
        if post_date is not UNSET:
            field_dict["postDate"] = post_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_amounts_response import TransactionAmountsResponse  # noqa: PLC0415

        d = dict(src_dict)
        amounts = TransactionAmountsResponse.from_dict(d.pop("amounts"))

        transaction_date = datetime.datetime.fromisoformat(d.pop("transactionDate"))

        def _parse_credit_breakdown(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        credit_breakdown = _parse_credit_breakdown(d.pop("creditBreakdown", UNSET))

        def _parse_credit_money_used(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credit_money_used = decimal_in(_parse_credit_money_used(d.pop("creditMoneyUsed", UNSET)))

        def _parse_currency_conversion_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                currency_conversion_date_type_0 = datetime.datetime.fromisoformat(data)

                return currency_conversion_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        currency_conversion_date = _parse_currency_conversion_date(d.pop("currencyConversionDate", UNSET))

        def _parse_currency_conversion_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_conversion_rate = decimal_in(_parse_currency_conversion_rate(d.pop("currencyConversionRate", UNSET)))

        def _parse_exchange_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_rate = decimal_in(_parse_exchange_rate(d.pop("exchangeRate", UNSET)))

        def _parse_own_money_used(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        own_money_used = decimal_in(_parse_own_money_used(d.pop("ownMoneyUsed", UNSET)))

        def _parse_post_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_date_type_0 = datetime.datetime.fromisoformat(data)

                return post_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        post_date = _parse_post_date(d.pop("postDate", UNSET))

        transaction_financials_response = cls(
            amounts=amounts,
            transaction_date=transaction_date,
            credit_breakdown=credit_breakdown,
            credit_money_used=credit_money_used,
            currency_conversion_date=currency_conversion_date,
            currency_conversion_rate=currency_conversion_rate,
            exchange_rate=exchange_rate,
            own_money_used=own_money_used,
            post_date=post_date,
        )

        transaction_financials_response.additional_properties = d
        return transaction_financials_response

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
