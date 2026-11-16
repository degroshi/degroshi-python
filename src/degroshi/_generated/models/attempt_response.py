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
    from ..models.attempt_response_response_headers_type_0 import AttemptResponseResponseHeadersType0


T = TypeVar("T", bound="AttemptResponse")


@_attrs_define
class AttemptResponse:
    """
    Attributes:
        duration_ms (int):
        n (int):
        response_body (str): The answer's first 4 KB.
        started_at (datetime.datetime):
        error (None | str | Unset):
        http_status (int | None | Unset):
        response_headers (AttemptResponseResponseHeadersType0 | None | Unset): The answer's first 20 headers.
    """

    duration_ms: int
    n: int
    response_body: str
    started_at: datetime.datetime
    error: None | str | Unset = UNSET
    http_status: int | None | Unset = UNSET
    response_headers: AttemptResponseResponseHeadersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attempt_response_response_headers_type_0 import AttemptResponseResponseHeadersType0  # noqa: PLC0415

        duration_ms = self.duration_ms

        n = self.n

        response_body = self.response_body

        started_at = self.started_at.isoformat()

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

        response_headers: dict[str, Any] | None | Unset
        if isinstance(self.response_headers, Unset):
            response_headers = UNSET
        elif isinstance(self.response_headers, AttemptResponseResponseHeadersType0):
            response_headers = self.response_headers.to_dict()
        else:
            response_headers = self.response_headers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration_ms": duration_ms,
                "n": n,
                "response_body": response_body,
                "started_at": started_at,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if http_status is not UNSET:
            field_dict["http_status"] = http_status
        if response_headers is not UNSET:
            field_dict["response_headers"] = response_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attempt_response_response_headers_type_0 import AttemptResponseResponseHeadersType0  # noqa: PLC0415

        d = dict(src_dict)
        duration_ms = d.pop("duration_ms")

        n = d.pop("n")

        response_body = d.pop("response_body")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

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

        def _parse_response_headers(data: object) -> AttemptResponseResponseHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_headers_type_0 = AttemptResponseResponseHeadersType0.from_dict(data)

                return response_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttemptResponseResponseHeadersType0 | None | Unset, data)

        response_headers = _parse_response_headers(d.pop("response_headers", UNSET))

        attempt_response = cls(
            duration_ms=duration_ms,
            n=n,
            response_body=response_body,
            started_at=started_at,
            error=error,
            http_status=http_status,
            response_headers=response_headers,
        )

        attempt_response.additional_properties = d
        return attempt_response

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
