from typing import Literal

EndpointResponseState = Literal["active", "disabled", "paused"]

ENDPOINT_RESPONSE_STATE_VALUES: set[EndpointResponseState] = {
    "active",
    "disabled",
    "paused",
}


def check_endpoint_response_state(value: str) -> EndpointResponseState:
    if value in ENDPOINT_RESPONSE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_RESPONSE_STATE_VALUES!r}")
