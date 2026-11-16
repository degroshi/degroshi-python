from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.endpoint_response import EndpointResponse


T = TypeVar("T", bound="CreatedEndpointResponse")


@_attrs_define
class CreatedEndpointResponse:
    """
    Attributes:
        endpoint (EndpointResponse):
        secret (str): Secret signs every delivery (Degroshi-Signature). The app can show it again later; an API key can
            only rotate it.
    """

    endpoint: EndpointResponse
    secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.endpoint_response import EndpointResponse  # noqa: PLC0415

        endpoint = self.endpoint.to_dict()

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_response import EndpointResponse  # noqa: PLC0415

        d = dict(src_dict)
        endpoint = EndpointResponse.from_dict(d.pop("endpoint"))

        secret = d.pop("secret")

        created_endpoint_response = cls(
            endpoint=endpoint,
            secret=secret,
        )

        created_endpoint_response.additional_properties = d
        return created_endpoint_response

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
