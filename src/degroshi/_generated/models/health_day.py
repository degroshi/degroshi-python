from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="HealthDay")


@_attrs_define
class HealthDay:
    """
    Attributes:
        day (datetime.date):
        failed (int):
        sent (int):
        p95_latency_ms (int | None | Unset):
    """

    day: datetime.date
    failed: int
    sent: int
    p95_latency_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day.isoformat()

        failed = self.failed

        sent = self.sent

        p95_latency_ms: int | None | Unset
        if isinstance(self.p95_latency_ms, Unset):
            p95_latency_ms = UNSET
        else:
            p95_latency_ms = self.p95_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "failed": failed,
                "sent": sent,
            }
        )
        if p95_latency_ms is not UNSET:
            field_dict["p95_latency_ms"] = p95_latency_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = datetime.date.fromisoformat(d.pop("day"))

        failed = d.pop("failed")

        sent = d.pop("sent")

        def _parse_p95_latency_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        p95_latency_ms = _parse_p95_latency_ms(d.pop("p95_latency_ms", UNSET))

        health_day = cls(
            day=day,
            failed=failed,
            sent=sent,
            p95_latency_ms=p95_latency_ms,
        )

        health_day.additional_properties = d
        return health_day

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
