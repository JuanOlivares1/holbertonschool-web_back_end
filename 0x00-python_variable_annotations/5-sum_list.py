#!/usr/bin/env python3
""" Module """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of all list's items """
    sum: float = 0

    for n in input_list:
        sum += n
    return sum
