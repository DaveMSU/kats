import typing as tp
from functools import total_ordering


def binary_search(arr: tp.List[total_ordering], x: total_ordering) -> int:
    l, m, r = 0, len(arr) // 2, len(arr) - 1
    while l <= r:
        if arr[m] == x:
            return m
        else:
            l, r = (m + 1, r) if arr[m] < x else (l, m - 1)
            m = l // 2 + r // 2 + (l % 2) * (r % 2)
    return l
