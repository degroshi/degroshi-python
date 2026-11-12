from typing import Literal

ListTransactionsSort = Literal["amount_asc", "amount_desc", "date_asc", "date_desc", "updated_asc"]

LIST_TRANSACTIONS_SORT_VALUES: set[ListTransactionsSort] = {
    "amount_asc",
    "amount_desc",
    "date_asc",
    "date_desc",
    "updated_asc",
}


def check_list_transactions_sort(value: str) -> ListTransactionsSort:
    if value in LIST_TRANSACTIONS_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_TRANSACTIONS_SORT_VALUES!r}")
