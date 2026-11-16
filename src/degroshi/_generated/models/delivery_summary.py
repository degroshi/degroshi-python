from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.delivery_summary_status import check_delivery_summary_status
from ..models.delivery_summary_status import DeliverySummaryStatus
from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="DeliverySummary")


@_attrs_define
class DeliverySummary:
    """
    Attributes:
        attempts (int): Attempts counts the calls so far.
        created_at (datetime.datetime):
        event_id (str):
        id (str):
        status (DeliverySummaryStatus):
        test (bool): Test marks a test event (POST /v1/webhooks/{id}/test).
        type_ (str):
        delivered_at (datetime.datetime | None | Unset): When a 2xx came back.
        error (None | str | Unset):
        http_status (int | None | Unset): HTTPStatus is the last answer's status; absent when the call got none (a
            timeout, DNS, TLS).
        latency_ms (int | None | Unset):
        next_attempt_at (datetime.datetime | None | Unset): When a pending delivery is tried again.
    """

    attempts: int
    created_at: datetime.datetime
    event_id: str
    id: str
    status: DeliverySummaryStatus
    test: bool
    type_: str
    delivered_at: datetime.datetime | None | Unset = UNSET
    error: None | str | Unset = UNSET
    http_status: int | None | Unset = UNSET
    latency_ms: int | None | Unset = UNSET
    next_attempt_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        created_at = self.created_at.isoformat()

        event_id = self.event_id

        id = self.id

        status: str = self.status

        test = self.test

        type_ = self.type_

        delivered_at: None | str | Unset
        if isinstance(self.delivered_at, Unset):
            delivered_at = UNSET
        elif isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        http_status: int | None | Unset
        if isinstance(self.http_status, Unset):
            http_status = UNSET
        else:
            http_status = self.http_status

        latency_ms: int | None | Unset
        if isinstance(self.latency_ms, Unset):
            latency_ms = UNSET
        else:
            latency_ms = self.latency_ms

        next_attempt_at: None | str | Unset
        if isinstance(self.next_attempt_at, Unset):
            next_attempt_at = UNSET
        elif isinstance(self.next_attempt_at, datetime.datetime):
            next_attempt_at = self.next_attempt_at.isoformat()
        else:
            next_attempt_at = self.next_attempt_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempts": attempts,
                "created_at": created_at,
                "event_id": event_id,
                "id": id,
                "status": status,
                "test": test,
                "type": type_,
            }
        )
        if delivered_at is not UNSET:
            field_dict["delivered_at"] = delivered_at
        if error is not UNSET:
            field_dict["error"] = error
        if http_status is not UNSET:
            field_dict["http_status"] = http_status
        if latency_ms is not UNSET:
            field_dict["latency_ms"] = latency_ms
        if next_attempt_at is not UNSET:
            field_dict["next_attempt_at"] = next_attempt_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_id = d.pop("event_id")

        id = d.pop("id")

        status = check_delivery_summary_status(d.pop("status"))

        test = d.pop("test")

        type_ = d.pop("type")

        def _parse_delivered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_http_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_status = _parse_http_status(d.pop("http_status", UNSET))

        def _parse_latency_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latency_ms = _parse_latency_ms(d.pop("latency_ms", UNSET))

        def _parse_next_attempt_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at", UNSET))

        delivery_summary = cls(
            attempts=attempts,
            created_at=created_at,
            event_id=event_id,
            id=id,
            status=status,
            test=test,
            type_=type_,
            delivered_at=delivered_at,
            error=error,
            http_status=http_status,
            latency_ms=latency_ms,
            next_attempt_at=next_attempt_at,
        )

        delivery_summary.additional_properties = d
        return delivery_summary

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
