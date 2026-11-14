from typing import Literal

LinkedActivityLegDirection = Literal["in", "out", "self"]

LINKED_ACTIVITY_LEG_DIRECTION_VALUES: set[LinkedActivityLegDirection] = {
    "in",
    "out",
    "self",
}


def check_linked_activity_leg_direction(value: str) -> LinkedActivityLegDirection:
    if value in LINKED_ACTIVITY_LEG_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINKED_ACTIVITY_LEG_DIRECTION_VALUES!r}")
