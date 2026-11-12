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
    from ..models.cash_flow_point import CashFlowPoint


T = TypeVar("T", bound="CashFlowResponse")


@_attrs_define
class CashFlowResponse:
    """
    Attributes:
        avg_monthly_expenses (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        avg_monthly_income (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        currency_info (AnalyticsCurrencyInfo):
        total_expenses (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        total_income (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        missing_rates (list[str] | None | Unset): Lists currencies whose amounts could not be converted into the
            response currency (no exchange rate available). Those amounts are excluded from the totals above; empty/omitted
            when everything converted.
        pending_valuation (int | None | Unset): Counts the business-space transactions of the period that have no UAH
            value yet (the NBU rate of their legal date is not published, or the valuation has not run): they are left out
            of the totals above until valued. Omitted when 0 and in personal spaces.
        points (list[CashFlowPoint] | None | Unset):
    """

    avg_monthly_expenses: Decimal
    avg_monthly_income: Decimal
    currency_info: AnalyticsCurrencyInfo
    total_expenses: Decimal
    total_income: Decimal
    missing_rates: list[str] | None | Unset = UNSET
    pending_valuation: int | None | Unset = UNSET
    points: list[CashFlowPoint] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.cash_flow_point import CashFlowPoint  # noqa: PLC0415

        avg_monthly_expenses = decimal_out(self.avg_monthly_expenses)

        avg_monthly_income = decimal_out(self.avg_monthly_income)

        currency_info = self.currency_info.to_dict()

        total_expenses = decimal_out(self.total_expenses)

        total_income = decimal_out(self.total_income)

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

        points: list[dict[str, Any]] | None | Unset
        if isinstance(self.points, Unset):
            points = UNSET
        elif isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)

        else:
            points = self.points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avg_monthly_expenses": avg_monthly_expenses,
                "avg_monthly_income": avg_monthly_income,
                "currencyInfo": currency_info,
                "total_expenses": total_expenses,
                "total_income": total_income,
            }
        )
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates
        if pending_valuation is not UNSET:
            field_dict["pending_valuation"] = pending_valuation
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.cash_flow_point import CashFlowPoint  # noqa: PLC0415

        d = dict(src_dict)
        avg_monthly_expenses = decimal_in(d.pop("avg_monthly_expenses"))

        avg_monthly_income = decimal_in(d.pop("avg_monthly_income"))

        currency_info = AnalyticsCurrencyInfo.from_dict(d.pop("currencyInfo"))

        total_expenses = decimal_in(d.pop("total_expenses"))

        total_income = decimal_in(d.pop("total_income"))

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

        def _parse_points(data: object) -> list[CashFlowPoint] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = CashFlowPoint.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CashFlowPoint] | None | Unset, data)

        points = _parse_points(d.pop("points", UNSET))

        cash_flow_response = cls(
            avg_monthly_expenses=avg_monthly_expenses,
            avg_monthly_income=avg_monthly_income,
            currency_info=currency_info,
            total_expenses=total_expenses,
            total_income=total_income,
            missing_rates=missing_rates,
            pending_valuation=pending_valuation,
            points=points,
        )

        cash_flow_response.additional_properties = d
        return cash_flow_response

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
