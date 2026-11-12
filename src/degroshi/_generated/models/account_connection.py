from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_connection_health_type_0 import AccountConnectionHealthType0
from ..models.account_connection_health_type_0 import check_account_connection_health_type_0
from ..models.account_connection_kind import AccountConnectionKind
from ..models.account_connection_kind import check_account_connection_kind
from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="AccountConnection")


@_attrs_define
class AccountConnection:
    """
    Attributes:
        kind (AccountConnectionKind):
        provider (str): The source: monobank, saltedge, zerion, ccxt:binance, …
        health (AccountConnectionHealthType0 | None | Unset): Health of a Monobank-synced account: ok, stale (the bank
            has not answered for it for more than 24 hours while the connection is active) or reconnect_required (confirm a
            new request in the Monobank app). Omitted for other connections.
        last_data_at (datetime.datetime | None | Unset): When the bank last answered for the account (a statement, a
            balance refresh or a push), with or without new rows.
        last_synced_at (datetime.datetime | None | Unset): When the balance was last read from the source.
        name (None | str | Unset): The connection's display name ("Monobank", a wallet label).
    """

    kind: AccountConnectionKind
    provider: str
    health: AccountConnectionHealthType0 | None | Unset = UNSET
    last_data_at: datetime.datetime | None | Unset = UNSET
    last_synced_at: datetime.datetime | None | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        provider = self.provider

        health: None | str | Unset
        if isinstance(self.health, Unset):
            health = UNSET
        elif isinstance(self.health, str):
            health = self.health
        else:
            health = self.health

        last_data_at: None | str | Unset
        if isinstance(self.last_data_at, Unset):
            last_data_at = UNSET
        elif isinstance(self.last_data_at, datetime.datetime):
            last_data_at = self.last_data_at.isoformat()
        else:
            last_data_at = self.last_data_at

        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        elif isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "provider": provider,
            }
        )
        if health is not UNSET:
            field_dict["health"] = health
        if last_data_at is not UNSET:
            field_dict["last_data_at"] = last_data_at
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_account_connection_kind(d.pop("kind"))

        provider = d.pop("provider")

        def _parse_health(data: object) -> AccountConnectionHealthType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                health_type_0 = check_account_connection_health_type_0(data)

                return health_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountConnectionHealthType0 | None | Unset, data)

        health = _parse_health(d.pop("health", UNSET))

        def _parse_last_data_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_data_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_data_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_data_at = _parse_last_data_at(d.pop("last_data_at", UNSET))

        def _parse_last_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        account_connection = cls(
            kind=kind,
            provider=provider,
            health=health,
            last_data_at=last_data_at,
            last_synced_at=last_synced_at,
            name=name,
        )

        account_connection.additional_properties = d
        return account_connection

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
