from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.linked_activity_response_status import check_linked_activity_response_status
from ..models.linked_activity_response_status import LinkedActivityResponseStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.linked_activity_leg import LinkedActivityLeg


T = TypeVar("T", bound="LinkedActivityResponse")


@_attrs_define
class LinkedActivityResponse:
    """
    Attributes:
        account_id (str):
        id (str):
        kind (str): Kind: send, receive, trade, convert, transfer, deposit, withdraw, fee, bonus, stake, unstake,
            borrow, repay, approve, mint, burn, other.
        legs (list[LinkedActivityLeg]):
        occurred_at (datetime.datetime):
        provider (str): The connection's provider: "zerion" for a wallet, "ccxt:<venue>" for an exchange.
        status (LinkedActivityResponseStatus):
        chain (None | str | Unset): The network it happened on: a wallet activity's chain, or the network an exchange's
            deposit or withdrawal names. Absent when unknown (an exchange trade).
        chain_name (None | str | Unset): Chain's display name («binance-smart-chain» → «BNB Chain»).
        explorer_url (None | str | Unset): The page of `tx_hash` in its chain's explorer; absent when the chain isn't
            known, then the hash is shown as copyable text.
        fee (LinkedActivityLeg | None | Unset):
        tx_hash (None | str | Unset): The on-chain transaction hash; absent when the activity has none.
    """

    account_id: str
    id: str
    kind: str
    legs: list[LinkedActivityLeg]
    occurred_at: datetime.datetime
    provider: str
    status: LinkedActivityResponseStatus
    chain: None | str | Unset = UNSET
    chain_name: None | str | Unset = UNSET
    explorer_url: None | str | Unset = UNSET
    fee: LinkedActivityLeg | None | Unset = UNSET
    tx_hash: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.linked_activity_leg import LinkedActivityLeg  # noqa: PLC0415

        account_id = self.account_id

        id = self.id

        kind = self.kind

        legs = []
        for legs_item_data in self.legs:
            legs_item = legs_item_data.to_dict()
            legs.append(legs_item)

        occurred_at = self.occurred_at.isoformat()

        provider = self.provider

        status: str = self.status

        chain: None | str | Unset
        if isinstance(self.chain, Unset):
            chain = UNSET
        else:
            chain = self.chain

        chain_name: None | str | Unset
        if isinstance(self.chain_name, Unset):
            chain_name = UNSET
        else:
            chain_name = self.chain_name

        explorer_url: None | str | Unset
        if isinstance(self.explorer_url, Unset):
            explorer_url = UNSET
        else:
            explorer_url = self.explorer_url

        fee: dict[str, Any] | None | Unset
        if isinstance(self.fee, Unset):
            fee = UNSET
        elif isinstance(self.fee, LinkedActivityLeg):
            fee = self.fee.to_dict()
        else:
            fee = self.fee

        tx_hash: None | str | Unset
        if isinstance(self.tx_hash, Unset):
            tx_hash = UNSET
        else:
            tx_hash = self.tx_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "id": id,
                "kind": kind,
                "legs": legs,
                "occurred_at": occurred_at,
                "provider": provider,
                "status": status,
            }
        )
        if chain is not UNSET:
            field_dict["chain"] = chain
        if chain_name is not UNSET:
            field_dict["chain_name"] = chain_name
        if explorer_url is not UNSET:
            field_dict["explorer_url"] = explorer_url
        if fee is not UNSET:
            field_dict["fee"] = fee
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_activity_leg import LinkedActivityLeg  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        id = d.pop("id")

        kind = d.pop("kind")

        legs = []
        _legs = d.pop("legs")
        for legs_item_data in _legs:
            legs_item = LinkedActivityLeg.from_dict(legs_item_data)

            legs.append(legs_item)

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        provider = d.pop("provider")

        status = check_linked_activity_response_status(d.pop("status"))

        def _parse_chain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chain = _parse_chain(d.pop("chain", UNSET))

        def _parse_chain_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chain_name = _parse_chain_name(d.pop("chain_name", UNSET))

        def _parse_explorer_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        explorer_url = _parse_explorer_url(d.pop("explorer_url", UNSET))

        def _parse_fee(data: object) -> LinkedActivityLeg | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fee_type_0 = LinkedActivityLeg.from_dict(data)

                return fee_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinkedActivityLeg | None | Unset, data)

        fee = _parse_fee(d.pop("fee", UNSET))

        def _parse_tx_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tx_hash = _parse_tx_hash(d.pop("tx_hash", UNSET))

        linked_activity_response = cls(
            account_id=account_id,
            id=id,
            kind=kind,
            legs=legs,
            occurred_at=occurred_at,
            provider=provider,
            status=status,
            chain=chain,
            chain_name=chain_name,
            explorer_url=explorer_url,
            fee=fee,
            tx_hash=tx_hash,
        )

        linked_activity_response.additional_properties = d
        return linked_activity_response

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
