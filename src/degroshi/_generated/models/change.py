from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.change_op import ChangeOp
from ..models.change_op import check_change_op
from ..models.object_type import check_object_type
from ..models.object_type import ObjectType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.change_data_type_0 import ChangeDataType0


T = TypeVar("T", bound="Change")


@_attrs_define
class Change:
    """
    Attributes:
        id (str): ID is the object's id.
        op (ChangeOp): Op: upsert (the object is new or changed: data is it now) or delete (gone, or no longer visible
            to the caller).
        type_ (ObjectType):
        data (ChangeDataType0 | None | Unset): The object as its list endpoint returns it now (GET /v1/transactions,
            /v1/accounts, /v1/categories without children, /v1/budgets, /v1/recurring-transactions); absent for a delete.
    """

    id: str
    op: ChangeOp
    type_: ObjectType
    data: ChangeDataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.change_data_type_0 import ChangeDataType0  # noqa: PLC0415

        id = self.id

        op: str = self.op

        type_: str = self.type_

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, ChangeDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "op": op,
                "type": type_,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_data_type_0 import ChangeDataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        op = check_change_op(d.pop("op"))

        type_ = check_object_type(d.pop("type"))

        def _parse_data(data: object) -> ChangeDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ChangeDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChangeDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        change = cls(
            id=id,
            op=op,
            type_=type_,
            data=data,
        )

        change.additional_properties = d
        return change

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
