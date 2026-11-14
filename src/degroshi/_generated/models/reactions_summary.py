from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reactions_summary_glyph_type_0 import check_reactions_summary_glyph_type_0
from ..models.reactions_summary_glyph_type_0 import ReactionsSummaryGlyphType0
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="ReactionsSummary")


@_attrs_define
class ReactionsSummary:
    """
    Attributes:
        comments (int): How many comments it has.
        open_question (bool): The latest question glyph has no comment from another member after it.
        glyph (None | ReactionsSummaryGlyphType0 | Unset): The latest reaction by anyone; omitted without one.
    """

    comments: int
    open_question: bool
    glyph: None | ReactionsSummaryGlyphType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        open_question = self.open_question

        glyph: None | str | Unset
        if isinstance(self.glyph, Unset):
            glyph = UNSET
        elif isinstance(self.glyph, str):
            glyph = self.glyph
        else:
            glyph = self.glyph

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comments": comments,
                "open_question": open_question,
            }
        )
        if glyph is not UNSET:
            field_dict["glyph"] = glyph

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments")

        open_question = d.pop("open_question")

        def _parse_glyph(data: object) -> None | ReactionsSummaryGlyphType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                glyph_type_0 = check_reactions_summary_glyph_type_0(data)

                return glyph_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReactionsSummaryGlyphType0 | Unset, data)

        glyph = _parse_glyph(d.pop("glyph", UNSET))

        reactions_summary = cls(
            comments=comments,
            open_question=open_question,
            glyph=glyph,
        )

        reactions_summary.additional_properties = d
        return reactions_summary

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
