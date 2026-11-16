from typing import Literal

RotateSecretRequestOverlapHours = Literal[0, 1, 24, 72]

ROTATE_SECRET_REQUEST_OVERLAP_HOURS_VALUES: set[RotateSecretRequestOverlapHours] = {
    0,
    1,
    24,
    72,
}


def check_rotate_secret_request_overlap_hours(value: int) -> RotateSecretRequestOverlapHours:
    if value in ROTATE_SECRET_REQUEST_OVERLAP_HOURS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROTATE_SECRET_REQUEST_OVERLAP_HOURS_VALUES!r}")
