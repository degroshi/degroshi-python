from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.attempt_response import AttemptResponse
    from ..models.delivery_request import DeliveryRequest
    from ..models.delivery_summary import DeliverySummary


T = TypeVar("T", bound="DeliveryDetail")


@_attrs_define
class DeliveryDetail:
    """
    Attributes:
        delivery (DeliverySummary):
        request (DeliveryRequest):
        attempt_log (list[AttemptResponse] | None | Unset):
    """

    delivery: DeliverySummary
    request: DeliveryRequest
    attempt_log: list[AttemptResponse] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attempt_response import AttemptResponse  # noqa: PLC0415
        from ..models.delivery_request import DeliveryRequest  # noqa: PLC0415
        from ..models.delivery_summary import DeliverySummary  # noqa: PLC0415

        delivery = self.delivery.to_dict()

        request = self.request.to_dict()

        attempt_log: list[dict[str, Any]] | None | Unset
        if isinstance(self.attempt_log, Unset):
            attempt_log = UNSET
        elif isinstance(self.attempt_log, list):
            attempt_log = []
            for attempt_log_type_0_item_data in self.attempt_log:
                attempt_log_type_0_item = attempt_log_type_0_item_data.to_dict()
                attempt_log.append(attempt_log_type_0_item)

        else:
            attempt_log = self.attempt_log

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delivery": delivery,
                "request": request,
            }
        )
        if attempt_log is not UNSET:
            field_dict["attempt_log"] = attempt_log

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attempt_response import AttemptResponse  # noqa: PLC0415
        from ..models.delivery_request import DeliveryRequest  # noqa: PLC0415
        from ..models.delivery_summary import DeliverySummary  # noqa: PLC0415

        d = dict(src_dict)
        delivery = DeliverySummary.from_dict(d.pop("delivery"))

        request = DeliveryRequest.from_dict(d.pop("request"))

        def _parse_attempt_log(data: object) -> list[AttemptResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attempt_log_type_0 = []
                _attempt_log_type_0 = data
                for attempt_log_type_0_item_data in _attempt_log_type_0:
                    attempt_log_type_0_item = AttemptResponse.from_dict(attempt_log_type_0_item_data)

                    attempt_log_type_0.append(attempt_log_type_0_item)

                return attempt_log_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AttemptResponse] | None | Unset, data)

        attempt_log = _parse_attempt_log(d.pop("attempt_log", UNSET))

        delivery_detail = cls(
            delivery=delivery,
            request=request,
            attempt_log=attempt_log,
        )

        delivery_detail.additional_properties = d
        return delivery_detail

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
