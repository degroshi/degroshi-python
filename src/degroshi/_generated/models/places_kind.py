from typing import Literal

PlacesKind = Literal["city", "country", "online", "pin", "poi"]

PLACES_KIND_VALUES: set[PlacesKind] = {
    "city",
    "country",
    "online",
    "pin",
    "poi",
}


def check_places_kind(value: str) -> PlacesKind:
    if value in PLACES_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLACES_KIND_VALUES!r}")
