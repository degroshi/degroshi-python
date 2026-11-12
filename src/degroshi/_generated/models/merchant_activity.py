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
    from ..models.brand_response import BrandResponse
    from ..models.merchant_category import MerchantCategory


T = TypeVar("T", bound="MerchantActivity")


@_attrs_define
class MerchantActivity:
    """
    Attributes:
        amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        count (int):
        key (str): Key identifies the merchant across periods and endpoints: "p:<id>" for a recognized brand,
            "n:<normalized name>" otherwise.
        name (str): The brand's name, else the merchant's spelling used by the most operations.
        previous_amount (Decimal): Decimal number encoded as a string (for example "1234.5600"); never a JSON number.
        previous_count (int):
        brand (BrandResponse | None | Unset): The recognized brand with its logo URLs, when there is one.
        category (MerchantCategory | None | Unset): Where most of the merchant's amount went in the period.
        change_percent (float | None | Unset): The change of amount against previous_amount, null when there was nothing
            in the previous period.
    """

    amount: Decimal
    count: int
    key: str
    name: str
    previous_amount: Decimal
    previous_count: int
    brand: BrandResponse | None | Unset = UNSET
    category: MerchantCategory | None | Unset = UNSET
    change_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brand_response import BrandResponse  # noqa: PLC0415
        from ..models.merchant_category import MerchantCategory  # noqa: PLC0415

        amount = decimal_out(self.amount)

        count = self.count

        key = self.key

        name = self.name

        previous_amount = decimal_out(self.previous_amount)

        previous_count = self.previous_count

        brand: dict[str, Any] | None | Unset
        if isinstance(self.brand, Unset):
            brand = UNSET
        elif isinstance(self.brand, BrandResponse):
            brand = self.brand.to_dict()
        else:
            brand = self.brand

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, MerchantCategory):
            category = self.category.to_dict()
        else:
            category = self.category

        change_percent: float | None | Unset
        if isinstance(self.change_percent, Unset):
            change_percent = UNSET
        else:
            change_percent = self.change_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "count": count,
                "key": key,
                "name": name,
                "previous_amount": previous_amount,
                "previous_count": previous_count,
            }
        )
        if brand is not UNSET:
            field_dict["brand"] = brand
        if category is not UNSET:
            field_dict["category"] = category
        if change_percent is not UNSET:
            field_dict["change_percent"] = change_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand_response import BrandResponse  # noqa: PLC0415
        from ..models.merchant_category import MerchantCategory  # noqa: PLC0415

        d = dict(src_dict)
        amount = decimal_in(d.pop("amount"))

        count = d.pop("count")

        key = d.pop("key")

        name = d.pop("name")

        previous_amount = decimal_in(d.pop("previous_amount"))

        previous_count = d.pop("previous_count")

        def _parse_brand(data: object) -> BrandResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                brand_type_0 = BrandResponse.from_dict(data)

                return brand_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrandResponse | None | Unset, data)

        brand = _parse_brand(d.pop("brand", UNSET))

        def _parse_category(data: object) -> MerchantCategory | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_type_0 = MerchantCategory.from_dict(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MerchantCategory | None | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_change_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        change_percent = _parse_change_percent(d.pop("change_percent", UNSET))

        merchant_activity = cls(
            amount=amount,
            count=count,
            key=key,
            name=name,
            previous_amount=previous_amount,
            previous_count=previous_count,
            brand=brand,
            category=category,
            change_percent=change_percent,
        )

        merchant_activity.additional_properties = d
        return merchant_activity

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
