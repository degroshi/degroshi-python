from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.analytics_currency_info import AnalyticsCurrencyInfo
    from ..models.net_worth_point import NetWorthPoint


T = TypeVar("T", bound="NetWorthTimeSeriesResponse")


@_attrs_define
class NetWorthTimeSeriesResponse:
    """
    Attributes:
        currency_info (AnalyticsCurrencyInfo):
        missing_rates (list[str] | None | Unset): `missing_rates` lists currencies whose amounts could not be converted
            into the response currency (no exchange rate available). Those amounts are excluded from the totals above;
            empty/omitted when everything converted.
        points (list[NetWorthPoint] | None | Unset):
    """

    currency_info: AnalyticsCurrencyInfo
    missing_rates: list[str] | None | Unset = UNSET
    points: list[NetWorthPoint] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.net_worth_point import NetWorthPoint  # noqa: PLC0415

        currency_info = self.currency_info.to_dict()

        missing_rates: list[str] | None | Unset
        if isinstance(self.missing_rates, Unset):
            missing_rates = UNSET
        elif isinstance(self.missing_rates, list):
            missing_rates = self.missing_rates

        else:
            missing_rates = self.missing_rates

        points: list[dict[str, Any]] | None | Unset
        if isinstance(self.points, Unset):
            points = UNSET
        elif isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)

        else:
            points = self.points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyInfo": currency_info,
            }
        )
        if missing_rates is not UNSET:
            field_dict["missing_rates"] = missing_rates
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_currency_info import AnalyticsCurrencyInfo  # noqa: PLC0415
        from ..models.net_worth_point import NetWorthPoint  # noqa: PLC0415

        d = dict(src_dict)
        currency_info = AnalyticsCurrencyInfo.from_dict(d.pop("currencyInfo"))

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

        def _parse_points(data: object) -> list[NetWorthPoint] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = NetWorthPoint.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NetWorthPoint] | None | Unset, data)

        points = _parse_points(d.pop("points", UNSET))

        net_worth_time_series_response = cls(
            currency_info=currency_info,
            missing_rates=missing_rates,
            points=points,
        )

        net_worth_time_series_response.additional_properties = d
        return net_worth_time_series_response

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
