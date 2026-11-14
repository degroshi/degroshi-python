from typing import Literal

ChangeOp = Literal["delete", "upsert"]

CHANGE_OP_VALUES: set[ChangeOp] = {
    "delete",
    "upsert",
}


def check_change_op(value: str) -> ChangeOp:
    if value in CHANGE_OP_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHANGE_OP_VALUES!r}")
