#!/usr/bin/env python3
""" Module """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """ Returns tuple """
    n: float = v * v
    return (k, n)
