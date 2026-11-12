from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.error_body_details_type_0 import ErrorBodyDetailsType0


T = TypeVar("T", bound="ErrorBody")


@_attrs_define
class ErrorBody:
    """
    Attributes:
        code (str): Machine-readable error code (see x-error-codes)
        message (str): Human-readable error message describing the specific error
        correlation_id (None | str | Unset): Request correlation id; include it in bug reports
        details (ErrorBodyDetailsType0 | None | Unset): Additional error context
    """

    code: str
    message: str
    correlation_id: None | str | Unset = UNSET
    details: ErrorBodyDetailsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_body_details_type_0 import ErrorBodyDetailsType0  # noqa: PLC0415

        code = self.code

        message = self.message

        correlation_id: None | str | Unset
        if isinstance(self.correlation_id, Unset):
            correlation_id = UNSET
        else:
            correlation_id = self.correlation_id

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, ErrorBodyDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if correlation_id is not UNSET:
            field_dict["correlation_id"] = correlation_id
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_body_details_type_0 import ErrorBodyDetailsType0  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        def _parse_correlation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        correlation_id = _parse_correlation_id(d.pop("correlation_id", UNSET))

        def _parse_details(data: object) -> ErrorBodyDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = ErrorBodyDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ErrorBodyDetailsType0 | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        error_body = cls(
            code=code,
            message=message,
            correlation_id=correlation_id,
            details=details,
        )

        error_body.additional_properties = d
        return error_body

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
