from typing import Literal

EndpointResponseDisabledReasonType0 = Literal["failing", "owner_left"]

ENDPOINT_RESPONSE_DISABLED_REASON_TYPE_0_VALUES: set[EndpointResponseDisabledReasonType0] = {
    "failing",
    "owner_left",
}


def check_endpoint_response_disabled_reason_type_0(value: str) -> EndpointResponseDisabledReasonType0:
    if value in ENDPOINT_RESPONSE_DISABLED_REASON_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_RESPONSE_DISABLED_REASON_TYPE_0_VALUES!r}")
