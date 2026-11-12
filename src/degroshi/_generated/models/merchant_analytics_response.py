from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.merchant_analytics_response_side import check_merchant_analytics_response_side
from ..models.merchant_analytics_response_side import MerchantAnalyticsResponseSide
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.analytics_currency_info import AnalyticsCurrencyInfo
    from ..models.merchant_activity import MerchantActivity
    from ..models.merchant_figures import MerchantFigures


T = TypeVar("T", bound="MerchantAnalyticsResponse")


@_attrs_define
class MerchantAnalyticsResponse:
    """
    Attributes:
        currency_info (AnalyticsCurrencyInfo):
        from_ (datetime.date):
        merchants (list[MerchantActivity]): The merchants with operations in the period, the largest amount first, at
            most `limit`.
        previous_from (datetime.date):
        previous_to (datetime.date):
        side (MerchantAnalyticsResponseSide): The side the amounts are of: expense or income.
        to (datetime.date):
        total (MerchantFigures):
        unattributed (MerchantFigures):
        missing_rates (list[str] | None | Unset): Lists currencies without an exchange rate; their amounts are left out.
            Omitted when everything converted.
        pending_valuation (int | None | Unset): Counts the business-space operations of the period that have no UAH
            value yet (left out). Omitted when 0.
    """

    currency_info: AnalyticsCurrencyInfo
    from_: datetime.date
    merchants: list[MerchantActivity]
    previous_from: datetime.date
    previous_to: datetime.date
    side: MerchantAnalyticsResponseSide
    to: datetime.date
    total: MerchantFigures
    unattributed: MerchantFigures
    missing_rates: list[str] | None | Unset = UNSET
    pending_valuation: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.merchant_activity import MerchantActivity  # noqa: PLC0415
        from ..models.merchant_figures import MerchantFigures  # noqa: PLC0415

        currency_info = self.currency_info.to_dict()

        from_ = self.from_.isoformat()

        merchants = []
        for merchants_item_data in self.merchants:
            merchants_item = merchants_item_data.to_dict()
            merchants.append(merchants_item)

        previous_from = self.previous_from.isoformat()

        previous_to = self.previous_to.isoformat()

        side: str = self.side

        to = self.to.isoformat()

        total = self.total.to_dict()

        unattributed = self.unattributed.to_dict()

        missing_rates: list[str] | None | Unset
        if isinstance(self.missing_rates, Unset):
            missing_rates = UNSET
        elif isinstance(self.missing_rates, list):
            missing_rates = self.missing_rates

        else:
            missing_rates = self.missing_rates

        pending_valuation: int | None | Unset
        if isinstance(self.pending_valuation, Unset):
            pending_valuation = UNSET
        else:
            pending_valuation = self.pending_valuation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyInfo": currency_info,
                "from": from_,
                "merchants": merchants,
                "previous_from": previous_from,
                "previous_to": previous_to,
                "side": side,
                "to": to,
                "total": total,
                "unattributed": unattributed,
            }
        )
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates
        if pending_valuation is not UNSET:
            field_dict["pending_valuation"] = pending_valuation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.merchant_activity import MerchantActivity  # noqa: PLC0415
        from ..models.merchant_figures import MerchantFigures  # noqa: PLC0415

        d = dict(src_dict)
        currency_info = AnalyticsCurrencyInfo.from_dict(d.pop("currencyInfo"))

        from_ = datetime.date.fromisoformat(d.pop("from"))

        merchants = []
        _merchants = d.pop("merchants")
        for merchants_item_data in _merchants:
            merchants_item = MerchantActivity.from_dict(merchants_item_data)

            merchants.append(merchants_item)

        previous_from = datetime.date.fromisoformat(d.pop("previous_from"))

        previous_to = datetime.date.fromisoformat(d.pop("previous_to"))

        side = check_merchant_analytics_response_side(d.pop("side"))

        to = datetime.date.fromisoformat(d.pop("to"))

        total = MerchantFigures.from_dict(d.pop("total"))

        unattributed = MerchantFigures.from_dict(d.pop("unattributed"))

        def _parse_missing_rates(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_rates_type_0 = cast(list[str], data)

                return missing_rates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        missing_rates = _parse_missing_rates(d.pop("missing_rates", UNSET))

        def _parse_pending_valuation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pending_valuation = _parse_pending_valuation(d.pop("pending_valuation", UNSET))

        merchant_analytics_response = cls(
            currency_info=currency_info,
            from_=from_,
            merchants=merchants,
            previous_from=previous_from,
            previous_to=previous_to,
            side=side,
            to=to,
            total=total,
            unattributed=unattributed,
            missing_rates=missing_rates,
            pending_valuation=pending_valuation,
        )

        merchant_analytics_response.additional_properties = d
        return merchant_analytics_response

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
