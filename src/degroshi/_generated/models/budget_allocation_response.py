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

if TYPE_CHECKING:
    from ..models.allocation_display import AllocationDisplay


T = TypeVar("T", bound="BudgetAllocationResponse")


@_attrs_define
class BudgetAllocationResponse:
    """
    Attributes:
        amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        budget_id (str):
        category_id (str):
        category_name (str): The category's display name in the request language (built-in categories translated, custom
            ones as stored).
        id (str):
        progress (float):
        remaining (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        spent (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        display (AllocationDisplay | None | Unset): The allocation in the display currency the device sent (X-Display-
            Currency), converted at today's rate; null when that is the budget currency, none was sent or there is no rate.
        missing_rates (list[str] | None | Unset): Lists spending currencies without an exchange rate into the budget
            currency; that spending is not included in spent.
        parent_allocation_id (None | str | Unset): The group allocation this one is an inner limit of: the budget's
            allocation of the nearest ancestor category; null at the top level. An inner limit is part of its group's amount
            and the group's spent already includes it, so the budget's totals count only top-level allocations.
        version (int | None | Unset): The allocation row version (also the ETag): send it as If-Match on PATCH / DELETE
            to detect concurrent edits (412).
    """

    amount: Decimal
    budget_id: str
    category_id: str
    category_name: str
    id: str
    progress: float
    remaining: Decimal
    spent: Decimal
    display: AllocationDisplay | None | Unset = UNSET
    missing_rates: list[str] | None | Unset = UNSET
    parent_allocation_id: None | str | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.allocation_display import AllocationDisplay  # noqa: PLC0415

        amount = decimal_out(self.amount)

        budget_id = self.budget_id

        category_id = self.category_id

        category_name = self.category_name

        id = self.id

        progress = self.progress

        remaining = decimal_out(self.remaining)

        spent = decimal_out(self.spent)

        display: dict[str, Any] | None | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        elif isinstance(self.display, AllocationDisplay):
            display = self.display.to_dict()
        else:
            display = self.display

        missing_rates: list[str] | None | Unset
        if isinstance(self.missing_rates, Unset):
            missing_rates = UNSET
        elif isinstance(self.missing_rates, list):
            missing_rates = self.missing_rates

        else:
            missing_rates = self.missing_rates

        parent_allocation_id: None | str | Unset
        if isinstance(self.parent_allocation_id, Unset):
            parent_allocation_id = UNSET
        else:
            parent_allocation_id = self.parent_allocation_id

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "budget_id": budget_id,
                "category_id": category_id,
                "category_name": category_name,
                "id": id,
                "progress": progress,
                "remaining": remaining,
                "spent": spent,
            }
        )
        if display is not UNSET:
            field_dict["display"] = display
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates
        if parent_allocation_id is not UNSET:
            field_dict["parent_allocation_id"] = parent_allocation_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_display import AllocationDisplay  # noqa: PLC0415

        d = dict(src_dict)
        amount = decimal_in(d.pop("amount"))

        budget_id = d.pop("budget_id")

        category_id = d.pop("category_id")

        category_name = d.pop("category_name")

        id = d.pop("id")

        progress = d.pop("progress")

        remaining = decimal_in(d.pop("remaining"))

        spent = decimal_in(d.pop("spent"))

        def _parse_display(data: object) -> AllocationDisplay | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_type_0 = AllocationDisplay.from_dict(data)

                return display_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AllocationDisplay | None | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        def _parse_missing_rates(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_rates_type_0 = cast(list[str], data)

                return missing_rates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        missing_rates = _parse_missing_rates(d.pop("missing_rates", UNSET))

        def _parse_parent_allocation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_allocation_id = _parse_parent_allocation_id(d.pop("parent_allocation_id", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        budget_allocation_response = cls(
            amount=amount,
            budget_id=budget_id,
            category_id=category_id,
            category_name=category_name,
            id=id,
            progress=progress,
            remaining=remaining,
            spent=spent,
            display=display,
            missing_rates=missing_rates,
            parent_allocation_id=parent_allocation_id,
            version=version,
        )

        budget_allocation_response.additional_properties = d
        return budget_allocation_response

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
