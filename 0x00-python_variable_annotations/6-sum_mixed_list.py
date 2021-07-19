#!/usr/bin/env python3
""" Module """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of all list's items """
    sum: float = 0

    for n in mxd_lst:
        sum += n
    return sum
