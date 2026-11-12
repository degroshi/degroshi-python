from typing import Literal

MySpaceResponseKind = Literal["business", "personal"]

MY_SPACE_RESPONSE_KIND_VALUES: set[MySpaceResponseKind] = {
    "business",
    "personal",
}


def check_my_space_response_kind(value: str) -> MySpaceResponseKind:
    if value in MY_SPACE_RESPONSE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MY_SPACE_RESPONSE_KIND_VALUES!r}")
