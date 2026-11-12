"""Money as Decimal. The API sends amounts as strings ("642.30"); the generated models read them through
decimal_in and write them through decimal_out (the generator's post-processing rewrites the decimal fields after each
generation). Never float."""

from decimal import Decimal
from typing import Any


def decimal_in(value: Any) -> Any:
    """A decimal string from the API as Decimal; UNSET and None pass through."""
    if isinstance(value, str):
        return Decimal(value)
    return value


def decimal_out(value: Any) -> Any:
    """A Decimal as the string the API takes, without an exponent."""
    if isinstance(value, Decimal):
        return format(value, "f")
    return value
