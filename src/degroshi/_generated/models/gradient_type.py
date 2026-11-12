from typing import Literal

GradientType = Literal["conic", "linear", "radial"]

GRADIENT_TYPE_VALUES: set[GradientType] = {
    "conic",
    "linear",
    "radial",
}


def check_gradient_type(value: str) -> GradientType:
    if value in GRADIENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRADIENT_TYPE_VALUES!r}")
