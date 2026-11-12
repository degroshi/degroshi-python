from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.balance_result_status import BalanceResultStatus
from ..models.balance_result_status import check_balance_result_status
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.push_item_error import PushItemError


T = TypeVar("T", bound="BalanceResult")


@_attrs_define
class BalanceResult:
    """
    Attributes:
        account (str):
        status (BalanceResultStatus): Adjusted (the difference became one balance adjustment), unchanged, stale (an
            older as_of than the last applied) or failed.
        adjustment (None | str | Unset): The difference booked, signed; absent unless adjusted.
        error (None | PushItemError | Unset):
    """

    account: str
    status: BalanceResultStatus
    adjustment: None | str | Unset = UNSET
    error: None | PushItemError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.push_item_error import PushItemError  # noqa: PLC0415

        account = self.account

        status: str = self.status

        adjustment: None | str | Unset
        if isinstance(self.adjustment, Unset):
            adjustment = UNSET
        else:
            adjustment = self.adjustment

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, PushItemError):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "status": status,
            }
        )
        if adjustment is not UNSET:
            field_dict["adjustment"] = adjustment
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.push_item_error import PushItemError  # noqa: PLC0415

        d = dict(src_dict)
        account = d.pop("account")

        status = check_balance_result_status(d.pop("status"))

        def _parse_adjustment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adjustment = _parse_adjustment(d.pop("adjustment", UNSET))

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

        balance_result = cls(
            account=account,
            status=status,
            adjustment=adjustment,
            error=error,
        )

        balance_result.additional_properties = d
        return balance_result

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
