#!/usr/bin/env python3
""" Module - pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple of size two containing a start and end index """
    return ((page - 1) * page_size, page * page_size)
