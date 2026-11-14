from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.analytics_currency_info import AnalyticsCurrencyInfo
    from ..models.trend_comparison import TrendComparison


T = TypeVar("T", bound="TrendsResponse")


@_attrs_define
class TrendsResponse:
    """
    Attributes:
        currency_info (AnalyticsCurrencyInfo):
        missing_rates (list[str] | None | Unset): `missing_rates` lists currencies whose amounts could not be converted
            into the response currency (no exchange rate available). Those amounts are excluded from the totals above;
            empty/omitted when everything converted.
        pending_valuation (int | None | Unset): `pending_valuation` counts the business-space transactions of the period
            that have no UAH value yet (the NBU rate of their legal date is not published, or the valuation has not run):
            they are left out of the totals above until valued. Omitted when 0 and in personal spaces.
        trends (list[TrendComparison] | None | Unset):
    """

    currency_info: AnalyticsCurrencyInfo
    missing_rates: list[str] | None | Unset = UNSET
    pending_valuation: int | None | Unset = UNSET
    trends: list[TrendComparison] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.trend_comparison import TrendComparison  # noqa: PLC0415

        currency_info = self.currency_info.to_dict()

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

        trends: list[dict[str, Any]] | None | Unset
        if isinstance(self.trends, Unset):
            trends = UNSET
        elif isinstance(self.trends, list):
            trends = []
            for trends_type_0_item_data in self.trends:
                trends_type_0_item = trends_type_0_item_data.to_dict()
                trends.append(trends_type_0_item)

        else:
            trends = self.trends

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyInfo": currency_info,
            }
        )
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates
        if pending_valuation is not UNSET:
            field_dict["pending_valuation"] = pending_valuation
        if trends is not UNSET:
            field_dict["trends"] = trends

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.trend_comparison import TrendComparison  # noqa: PLC0415

        d = dict(src_dict)
        currency_info = AnalyticsCurrencyInfo.from_dict(d.pop("currencyInfo"))

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

        def _parse_trends(data: object) -> list[TrendComparison] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trends_type_0 = []
                _trends_type_0 = data
                for trends_type_0_item_data in _trends_type_0:
                    trends_type_0_item = TrendComparison.from_dict(trends_type_0_item_data)

                    trends_type_0.append(trends_type_0_item)

                return trends_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TrendComparison] | None | Unset, data)

        trends = _parse_trends(d.pop("trends", UNSET))

        trends_response = cls(
            currency_info=currency_info,
            missing_rates=missing_rates,
            pending_valuation=pending_valuation,
            trends=trends,
        )

        trends_response.additional_properties = d
        return trends_response

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
