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


T = TypeVar("T", bound="BudgetListItem")


@_attrs_define
class BudgetListItem:
    """
    Attributes:
        created_at (datetime.datetime):
        currency (str):
        id (str):
        is_active (bool):
        name (str):
        period (BudgetPeriod):
        period_end (datetime.datetime):
        period_start (datetime.datetime): / PeriodEnd are the inclusive calendar dates (space timezone) of the current
            period, or of the period containing as_of.
        space_id (str):
        start_date (datetime.datetime):
        alerts_muted (bool | None | Unset): Whether you muted this budget's alerts.
        end_date (datetime.datetime | None | Unset):
        total_limit (None | Decimal | Unset): The budget's one amount for all spending, null when it is the sum of its
            allocations.
        version (int | None | Unset): The budget row version (also the ETag of single-budget responses): send it as If-
            Match on PATCH / DELETE.
    """

    created_at: datetime.datetime
    currency: str
    id: str
    is_active: bool
    name: str
    period: BudgetPeriod
    period_end: datetime.datetime
    period_start: datetime.datetime
    space_id: str
    start_date: datetime.datetime
    alerts_muted: bool | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    total_limit: None | Decimal | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        currency = self.currency

        id = self.id

        is_active = self.is_active

        name = self.name

        period: str = self.period

        period_end = self.period_end.isoformat()

        period_start = self.period_start.isoformat()

        space_id = self.space_id

        start_date = self.start_date.isoformat()

        alerts_muted: bool | None | Unset
        if isinstance(self.alerts_muted, Unset):
            alerts_muted = UNSET
        else:
            alerts_muted = self.alerts_muted

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

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
                "created_at": created_at,
                "currency": currency,
                "id": id,
                "is_active": is_active,
                "name": name,
                "period": period,
                "period_end": period_end,
                "period_start": period_start,
                "space_id": space_id,
                "start_date": start_date,
            }
        )
        if alerts_muted is not UNSET:
            field_dict["alerts_muted"] = alerts_muted
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if total_limit is not UNSET:
            field_dict["total_limit"] = total_limit
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency = d.pop("currency")

        id = d.pop("id")

        is_active = d.pop("is_active")

        name = d.pop("name")

        period = check_budget_period(d.pop("period"))

        period_end = datetime.datetime.fromisoformat(d.pop("period_end"))

        period_start = datetime.datetime.fromisoformat(d.pop("period_start"))

        space_id = d.pop("space_id")

        start_date = datetime.datetime.fromisoformat(d.pop("start_date"))

        def _parse_alerts_muted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        alerts_muted = _parse_alerts_muted(d.pop("alerts_muted", UNSET))

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

        budget_list_item = cls(
            created_at=created_at,
            currency=currency,
            id=id,
            is_active=is_active,
            name=name,
            period=period,
            period_end=period_end,
            period_start=period_start,
            space_id=space_id,
            start_date=start_date,
            alerts_muted=alerts_muted,
            end_date=end_date,
            total_limit=total_limit,
            version=version,
        )

        budget_list_item.additional_properties = d
        return budget_list_item

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
