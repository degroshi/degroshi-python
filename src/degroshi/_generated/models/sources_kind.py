from typing import Literal

SourcesKind = Literal["bank", "broker", "card", "crypto", "income", "other"]

SOURCES_KIND_VALUES: set[SourcesKind] = {
    "bank",
    "broker",
    "card",
    "crypto",
    "income",
    "other",
}


def check_sources_kind(value: str) -> SourcesKind:
    if value in SOURCES_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SOURCES_KIND_VALUES!r}")
