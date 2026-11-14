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
    from ..models.category_summary import CategorySummary
    from ..models.date_range import DateRange


T = TypeVar("T", bound="SummaryResponse")


@_attrs_define
class SummaryResponse:
    """
    Attributes:
        currency_info (AnalyticsCurrencyInfo):
        net_savings (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        period (DateRange):
        savings_rate (float):
        total_expenses (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        total_income (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        transaction_count (int):
        missing_rates (list[str] | None | Unset): `missing_rates` lists currencies whose amounts could not be converted
            into the response currency (no exchange rate available). Those amounts are excluded from the totals above;
            empty/omitted when everything converted.
        pending_valuation (int | None | Unset): `pending_valuation` counts the business-space transactions of the period
            that have no UAH value yet (the NBU rate of their legal date is not published, or the valuation has not run):
            they are left out of the totals above until valued. Omitted when 0 and in personal spaces.
        top_expense_category (CategorySummary | None | Unset):
    """

    currency_info: AnalyticsCurrencyInfo
    net_savings: Decimal
    period: DateRange
    savings_rate: float
    total_expenses: Decimal
    total_income: Decimal
    transaction_count: int
    missing_rates: list[str] | None | Unset = UNSET
    pending_valuation: int | None | Unset = UNSET
    top_expense_category: CategorySummary | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.category_summary import CategorySummary  # noqa: PLC0415
        from ..models.date_range import DateRange  # noqa: PLC0415

        currency_info = self.currency_info.to_dict()

        net_savings = decimal_out(self.net_savings)

        period = self.period.to_dict()

        savings_rate = self.savings_rate

        total_expenses = decimal_out(self.total_expenses)

        total_income = decimal_out(self.total_income)

        transaction_count = self.transaction_count

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

        top_expense_category: dict[str, Any] | None | Unset
        if isinstance(self.top_expense_category, Unset):
            top_expense_category = UNSET
        elif isinstance(self.top_expense_category, CategorySummary):
            top_expense_category = self.top_expense_category.to_dict()
        else:
            top_expense_category = self.top_expense_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyInfo": currency_info,
                "net_savings": net_savings,
                "period": period,
                "savings_rate": savings_rate,
                "total_expenses": total_expenses,
                "total_income": total_income,
                "transaction_count": transaction_count,
            }
        )
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates
        if pending_valuation is not UNSET:
            field_dict["pending_valuation"] = pending_valuation
        if top_expense_category is not UNSET:
            field_dict["top_expense_category"] = top_expense_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.category_summary import CategorySummary  # noqa: PLC0415
        from ..models.date_range import DateRange  # noqa: PLC0415

        d = dict(src_dict)
        currency_info = AnalyticsCurrencyInfo.from_dict(d.pop("currencyInfo"))

        net_savings = decimal_in(d.pop("net_savings"))

        period = DateRange.from_dict(d.pop("period"))

        savings_rate = d.pop("savings_rate")

        total_expenses = decimal_in(d.pop("total_expenses"))

        total_income = decimal_in(d.pop("total_income"))

        transaction_count = d.pop("transaction_count")

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

        def _parse_top_expense_category(data: object) -> CategorySummary | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                top_expense_category_type_0 = CategorySummary.from_dict(data)

                return top_expense_category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CategorySummary | None | Unset, data)

        top_expense_category = _parse_top_expense_category(d.pop("top_expense_category", UNSET))

        summary_response = cls(
            currency_info=currency_info,
            net_savings=net_savings,
            period=period,
            savings_rate=savings_rate,
            total_expenses=total_expenses,
            total_income=total_income,
            transaction_count=transaction_count,
            missing_rates=missing_rates,
            pending_valuation=pending_valuation,
            top_expense_category=top_expense_category,
        )

        summary_response.additional_properties = d
        return summary_response

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
