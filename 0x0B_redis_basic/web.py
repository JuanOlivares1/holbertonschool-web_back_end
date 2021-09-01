#!/usr/bin/env python3
"""Module - web"""

import redis
import requests
from functools import wraps


_redis = redis.Redis()
url = "http://slowwly.robertomurray.co.uk"


def get_page(url: str) -> str:
    """request a page
    """
