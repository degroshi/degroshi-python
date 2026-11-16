from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.health_day import HealthDay


T = TypeVar("T", bound="EndpointHealth")


@_attrs_define
class EndpointHealth:
    """
    Attributes:
        sent_24h (int): Sent24h counts deliveries finished or still retrying in the last 24 hours; Succeeded24h those
            that got a 2xx.
        sent_7d (int):
        succeeded_24h (int):
        succeeded_7d (int):
        days (list[HealthDay] | None | Unset): The last 7 days in the person's zone, oldest first, for the list's
            sparklines.
        p95_latency_ms_24h (int | None | Unset): The 95th percentile of the attempts' durations in the last 24 hours;
            absent without any.
    """

    sent_24h: int
    sent_7d: int
    succeeded_24h: int
    succeeded_7d: int
    days: list[HealthDay] | None | Unset = UNSET
    p95_latency_ms_24h: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.health_day import HealthDay  # noqa: PLC0415

        sent_24h = self.sent_24h

        sent_7d = self.sent_7d

        succeeded_24h = self.succeeded_24h

        succeeded_7d = self.succeeded_7d

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

        p95_latency_ms_24h: int | None | Unset
        if isinstance(self.p95_latency_ms_24h, Unset):
            p95_latency_ms_24h = UNSET
        else:
            p95_latency_ms_24h = self.p95_latency_ms_24h

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sent_24h": sent_24h,
                "sent_7d": sent_7d,
                "succeeded_24h": succeeded_24h,
                "succeeded_7d": succeeded_7d,
            }
        )
        if days is not UNSET:
            field_dict["days"] = days
        if p95_latency_ms_24h is not UNSET:
            field_dict["p95_latency_ms_24h"] = p95_latency_ms_24h

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_day import HealthDay  # noqa: PLC0415

        d = dict(src_dict)
        sent_24h = d.pop("sent_24h")

        sent_7d = d.pop("sent_7d")

        succeeded_24h = d.pop("succeeded_24h")

        succeeded_7d = d.pop("succeeded_7d")

        def _parse_days(data: object) -> list[HealthDay] | None | Unset:
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
                    days_type_0_item = HealthDay.from_dict(days_type_0_item_data)

                    days_type_0.append(days_type_0_item)

                return days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HealthDay] | None | Unset, data)

        days = _parse_days(d.pop("days", UNSET))

        def _parse_p95_latency_ms_24h(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        p95_latency_ms_24h = _parse_p95_latency_ms_24h(d.pop("p95_latency_ms_24h", UNSET))

        endpoint_health = cls(
            sent_24h=sent_24h,
            sent_7d=sent_7d,
            succeeded_24h=succeeded_24h,
            succeeded_7d=succeeded_7d,
            days=days,
            p95_latency_ms_24h=p95_latency_ms_24h,
        )

        endpoint_health.additional_properties = d
        return endpoint_health

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
