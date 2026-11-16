from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="StatsDay")


@_attrs_define
class StatsDay:
    """
    Attributes:
        after_retry (int):
        day (datetime.date):
        delivered (int):
        failed (int):
        retrying (int):
        sent (int): Sent counts the deliveries made that day (at least one call): Delivered on the first call,
            `after_retry` later, Failed given up, Retrying still being retried.
        average_ms (int | None | Unset):
        max_ms (int | None | Unset):
        min_ms (int | None | Unset): `min_ms`, `average_ms`, `p95_ms` and `max_ms` are the day's calls' durations;
            absent on a day without calls.
        p95_ms (int | None | Unset):
    """

    after_retry: int
    day: datetime.date
    delivered: int
    failed: int
    retrying: int
    sent: int
    average_ms: int | None | Unset = UNSET
    max_ms: int | None | Unset = UNSET
    min_ms: int | None | Unset = UNSET
    p95_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_retry = self.after_retry

        day = self.day.isoformat()

        delivered = self.delivered

        failed = self.failed

        retrying = self.retrying

        sent = self.sent

        average_ms: int | None | Unset
        if isinstance(self.average_ms, Unset):
            average_ms = UNSET
        else:
            average_ms = self.average_ms

        max_ms: int | None | Unset
        if isinstance(self.max_ms, Unset):
            max_ms = UNSET
        else:
            max_ms = self.max_ms

        min_ms: int | None | Unset
        if isinstance(self.min_ms, Unset):
            min_ms = UNSET
        else:
            min_ms = self.min_ms

        p95_ms: int | None | Unset
        if isinstance(self.p95_ms, Unset):
            p95_ms = UNSET
        else:
            p95_ms = self.p95_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after_retry": after_retry,
                "day": day,
                "delivered": delivered,
                "failed": failed,
                "retrying": retrying,
                "sent": sent,
            }
        )
        if average_ms is not UNSET:
            field_dict["average_ms"] = average_ms
        if max_ms is not UNSET:
            field_dict["max_ms"] = max_ms
        if min_ms is not UNSET:
            field_dict["min_ms"] = min_ms
        if p95_ms is not UNSET:
            field_dict["p95_ms"] = p95_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after_retry = d.pop("after_retry")

        day = datetime.date.fromisoformat(d.pop("day"))

        delivered = d.pop("delivered")

        failed = d.pop("failed")

        retrying = d.pop("retrying")

        sent = d.pop("sent")

        def _parse_average_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        average_ms = _parse_average_ms(d.pop("average_ms", UNSET))

        def _parse_max_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ms = _parse_max_ms(d.pop("max_ms", UNSET))

        def _parse_min_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_ms = _parse_min_ms(d.pop("min_ms", UNSET))

        def _parse_p95_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        p95_ms = _parse_p95_ms(d.pop("p95_ms", UNSET))

        stats_day = cls(
            after_retry=after_retry,
            day=day,
            delivered=delivered,
            failed=failed,
            retrying=retrying,
            sent=sent,
            average_ms=average_ms,
            max_ms=max_ms,
            min_ms=min_ms,
            p95_ms=p95_ms,
        )

        stats_day.additional_properties = d
        return stats_day

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
