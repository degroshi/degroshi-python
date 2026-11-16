from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.delivery_request_body_type_0 import DeliveryRequestBodyType0
    from ..models.delivery_request_headers_type_0 import DeliveryRequestHeadersType0


T = TypeVar("T", bound="DeliveryRequest")


@_attrs_define
class DeliveryRequest:
    """
    Attributes:
        url (str):
        body (DeliveryRequestBodyType0 | None | Unset):
        headers (DeliveryRequestHeadersType0 | None | Unset):
    """

    url: str
    body: DeliveryRequestBodyType0 | None | Unset = UNSET
    headers: DeliveryRequestHeadersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.delivery_request_body_type_0 import DeliveryRequestBodyType0  # noqa: PLC0415
        from ..models.delivery_request_headers_type_0 import DeliveryRequestHeadersType0  # noqa: PLC0415

        url = self.url

        body: dict[str, Any] | None | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        elif isinstance(self.body, DeliveryRequestBodyType0):
            body = self.body.to_dict()
        else:
            body = self.body

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, DeliveryRequestHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delivery_request_body_type_0 import DeliveryRequestBodyType0  # noqa: PLC0415
        from ..models.delivery_request_headers_type_0 import DeliveryRequestHeadersType0  # noqa: PLC0415

        d = dict(src_dict)
        url = d.pop("url")

        def _parse_body(data: object) -> DeliveryRequestBodyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                body_type_0 = DeliveryRequestBodyType0.from_dict(data)

                return body_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeliveryRequestBodyType0 | None | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        def _parse_headers(data: object) -> DeliveryRequestHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = DeliveryRequestHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeliveryRequestHeadersType0 | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        delivery_request = cls(
            url=url,
            body=body,
            headers=headers,
        )

        delivery_request.additional_properties = d
        return delivery_request

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
