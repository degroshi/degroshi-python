from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.possible_duplicate import PossibleDuplicate
    from ..models.push_item_result import PushItemResult


T = TypeVar("T", bound="PushBatchResponse")


@_attrs_define
class PushBatchResponse:
    """
    Attributes:
        possible_duplicates (list[PossibleDuplicate] | None | Unset):
        results (list[PushItemResult] | None | Unset):
    """

    possible_duplicates: list[PossibleDuplicate] | None | Unset = UNSET
    results: list[PushItemResult] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.possible_duplicate import PossibleDuplicate  # noqa: PLC0415
        from ..models.push_item_result import PushItemResult  # noqa: PLC0415

        possible_duplicates: list[dict[str, Any]] | None | Unset
        if isinstance(self.possible_duplicates, Unset):
            possible_duplicates = UNSET
        elif isinstance(self.possible_duplicates, list):
            possible_duplicates = []
            for possible_duplicates_type_0_item_data in self.possible_duplicates:
                possible_duplicates_type_0_item = possible_duplicates_type_0_item_data.to_dict()
                possible_duplicates.append(possible_duplicates_type_0_item)

        else:
            possible_duplicates = self.possible_duplicates

        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)

        else:
            results = self.results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if possible_duplicates is not UNSET:
            field_dict["possible_duplicates"] = possible_duplicates
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.possible_duplicate import PossibleDuplicate  # noqa: PLC0415
        from ..models.push_item_result import PushItemResult  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_possible_duplicates(data: object) -> list[PossibleDuplicate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                possible_duplicates_type_0 = []
                _possible_duplicates_type_0 = data
                for possible_duplicates_type_0_item_data in _possible_duplicates_type_0:
                    possible_duplicates_type_0_item = PossibleDuplicate.from_dict(possible_duplicates_type_0_item_data)

                    possible_duplicates_type_0.append(possible_duplicates_type_0_item)

                return possible_duplicates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PossibleDuplicate] | None | Unset, data)

        possible_duplicates = _parse_possible_duplicates(d.pop("possible_duplicates", UNSET))

        def _parse_results(data: object) -> list[PushItemResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in _results_type_0:
                    results_type_0_item = PushItemResult.from_dict(results_type_0_item_data)

                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PushItemResult] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))

        push_batch_response = cls(
            possible_duplicates=possible_duplicates,
            results=results,
        )

        push_batch_response.additional_properties = d
        return push_batch_response

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
