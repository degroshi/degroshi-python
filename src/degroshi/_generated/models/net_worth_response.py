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
    from ..models.account_with_converted_balance import AccountWithConvertedBalance
    from ..models.accounts_currency_info import AccountsCurrencyInfo


T = TypeVar("T", bound="NetWorthResponse")


@_attrs_define
class NetWorthResponse:
    """
    Attributes:
        base_currency (str):
        calculated_at (datetime.datetime):
        currency_info (AccountsCurrencyInfo):
        net_worth (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        total_assets (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        total_liabilities (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        by_account (list[AccountWithConvertedBalance] | None | Unset):
        missing_rates (list[str] | None | Unset): Lists account currencies without an exchange rate into base_currency;
            those accounts are excluded from the totals.
    """

    base_currency: str
    calculated_at: datetime.datetime
    currency_info: AccountsCurrencyInfo
    net_worth: Decimal
    total_assets: Decimal
    total_liabilities: Decimal
    by_account: list[AccountWithConvertedBalance] | None | Unset = UNSET
    missing_rates: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.account_with_converted_balance import AccountWithConvertedBalance  # noqa: PLC0415
        from ..models.accounts_currency_info import AccountsCurrencyInfo  # noqa: PLC0415

        base_currency = self.base_currency

        calculated_at = self.calculated_at.isoformat()

        currency_info = self.currency_info.to_dict()

        net_worth = decimal_out(self.net_worth)

        total_assets = decimal_out(self.total_assets)

        total_liabilities = decimal_out(self.total_liabilities)

        by_account: list[dict[str, Any]] | None | Unset
        if isinstance(self.by_account, Unset):
            by_account = UNSET
        elif isinstance(self.by_account, list):
            by_account = []
            for by_account_type_0_item_data in self.by_account:
                by_account_type_0_item = by_account_type_0_item_data.to_dict()
                by_account.append(by_account_type_0_item)

        else:
            by_account = self.by_account

        missing_rates: list[str] | None | Unset
        if isinstance(self.missing_rates, Unset):
            missing_rates = UNSET
        elif isinstance(self.missing_rates, list):
            missing_rates = self.missing_rates

        else:
            missing_rates = self.missing_rates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_currency": base_currency,
                "calculated_at": calculated_at,
                "currency_info": currency_info,
                "net_worth": net_worth,
                "total_assets": total_assets,
                "total_liabilities": total_liabilities,
            }
        )
        if by_account is not UNSET:
            field_dict["by_account"] = by_account
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_with_converted_balance import AccountWithConvertedBalance  # noqa: PLC0415
        from ..models.accounts_currency_info import AccountsCurrencyInfo  # noqa: PLC0415

        d = dict(src_dict)
        base_currency = d.pop("base_currency")

        calculated_at = datetime.datetime.fromisoformat(d.pop("calculated_at"))

        currency_info = AccountsCurrencyInfo.from_dict(d.pop("currency_info"))

        net_worth = decimal_in(d.pop("net_worth"))

        total_assets = decimal_in(d.pop("total_assets"))

        total_liabilities = decimal_in(d.pop("total_liabilities"))

        def _parse_by_account(data: object) -> list[AccountWithConvertedBalance] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_account_type_0 = []
                _by_account_type_0 = data
                for by_account_type_0_item_data in _by_account_type_0:
                    by_account_type_0_item = AccountWithConvertedBalance.from_dict(by_account_type_0_item_data)

                    by_account_type_0.append(by_account_type_0_item)

                return by_account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccountWithConvertedBalance] | None | Unset, data)

        by_account = _parse_by_account(d.pop("by_account", UNSET))

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

        net_worth_response = cls(
            base_currency=base_currency,
            calculated_at=calculated_at,
            currency_info=currency_info,
            net_worth=net_worth,
            total_assets=total_assets,
            total_liabilities=total_liabilities,
            by_account=by_account,
            missing_rates=missing_rates,
        )

        net_worth_response.additional_properties = d
        return net_worth_response

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
