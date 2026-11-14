from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.transaction_created_event_data import TransactionCreatedEventData


T = TypeVar("T", bound="TransactionCreatedEvent")


@_attrs_define
class TransactionCreatedEvent:
    """The `transaction.created` event, as an endpoint receives it.

    Attributes:
        api_version (str): The endpoint's version of the event shapes.
        created (datetime.datetime):
        data (TransactionCreatedEventData):
        id (UUID):
        object_ (Literal['event']):
        source (str): Who made the change: app, api, bank_sync, import, recurring, categorize, rule, budget or test.
            Every write of a request authenticated by an API key is api.
        space_id (None | UUID): Null for a test event.
        test (bool): True for a test event sent from the endpoint's page.
        type_ (Literal['transaction.created']):
    """

    api_version: str
    created: datetime.datetime
    data: TransactionCreatedEventData
    id: UUID
    object_: Literal["event"]
    source: str
    space_id: None | UUID
    test: bool
    type_: Literal["transaction.created"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_created_event_data import TransactionCreatedEventData  # noqa: PLC0415

        api_version = self.api_version

        created = self.created.isoformat()

        data = self.data.to_dict()

        id = str(self.id)

        object_ = self.object_

        source = self.source

        space_id: None | str
        if isinstance(self.space_id, UUID):
            space_id = str(self.space_id)
        else:
            space_id = self.space_id

        test = self.test

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_version": api_version,
                "created": created,
                "data": data,
                "id": id,
                "object": object_,
                "source": source,
                "space_id": space_id,
                "test": test,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_created_event_data import TransactionCreatedEventData  # noqa: PLC0415

        d = dict(src_dict)
        api_version = d.pop("api_version")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        data = TransactionCreatedEventData.from_dict(d.pop("data"))

        id = UUID(d.pop("id"))

        object_ = cast(Literal["event"], d.pop("object"))
        if object_ != "event":
            raise ValueError(f"object must match const 'event', got '{object_}'")

        source = d.pop("source")

        def _parse_space_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                space_id_type_0 = UUID(data)

                return space_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        space_id = _parse_space_id(d.pop("space_id"))

        test = d.pop("test")

        type_ = cast(Literal["transaction.created"], d.pop("type"))
        if type_ != "transaction.created":
            raise ValueError(f"type must match const 'transaction.created', got '{type_}'")

        transaction_created_event = cls(
            api_version=api_version,
            created=created,
            data=data,
            id=id,
            object_=object_,
            source=source,
            space_id=space_id,
            test=test,
            type_=type_,
        )

        transaction_created_event.additional_properties = d
        return transaction_created_event

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
