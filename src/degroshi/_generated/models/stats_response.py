from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.stats_day import StatsDay
    from ..models.stats_figures import StatsFigures


T = TypeVar("T", bound="StatsResponse")


@_attrs_define
class StatsResponse:
    """
    Attributes:
        from_ (datetime.date):
        to (datetime.date):
        total (StatsFigures):
        days (list[StatsDay] | None | Unset):
    """

    from_: datetime.date
    to: datetime.date
    total: StatsFigures
    days: list[StatsDay] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.stats_day import StatsDay  # noqa: PLC0415
        from ..models.stats_figures import StatsFigures  # noqa: PLC0415

        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        total = self.total.to_dict()

        days: list[dict[str, Any]] | None | Unset
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = []
            for days_type_0_item_data in self.days:
                days_type_0_item = days_type_0_item_data.to_dict()
                days.append(days_type_0_item)

        else:
            days = self.days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "total": total,
            }
        )
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stats_day import StatsDay  # noqa: PLC0415
        from ..models.stats_figures import StatsFigures  # noqa: PLC0415

        d = dict(src_dict)
        from_ = datetime.date.fromisoformat(d.pop("from"))

        to = datetime.date.fromisoformat(d.pop("to"))

        total = StatsFigures.from_dict(d.pop("total"))

        def _parse_days(data: object) -> list[StatsDay] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = []
                _days_type_0 = data
                for days_type_0_item_data in _days_type_0:
                    days_type_0_item = StatsDay.from_dict(days_type_0_item_data)

                    days_type_0.append(days_type_0_item)

                return days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StatsDay] | None | Unset, data)

        days = _parse_days(d.pop("days", UNSET))

        stats_response = cls(
            from_=from_,
            to=to,
            total=total,
            days=days,
        )

        stats_response.additional_properties = d
        return stats_response

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
