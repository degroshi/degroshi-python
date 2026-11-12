from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="ImportCompletedEventDataObject")


@_attrs_define
class ImportCompletedEventDataObject:
    """
    Attributes:
        account_ids (list[str] | Unset):
        created (float | Unset):
        date_from (str | Unset):
        date_to (str | Unset):
        deleted (float | Unset):
        import_id (str | Unset):
        object_ (str | Unset):
        source (str | Unset):
        updated (float | Unset):
    """

    account_ids: list[str] | Unset = UNSET
    created: float | Unset = UNSET
    date_from: str | Unset = UNSET
    date_to: str | Unset = UNSET
    deleted: float | Unset = UNSET
    import_id: str | Unset = UNSET
    object_: str | Unset = UNSET
    source: str | Unset = UNSET
    updated: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_ids: list[str] | Unset = UNSET
        if not isinstance(self.account_ids, Unset):
            account_ids = self.account_ids

        created = self.created

        date_from = self.date_from

        date_to = self.date_to

        deleted = self.deleted

        import_id = self.import_id

        object_ = self.object_

        source = self.source

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_ids is not UNSET:
            field_dict["account_ids"] = account_ids
        if created is not UNSET:
            field_dict["created"] = created
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if object_ is not UNSET:
            field_dict["object"] = object_
        if source is not UNSET:
            field_dict["source"] = source
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_ids = cast(list[str], d.pop("account_ids", UNSET))

        created = d.pop("created", UNSET)

        date_from = d.pop("date_from", UNSET)

        date_to = d.pop("date_to", UNSET)

        deleted = d.pop("deleted", UNSET)

        import_id = d.pop("import_id", UNSET)

        object_ = d.pop("object", UNSET)

        source = d.pop("source", UNSET)

        updated = d.pop("updated", UNSET)

        import_completed_event_data_object = cls(
            account_ids=account_ids,
            created=created,
            date_from=date_from,
            date_to=date_to,
            deleted=deleted,
            import_id=import_id,
            object_=object_,
            source=source,
            updated=updated,
        )

        import_completed_event_data_object.additional_properties = d
        return import_completed_event_data_object

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
