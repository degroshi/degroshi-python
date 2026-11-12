from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.occurrence_response import OccurrenceResponse
    from ..models.occurrence_totals import OccurrenceTotals


T = TypeVar("T", bound="OccurrencesResponse")


@_attrs_define
class OccurrencesResponse:
    """
    Attributes:
        from_ (datetime.date): From and To are the evaluated window (calendar days, both included).
        occurrences (list[OccurrenceResponse]):
        timezone (str): The zone the days are evaluated in: the request's user zone (the chosen one, else the device's
            X-Timezone).
        to (datetime.date):
        totals (None | OccurrenceTotals | Unset): In the display currency the device sent (X-Display-Currency); null
            when it sent none.
    """

    from_: datetime.date
    occurrences: list[OccurrenceResponse]
    timezone: str
    to: datetime.date
    totals: None | OccurrenceTotals | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.occurrence_response import OccurrenceResponse  # noqa: PLC0415
        from ..models.occurrence_totals import OccurrenceTotals  # noqa: PLC0415

        from_ = self.from_.isoformat()

        occurrences = []
        for occurrences_item_data in self.occurrences:
            occurrences_item = occurrences_item_data.to_dict()
            occurrences.append(occurrences_item)

        timezone = self.timezone

        to = self.to.isoformat()

        totals: dict[str, Any] | None | Unset
        if isinstance(self.totals, Unset):
            totals = UNSET
        elif isinstance(self.totals, OccurrenceTotals):
            totals = self.totals.to_dict()
        else:
            totals = self.totals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "occurrences": occurrences,
                "timezone": timezone,
                "to": to,
            }
        )
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.occurrence_response import OccurrenceResponse  # noqa: PLC0415
        from ..models.occurrence_totals import OccurrenceTotals  # noqa: PLC0415

        d = dict(src_dict)
        from_ = datetime.date.fromisoformat(d.pop("from"))

        occurrences = []
        _occurrences = d.pop("occurrences")
        for occurrences_item_data in _occurrences:
            occurrences_item = OccurrenceResponse.from_dict(occurrences_item_data)

            occurrences.append(occurrences_item)

        timezone = d.pop("timezone")

        to = datetime.date.fromisoformat(d.pop("to"))

        def _parse_totals(data: object) -> None | OccurrenceTotals | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                totals_type_0 = OccurrenceTotals.from_dict(data)

                return totals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OccurrenceTotals | Unset, data)

        totals = _parse_totals(d.pop("totals", UNSET))

        occurrences_response = cls(
            from_=from_,
            occurrences=occurrences,
            timezone=timezone,
            to=to,
            totals=totals,
        )

        occurrences_response.additional_properties = d
        return occurrences_response

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
