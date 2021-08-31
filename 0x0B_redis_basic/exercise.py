#!/usr/bin/env python3
"""Module - Excersise"""

import redis
from uuid import uuid4
from typing import Union, Callable


class Cache():
    """Cache class for redis"""
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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int]:
        """Format data recived from redis
        """
        data = self._redis.get(key)
        if data is None:
            return None
        elif fn is None:
            return data
        else:
            return fn(data)

    def get_str(self, data) -> str:
        """Formats data to str"""
        return data.decode("utf-8")

    def get_int(self, data) -> int:
        """Formats data to str"""
        return int(data)
