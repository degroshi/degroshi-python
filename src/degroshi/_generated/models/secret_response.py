from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="SecretResponse")


@_attrs_define
class SecretResponse:
    """
    Attributes:
        secret (str):
        old_secret_until (datetime.datetime | None | Unset): When the replaced secret stops signing; absent without an
            overlap.
    """

    secret: str
    old_secret_until: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        old_secret_until: None | str | Unset
        if isinstance(self.old_secret_until, Unset):
            old_secret_until = UNSET
        elif isinstance(self.old_secret_until, datetime.datetime):
            old_secret_until = self.old_secret_until.isoformat()
        else:
            old_secret_until = self.old_secret_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
            }
        )
        if old_secret_until is not UNSET:
            field_dict["old_secret_until"] = old_secret_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret = d.pop("secret")

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

        secret_response = cls(
            secret=secret,
            old_secret_until=old_secret_until,
        )

        secret_response.additional_properties = d
        return secret_response

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
