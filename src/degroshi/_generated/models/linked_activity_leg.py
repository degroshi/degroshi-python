from __future__ import annotations

from decimal import Decimal
from ..._decimal import decimal_in, decimal_out

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.linked_activity_leg_direction import check_linked_activity_leg_direction
from ..models.linked_activity_leg_direction import LinkedActivityLegDirection
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="LinkedActivityLeg")


@_attrs_define
class LinkedActivityLeg:
    """
    Attributes:
        direction (LinkedActivityLegDirection): Direction: in, out, or self (a position of a derivative trade).
        quantity (Decimal): The amount of the asset that moved, always positive.
        symbol (str):
        chain (None | str | Unset):
        currency (None | str | Unset):
        icon_url (None | str | Unset):
        name (None | str | Unset):
        value (None | Decimal | Unset): Its fiat value at the time, in Currency.
    """

    direction: LinkedActivityLegDirection
    quantity: Decimal
    symbol: str
    chain: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    value: None | Decimal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction: str = self.direction

        quantity = decimal_out(self.quantity)

        symbol = self.symbol

        chain: None | str | Unset
        if isinstance(self.chain, Unset):
            chain = UNSET
        else:
            chain = self.chain

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        value: None | Decimal | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = decimal_out(self.value)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
                "quantity": quantity,
                "symbol": symbol,
            }
        )
        if chain is not UNSET:
            field_dict["chain"] = chain
        if currency is not UNSET:
            field_dict["currency"] = currency
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        direction = check_linked_activity_leg_direction(d.pop("direction"))

        quantity = decimal_in(d.pop("quantity"))

        symbol = d.pop("symbol")

        def _parse_chain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chain = _parse_chain(d.pop("chain", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("icon_url", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = decimal_in(_parse_value(d.pop("value", UNSET)))

        linked_activity_leg = cls(
            direction=direction,
            quantity=quantity,
            symbol=symbol,
            chain=chain,
            currency=currency,
            icon_url=icon_url,
            name=name,
            value=value,
        )

        linked_activity_leg.additional_properties = d
        return linked_activity_leg

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
