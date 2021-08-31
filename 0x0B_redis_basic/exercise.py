#!/usr/bin/env python3
"""Module - Excersise"""

import redis
from uuid import uuid4
from typing import Union


class Cache():
    """Cache class for red"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis db
        """
        key = uuid4()
        key = str(key)
        self._redis.mset({key: data})
        return key
