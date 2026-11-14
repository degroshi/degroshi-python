from typing import Literal

OccurrenceStatus = Literal["awaiting_confirmation", "missing", "paid", "paused", "planned", "skipped"]

OCCURRENCE_STATUS_VALUES: set[OccurrenceStatus] = {
    "awaiting_confirmation",
    "missing",
    "paid",
    "paused",
    "planned",
    "skipped",
}


def check_occurrence_status(value: str) -> OccurrenceStatus:
    if value in OCCURRENCE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OCCURRENCE_STATUS_VALUES!r}")
