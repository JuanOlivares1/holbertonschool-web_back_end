#!/usr/bin/env python3
""" Module """
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """ Returns first item of list """
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
