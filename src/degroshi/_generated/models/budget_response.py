from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.budget_period import BudgetPeriod
from ..models.budget_period import check_budget_period
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.budget_allocation_response import BudgetAllocationResponse
    from ..models.budget_display import BudgetDisplay


T = TypeVar("T", bound="BudgetResponse")


@_attrs_define
class BudgetResponse:
    """
    Attributes:
        allocations (list[BudgetAllocationResponse]):
        created_at (datetime.datetime):
        currency (str):
        id (str):
        is_active (bool):
        name (str):
        period (BudgetPeriod):
        period_end (datetime.datetime):
        period_start (datetime.datetime): `period_start` / `period_end` are the inclusive calendar dates (space
            timezone) of the evaluated period: the current one, or the one containing the as_of query date.
        progress (float):
        remaining (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        space_id (str):
        start_date (datetime.datetime):
        total_budget (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        total_spent (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        alerts_muted (bool | None | Unset): Whether you muted this budget's alerts.
        display (BudgetDisplay | None | Unset): The totals in the display currency the device sent (X-Display-Currency),
            converted at today's rate; null when that is the budget currency, none was sent or there is no rate. Clients
            show it first and the budget's own figures as the second line.
        end_date (datetime.datetime | None | Unset):
        missing_rates (list[str] | None | Unset): `missing_rates` lists spending currencies without an exchange rate
            into the budget currency; that spending is excluded from total_spent.
        total_limit (None | Decimal | Unset): The budget's one amount for all spending (null: the budget is the sum of its
            allocations). When set, total_budget is this amount and total_spent every expense of the space in the period,
            net of refunds; the allocations are inner limits.
        version (int | None | Unset): The budget row version (also the ETag): send it as If-Match on PATCH / DELETE to
            detect concurrent edits (412).
    """

    allocations: list[BudgetAllocationResponse]
    created_at: datetime.datetime
    currency: str
    id: str
    is_active: bool
    name: str
    period: BudgetPeriod
    period_end: datetime.datetime
    period_start: datetime.datetime
    progress: float
    remaining: Decimal
    space_id: str
    start_date: datetime.datetime
    total_budget: Decimal
    total_spent: Decimal
    alerts_muted: bool | None | Unset = UNSET
    display: BudgetDisplay | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    missing_rates: list[str] | None | Unset = UNSET
    total_limit: None | Decimal | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.budget_allocation_response import BudgetAllocationResponse  # noqa: PLC0415
        from ..models.budget_display import BudgetDisplay  # noqa: PLC0415

        allocations = []
        for allocations_item_data in self.allocations:
            allocations_item = allocations_item_data.to_dict()
            allocations.append(allocations_item)

        created_at = self.created_at.isoformat()

        currency = self.currency

        id = self.id

        is_active = self.is_active

        name = self.name

        period: str = self.period

        period_end = self.period_end.isoformat()

        period_start = self.period_start.isoformat()

        progress = self.progress

        remaining = decimal_out(self.remaining)

        space_id = self.space_id

        start_date = self.start_date.isoformat()

        total_budget = decimal_out(self.total_budget)

        total_spent = decimal_out(self.total_spent)

        alerts_muted: bool | None | Unset
        if isinstance(self.alerts_muted, Unset):
            alerts_muted = UNSET
        else:
            alerts_muted = self.alerts_muted

        display: dict[str, Any] | None | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        elif isinstance(self.display, BudgetDisplay):
            display = self.display.to_dict()
        else:
            display = self.display

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        missing_rates: list[str] | None | Unset
        if isinstance(self.missing_rates, Unset):
            missing_rates = UNSET
        elif isinstance(self.missing_rates, list):
            missing_rates = self.missing_rates

        else:
            missing_rates = self.missing_rates

        total_limit: None | Decimal | Unset
        if isinstance(self.total_limit, Unset):
            total_limit = UNSET
        else:
            total_limit = decimal_out(self.total_limit)

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allocations": allocations,
                "created_at": created_at,
                "currency": currency,
                "id": id,
                "is_active": is_active,
                "name": name,
                "period": period,
                "period_end": period_end,
                "period_start": period_start,
                "progress": progress,
                "remaining": remaining,
                "space_id": space_id,
                "start_date": start_date,
                "total_budget": total_budget,
                "total_spent": total_spent,
            }
        )
        if alerts_muted is not UNSET:
            field_dict["alerts_muted"] = alerts_muted
        if display is not UNSET:
            field_dict["display"] = display
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates
        if total_limit is not UNSET:
            field_dict["total_limit"] = total_limit
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_allocation_response import BudgetAllocationResponse  # noqa: PLC0415
        from ..models.budget_display import BudgetDisplay  # noqa: PLC0415

        d = dict(src_dict)
        allocations = []
        _allocations = d.pop("allocations")
        for allocations_item_data in _allocations:
            allocations_item = BudgetAllocationResponse.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency = d.pop("currency")

        id = d.pop("id")

        is_active = d.pop("is_active")

        name = d.pop("name")

        period = check_budget_period(d.pop("period"))

        period_end = datetime.datetime.fromisoformat(d.pop("period_end"))

        period_start = datetime.datetime.fromisoformat(d.pop("period_start"))

        progress = d.pop("progress")

        remaining = decimal_in(d.pop("remaining"))

        space_id = d.pop("space_id")

        start_date = datetime.datetime.fromisoformat(d.pop("start_date"))

        total_budget = decimal_in(d.pop("total_budget"))

        total_spent = decimal_in(d.pop("total_spent"))

        def _parse_alerts_muted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        alerts_muted = _parse_alerts_muted(d.pop("alerts_muted", UNSET))

        def _parse_display(data: object) -> BudgetDisplay | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_type_0 = BudgetDisplay.from_dict(data)

                return display_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BudgetDisplay | None | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.datetime.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

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

        def _parse_total_limit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_limit = decimal_in(_parse_total_limit(d.pop("total_limit", UNSET)))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        budget_response = cls(
            allocations=allocations,
            created_at=created_at,
            currency=currency,
            id=id,
            is_active=is_active,
            name=name,
            period=period,
            period_end=period_end,
            period_start=period_start,
            progress=progress,
            remaining=remaining,
            space_id=space_id,
            start_date=start_date,
            total_budget=total_budget,
            total_spent=total_spent,
            alerts_muted=alerts_muted,
            display=display,
            end_date=end_date,
            missing_rates=missing_rates,
            total_limit=total_limit,
            version=version,
        )

        budget_response.additional_properties = d
        return budget_response

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
