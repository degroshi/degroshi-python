from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.endpoint_response_disabled_reason_type_0 import check_endpoint_response_disabled_reason_type_0
from ..models.endpoint_response_disabled_reason_type_0 import EndpointResponseDisabledReasonType0
from ..models.endpoint_response_state import check_endpoint_response_state
from ..models.endpoint_response_state import EndpointResponseState
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.delivery_summary import DeliverySummary
    from ..models.endpoint_health import EndpointHealth


T = TypeVar("T", bound="EndpointResponse")


@_attrs_define
class EndpointResponse:
    """
    Attributes:
        api_version (str): APIVersion is the payload version the endpoint is pinned to.
        created_at (datetime.datetime):
        description (str):
        health (EndpointHealth):
        id (str):
        state (EndpointResponseState):
        updated_at (datetime.datetime):
        url (str):
        disabled_reason (EndpointResponseDisabledReasonType0 | None | Unset): `disabled_reason` says why a disabled
            endpoint stopped: failing (no 2xx for 3 days) or owner_left (no space left).
        events (list[str] | None | Unset):
        failing_since (datetime.datetime | None | Unset): When the run of failures began; absent while healthy.
        last_delivery (DeliverySummary | None | Unset):
        last_success_at (datetime.datetime | None | Unset):
        old_secret_until (datetime.datetime | None | Unset): When the replaced secret stops signing; absent without an
            overlap.
        space_ids (list[str] | None | Unset):
    """

    api_version: str
    created_at: datetime.datetime
    description: str
    health: EndpointHealth
    id: str
    state: EndpointResponseState
    updated_at: datetime.datetime
    url: str
    disabled_reason: EndpointResponseDisabledReasonType0 | None | Unset = UNSET
    events: list[str] | None | Unset = UNSET
    failing_since: datetime.datetime | None | Unset = UNSET
    last_delivery: DeliverySummary | None | Unset = UNSET
    last_success_at: datetime.datetime | None | Unset = UNSET
    old_secret_until: datetime.datetime | None | Unset = UNSET
    space_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.delivery_summary import DeliverySummary  # noqa: PLC0415
        from ..models.endpoint_health import EndpointHealth  # noqa: PLC0415

        api_version = self.api_version

        created_at = self.created_at.isoformat()

        description = self.description

        health = self.health.to_dict()

        id = self.id

        state: str = self.state

        updated_at = self.updated_at.isoformat()

        url = self.url

        disabled_reason: None | str | Unset
        if isinstance(self.disabled_reason, Unset):
            disabled_reason = UNSET
        elif isinstance(self.disabled_reason, str):
            disabled_reason = self.disabled_reason
        else:
            disabled_reason = self.disabled_reason

        events: list[str] | None | Unset
        if isinstance(self.events, Unset):
            events = UNSET
        elif isinstance(self.events, list):
            events = self.events

        else:
            events = self.events

        failing_since: None | str | Unset
        if isinstance(self.failing_since, Unset):
            failing_since = UNSET
        elif isinstance(self.failing_since, datetime.datetime):
            failing_since = self.failing_since.isoformat()
        else:
            failing_since = self.failing_since

        last_delivery: dict[str, Any] | None | Unset
        if isinstance(self.last_delivery, Unset):
            last_delivery = UNSET
        elif isinstance(self.last_delivery, DeliverySummary):
            last_delivery = self.last_delivery.to_dict()
        else:
            last_delivery = self.last_delivery

        last_success_at: None | str | Unset
        if isinstance(self.last_success_at, Unset):
            last_success_at = UNSET
        elif isinstance(self.last_success_at, datetime.datetime):
            last_success_at = self.last_success_at.isoformat()
        else:
            last_success_at = self.last_success_at

        old_secret_until: None | str | Unset
        if isinstance(self.old_secret_until, Unset):
            old_secret_until = UNSET
        elif isinstance(self.old_secret_until, datetime.datetime):
            old_secret_until = self.old_secret_until.isoformat()
        else:
            old_secret_until = self.old_secret_until

        space_ids: list[str] | None | Unset
        if isinstance(self.space_ids, Unset):
            space_ids = UNSET
        elif isinstance(self.space_ids, list):
            space_ids = self.space_ids

        else:
            space_ids = self.space_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_version": api_version,
                "created_at": created_at,
                "description": description,
                "health": health,
                "id": id,
                "state": state,
                "updated_at": updated_at,
                "url": url,
            }
        )
        if disabled_reason is not UNSET:
            field_dict["disabled_reason"] = disabled_reason
        if events is not UNSET:
            field_dict["events"] = events
        if failing_since is not UNSET:
            field_dict["failing_since"] = failing_since
        if last_delivery is not UNSET:
            field_dict["last_delivery"] = last_delivery
        if last_success_at is not UNSET:
            field_dict["last_success_at"] = last_success_at
        if old_secret_until is not UNSET:
            field_dict["old_secret_until"] = old_secret_until
        if space_ids is not UNSET:
            field_dict["space_ids"] = space_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delivery_summary import DeliverySummary  # noqa: PLC0415
        from ..models.endpoint_health import EndpointHealth  # noqa: PLC0415

        d = dict(src_dict)
        api_version = d.pop("api_version")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        health = EndpointHealth.from_dict(d.pop("health"))

        id = d.pop("id")

        state = check_endpoint_response_state(d.pop("state"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        url = d.pop("url")

        def _parse_disabled_reason(data: object) -> EndpointResponseDisabledReasonType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disabled_reason_type_0 = check_endpoint_response_disabled_reason_type_0(data)

                return disabled_reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointResponseDisabledReasonType0 | None | Unset, data)

        disabled_reason = _parse_disabled_reason(d.pop("disabled_reason", UNSET))

        def _parse_events(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = cast(list[str], data)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        events = _parse_events(d.pop("events", UNSET))

        def _parse_failing_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failing_since_type_0 = datetime.datetime.fromisoformat(data)

                return failing_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        failing_since = _parse_failing_since(d.pop("failing_since", UNSET))

        def _parse_last_delivery(data: object) -> DeliverySummary | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_delivery_type_0 = DeliverySummary.from_dict(data)

                return last_delivery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeliverySummary | None | Unset, data)

        last_delivery = _parse_last_delivery(d.pop("last_delivery", UNSET))

        def _parse_last_success_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_success_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_success_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_success_at = _parse_last_success_at(d.pop("last_success_at", UNSET))

        def _parse_old_secret_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                old_secret_until_type_0 = datetime.datetime.fromisoformat(data)

                return old_secret_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        old_secret_until = _parse_old_secret_until(d.pop("old_secret_until", UNSET))

        def _parse_space_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                space_ids_type_0 = cast(list[str], data)

                return space_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        space_ids = _parse_space_ids(d.pop("space_ids", UNSET))

        endpoint_response = cls(
            api_version=api_version,
            created_at=created_at,
            description=description,
            health=health,
            id=id,
            state=state,
            updated_at=updated_at,
            url=url,
            disabled_reason=disabled_reason,
            events=events,
            failing_since=failing_since,
            last_delivery=last_delivery,
            last_success_at=last_success_at,
            old_secret_until=old_secret_until,
            space_ids=space_ids,
        )

        endpoint_response.additional_properties = d
        return endpoint_response

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
