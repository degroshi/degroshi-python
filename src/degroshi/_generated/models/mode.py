from typing import Literal

Mode = Literal["post", "track_only"]

MODE_VALUES: set[Mode] = {
    "post",
    "track_only",
}


def check_mode(value: str) -> Mode:
    if value in MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MODE_VALUES!r}")
