from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.push_item_result_status import check_push_item_result_status
from ..models.push_item_result_status import PushItemResultStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.push_item_error import PushItemError


T = TypeVar("T", bound="PushItemResult")


@_attrs_define
class PushItemResult:
    """
    Attributes:
        external_id (str):
        status (PushItemResultStatus): Created, updated, unchanged, deleted or failed.
        error (None | PushItemError | Unset):
        id (None | str | Unset): The transaction's id in Degroshi (absent when failed).
    """

    external_id: str
    status: PushItemResultStatus
    error: None | PushItemError | Unset = UNSET
    id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.push_item_error import PushItemError  # noqa: PLC0415

        external_id = self.external_id

        status: str = self.status

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, PushItemError):
            error = self.error.to_dict()
        else:
            error = self.error

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.push_item_error import PushItemError  # noqa: PLC0415

        d = dict(src_dict)
        external_id = d.pop("external_id")

        status = check_push_item_result_status(d.pop("status"))

        def _parse_error(data: object) -> None | PushItemError | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = PushItemError.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PushItemError | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        push_item_result = cls(
            external_id=external_id,
            status=status,
            error=error,
            id=id,
        )

        push_item_result.additional_properties = d
        return push_item_result

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
