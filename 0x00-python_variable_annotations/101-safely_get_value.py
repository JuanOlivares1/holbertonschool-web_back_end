#!/usr/bin/env python3
""" Module """
from typing import Union, Any, TypeVar, Mapping
dd = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[dd, None] = None):
    """ Returns first item of list """
    if key in dct:
        return dct[key]
    else:
        return default
