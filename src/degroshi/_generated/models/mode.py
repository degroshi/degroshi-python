from typing import Literal

Mode = Literal["confirm", "post", "track_only"]

MODE_VALUES: set[Mode] = {
    "confirm",
    "post",
    "track_only",
}


def check_mode(value: str) -> Mode:
    if value in MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MODE_VALUES!r}")
