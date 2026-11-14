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

if TYPE_CHECKING:
    from ..models.analytics_currency_info import AnalyticsCurrencyInfo
    from ..models.category_analytics_item import CategoryAnalyticsItem
    from ..models.date_range import DateRange
    from ..models.uncategorized_activity import UncategorizedActivity


T = TypeVar("T", bound="CategoryAnalyticsResponse")


@_attrs_define
class CategoryAnalyticsResponse:
    """
    Attributes:
        categories_count (int):
        currency_info (AnalyticsCurrencyInfo):
        net (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        period (DateRange):
        total_expenses (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        total_income (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        transactions_analyzed (int):
        uncategorized (UncategorizedActivity):
        categories (list[CategoryAnalyticsItem] | None | Unset):
        missing_rates (list[str] | None | Unset): `missing_rates` lists currencies whose amounts could not be converted
            into the response currency (no exchange rate available). Those amounts are excluded from the totals above;
            empty/omitted when everything converted.
        pending_valuation (int | None | Unset): `pending_valuation` counts the business-space transactions of the period
            that have no UAH value yet (the NBU rate of their legal date is not published, or the valuation has not run):
            they are left out of the totals above until valued. Omitted when 0 and in personal spaces.
    """

    categories_count: int
    currency_info: AnalyticsCurrencyInfo
    net: Decimal
    period: DateRange
    total_expenses: Decimal
    total_income: Decimal
    transactions_analyzed: int
    uncategorized: UncategorizedActivity
    categories: list[CategoryAnalyticsItem] | None | Unset = UNSET
    missing_rates: list[str] | None | Unset = UNSET
    pending_valuation: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.category_analytics_item import CategoryAnalyticsItem  # noqa: PLC0415
        from ..models.date_range import DateRange  # noqa: PLC0415
        from ..models.uncategorized_activity import UncategorizedActivity  # noqa: PLC0415

        categories_count = self.categories_count

        currency_info = self.currency_info.to_dict()

        net = decimal_out(self.net)

        period = self.period.to_dict()

        total_expenses = decimal_out(self.total_expenses)

        total_income = decimal_out(self.total_income)

        transactions_analyzed = self.transactions_analyzed

        uncategorized = self.uncategorized.to_dict()

        categories: list[dict[str, Any]] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)

        else:
            categories = self.categories

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
                "categories_count": categories_count,
                "currencyInfo": currency_info,
                "net": net,
                "period": period,
                "total_expenses": total_expenses,
                "total_income": total_income,
                "transactions_analyzed": transactions_analyzed,
                "uncategorized": uncategorized,
            }
        )
        if categories is not UNSET:
            field_dict["categories"] = categories
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates
        if pending_valuation is not UNSET:
            field_dict["pending_valuation"] = pending_valuation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.category_analytics_item import CategoryAnalyticsItem  # noqa: PLC0415
        from ..models.date_range import DateRange  # noqa: PLC0415
        from ..models.uncategorized_activity import UncategorizedActivity  # noqa: PLC0415

        d = dict(src_dict)
        categories_count = d.pop("categories_count")

        currency_info = AnalyticsCurrencyInfo.from_dict(d.pop("currencyInfo"))

        net = decimal_in(d.pop("net"))

        period = DateRange.from_dict(d.pop("period"))

        total_expenses = decimal_in(d.pop("total_expenses"))

        total_income = decimal_in(d.pop("total_income"))

        transactions_analyzed = d.pop("transactions_analyzed")

        uncategorized = UncategorizedActivity.from_dict(d.pop("uncategorized"))

        def _parse_categories(data: object) -> list[CategoryAnalyticsItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:
                    categories_type_0_item = CategoryAnalyticsItem.from_dict(categories_type_0_item_data)

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CategoryAnalyticsItem] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

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

        category_analytics_response = cls(
            categories_count=categories_count,
            currency_info=currency_info,
            net=net,
            period=period,
            total_expenses=total_expenses,
            total_income=total_income,
            transactions_analyzed=transactions_analyzed,
            uncategorized=uncategorized,
            categories=categories,
            missing_rates=missing_rates,
            pending_valuation=pending_valuation,
        )

        category_analytics_response.additional_properties = d
        return category_analytics_response

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
