from typing import Literal

ReactionsSummaryGlyphType0 = Literal["later", "ok", "question", "thanks"]

REACTIONS_SUMMARY_GLYPH_TYPE_0_VALUES: set[ReactionsSummaryGlyphType0] = {
    "later",
    "ok",
    "question",
    "thanks",
}


def check_reactions_summary_glyph_type_0(value: str) -> ReactionsSummaryGlyphType0:
    if value in REACTIONS_SUMMARY_GLYPH_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REACTIONS_SUMMARY_GLYPH_TYPE_0_VALUES!r}")
