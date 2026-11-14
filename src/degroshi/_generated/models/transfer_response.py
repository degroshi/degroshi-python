from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.transfer_display import TransferDisplay


T = TypeVar("T", bound="TransferResponse")


@_attrs_define
class TransferResponse:
    """
    Attributes:
        asset (str): Asset and Quantity are what moved (the quantity as the key side reports it).
        date (datetime.date): The local day in the requesting user's zone.
        from_hidden (bool):
        id (str): ID is the pair's key: its outgoing activity, else (that one hidden from the caller) the incoming one.
        occurred_at (datetime.datetime):
        quantity (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        to_hidden (bool):
        chain (None | str | Unset):
        display (None | TransferDisplay | Unset): Value in the display currency the device sent (X-Display-Currency),
            converted at today's rate and rounded to cents; absent when that is `value_currency`, none was sent or there is
            no value or rate. Clients show it in place of Value.
        explorer_url (None | str | Unset): The page of `tx_hash` in its chain's explorer (Etherscan, Solscan, OKLink for
            X Layer…); absent when the chain isn't known, then the hash is shown as copyable text.
        from_account_id (None | str | Unset): `from_account_id` and `from_account_name` are the sending account;
            `from_hidden` marks one the caller can't see (shown as "another account"), and then both are absent. To*
            likewise.
        from_account_name (None | str | Unset):
        in_activity_id (None | str | Unset):
        out_activity_id (None | str | Unset): `out_activity_id` and `in_activity_id` are the two activities (each in its
            account's activity feed); absent for a side the caller can't see.
        to_account_id (None | str | Unset):
        to_account_name (None | str | Unset):
        tx_hash (None | str | Unset):
        value (None | Decimal | Unset): The fiat value at the time, in `value_currency`.
        value_currency (None | str | Unset):
    """

    asset: str
    date: datetime.date
    from_hidden: bool
    id: str
    occurred_at: datetime.datetime
    quantity: Decimal
    to_hidden: bool
    chain: None | str | Unset = UNSET
    display: None | TransferDisplay | Unset = UNSET
    explorer_url: None | str | Unset = UNSET
    from_account_id: None | str | Unset = UNSET
    from_account_name: None | str | Unset = UNSET
    in_activity_id: None | str | Unset = UNSET
    out_activity_id: None | str | Unset = UNSET
    to_account_id: None | str | Unset = UNSET
    to_account_name: None | str | Unset = UNSET
    tx_hash: None | str | Unset = UNSET
    value: None | Decimal | Unset = UNSET
    value_currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_display import TransferDisplay  # noqa: PLC0415

        asset = self.asset

        date = self.date.isoformat()

        from_hidden = self.from_hidden

        id = self.id

        occurred_at = self.occurred_at.isoformat()

        quantity = decimal_out(self.quantity)

        to_hidden = self.to_hidden

        chain: None | str | Unset
        if isinstance(self.chain, Unset):
            chain = UNSET
        else:
            chain = self.chain

        display: dict[str, Any] | None | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        elif isinstance(self.display, TransferDisplay):
            display = self.display.to_dict()
        else:
            display = self.display

        explorer_url: None | str | Unset
        if isinstance(self.explorer_url, Unset):
            explorer_url = UNSET
        else:
            explorer_url = self.explorer_url

        from_account_id: None | str | Unset
        if isinstance(self.from_account_id, Unset):
            from_account_id = UNSET
        else:
            from_account_id = self.from_account_id

        from_account_name: None | str | Unset
        if isinstance(self.from_account_name, Unset):
            from_account_name = UNSET
        else:
            from_account_name = self.from_account_name

        in_activity_id: None | str | Unset
        if isinstance(self.in_activity_id, Unset):
            in_activity_id = UNSET
        else:
            in_activity_id = self.in_activity_id

        out_activity_id: None | str | Unset
        if isinstance(self.out_activity_id, Unset):
            out_activity_id = UNSET
        else:
            out_activity_id = self.out_activity_id

        to_account_id: None | str | Unset
        if isinstance(self.to_account_id, Unset):
            to_account_id = UNSET
        else:
            to_account_id = self.to_account_id

        to_account_name: None | str | Unset
        if isinstance(self.to_account_name, Unset):
            to_account_name = UNSET
        else:
            to_account_name = self.to_account_name

        tx_hash: None | str | Unset
        if isinstance(self.tx_hash, Unset):
            tx_hash = UNSET
        else:
            tx_hash = self.tx_hash

        value: None | Decimal | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = decimal_out(self.value)

        value_currency: None | str | Unset
        if isinstance(self.value_currency, Unset):
            value_currency = UNSET
        else:
            value_currency = self.value_currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset": asset,
                "date": date,
                "from_hidden": from_hidden,
                "id": id,
                "occurred_at": occurred_at,
                "quantity": quantity,
                "to_hidden": to_hidden,
            }
        )
        if chain is not UNSET:
            field_dict["chain"] = chain
        if display is not UNSET:
            field_dict["display"] = display
        if explorer_url is not UNSET:
            field_dict["explorer_url"] = explorer_url
        if from_account_id is not UNSET:
            field_dict["from_account_id"] = from_account_id
        if from_account_name is not UNSET:
            field_dict["from_account_name"] = from_account_name
        if in_activity_id is not UNSET:
            field_dict["in_activity_id"] = in_activity_id
        if out_activity_id is not UNSET:
            field_dict["out_activity_id"] = out_activity_id
        if to_account_id is not UNSET:
            field_dict["to_account_id"] = to_account_id
        if to_account_name is not UNSET:
            field_dict["to_account_name"] = to_account_name
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if value is not UNSET:
            field_dict["value"] = value
        if value_currency is not UNSET:
            field_dict["value_currency"] = value_currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_display import TransferDisplay  # noqa: PLC0415

        d = dict(src_dict)
        asset = d.pop("asset")

        date = datetime.date.fromisoformat(d.pop("date"))

        from_hidden = d.pop("from_hidden")

        id = d.pop("id")

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        quantity = decimal_in(d.pop("quantity"))

        to_hidden = d.pop("to_hidden")

        def _parse_chain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chain = _parse_chain(d.pop("chain", UNSET))

        def _parse_display(data: object) -> None | TransferDisplay | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_type_0 = TransferDisplay.from_dict(data)

                return display_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransferDisplay | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        def _parse_explorer_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        explorer_url = _parse_explorer_url(d.pop("explorer_url", UNSET))

        def _parse_from_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_account_id = _parse_from_account_id(d.pop("from_account_id", UNSET))

        def _parse_from_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_account_name = _parse_from_account_name(d.pop("from_account_name", UNSET))

        def _parse_in_activity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        in_activity_id = _parse_in_activity_id(d.pop("in_activity_id", UNSET))

        def _parse_out_activity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        out_activity_id = _parse_out_activity_id(d.pop("out_activity_id", UNSET))

        def _parse_to_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_account_id = _parse_to_account_id(d.pop("to_account_id", UNSET))

        def _parse_to_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_account_name = _parse_to_account_name(d.pop("to_account_name", UNSET))

        def _parse_tx_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tx_hash = _parse_tx_hash(d.pop("tx_hash", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = decimal_in(_parse_value(d.pop("value", UNSET)))

        def _parse_value_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_currency = _parse_value_currency(d.pop("value_currency", UNSET))

        transfer_response = cls(
            asset=asset,
            date=date,
            from_hidden=from_hidden,
            id=id,
            occurred_at=occurred_at,
            quantity=quantity,
            to_hidden=to_hidden,
            chain=chain,
            display=display,
            explorer_url=explorer_url,
            from_account_id=from_account_id,
            from_account_name=from_account_name,
            in_activity_id=in_activity_id,
            out_activity_id=out_activity_id,
            to_account_id=to_account_id,
            to_account_name=to_account_name,
            tx_hash=tx_hash,
            value=value,
            value_currency=value_currency,
        )

        transfer_response.additional_properties = d
        return transfer_response

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
