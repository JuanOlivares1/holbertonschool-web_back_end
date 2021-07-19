#!/usr/bin/env python3
""" Module """
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns first item of list """
    if lst:
        return lst[0]
    else:
        return None
