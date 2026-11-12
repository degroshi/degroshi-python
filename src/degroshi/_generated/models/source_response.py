from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sources_kind import check_sources_kind
from ..models.sources_kind import SourcesKind
from ..models.status import check_status
from ..models.status import Status
from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="SourceResponse")


@_attrs_define
class SourceResponse:
    """
    Attributes:
        account_count (int):
        created_at (datetime.datetime):
        created_by (str):
        id (str):
        is_read_only (bool):
        kind (SourcesKind):
        name (str):
        status (Status):
        updated_at (datetime.datetime):
        last_push_at (datetime.datetime | None | Unset): When the source last pushed transactions or balances; absent
            before the first push.
    """

    account_count: int
    created_at: datetime.datetime
    created_by: str
    id: str
    is_read_only: bool
    kind: SourcesKind
    name: str
    status: Status
    updated_at: datetime.datetime
    last_push_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_count = self.account_count

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        id = self.id

        is_read_only = self.is_read_only

        kind: str = self.kind

        name = self.name

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        last_push_at: None | str | Unset
        if isinstance(self.last_push_at, Unset):
            last_push_at = UNSET
        elif isinstance(self.last_push_at, datetime.datetime):
            last_push_at = self.last_push_at.isoformat()
        else:
            last_push_at = self.last_push_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_count": account_count,
                "created_at": created_at,
                "created_by": created_by,
                "id": id,
                "is_read_only": is_read_only,
                "kind": kind,
                "name": name,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if last_push_at is not UNSET:
            field_dict["last_push_at"] = last_push_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_count = d.pop("account_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by = d.pop("created_by")

        id = d.pop("id")

        is_read_only = d.pop("is_read_only")

        kind = check_sources_kind(d.pop("kind"))

        name = d.pop("name")

        status = check_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_last_push_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_push_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_push_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_push_at = _parse_last_push_at(d.pop("last_push_at", UNSET))

        source_response = cls(
            account_count=account_count,
            created_at=created_at,
            created_by=created_by,
            id=id,
            is_read_only=is_read_only,
            kind=kind,
            name=name,
            status=status,
            updated_at=updated_at,
            last_push_at=last_push_at,
        )

        source_response.additional_properties = d
        return source_response

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
