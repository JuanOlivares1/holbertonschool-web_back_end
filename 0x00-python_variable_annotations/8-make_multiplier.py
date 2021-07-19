#!/usr/bin/env python3
""" Module """
from typing import Callable, Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns tuple """
    def mult(n: float) -> float:
        return n * multiplier
    return mult
