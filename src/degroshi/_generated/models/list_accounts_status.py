from typing import Literal

ListAccountsStatus = Literal["all", "closed", "open"]

LIST_ACCOUNTS_STATUS_VALUES: set[ListAccountsStatus] = {
    "all",
    "closed",
    "open",
}


def check_list_accounts_status(value: str) -> ListAccountsStatus:
    if value in LIST_ACCOUNTS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ACCOUNTS_STATUS_VALUES!r}")
