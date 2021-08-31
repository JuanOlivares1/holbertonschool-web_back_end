#!/usr/bin/env python3
"""Module - Excersise"""

import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts the number of times a method is called
    """
    @wraps(method)
    def f(self, data):
        self._redis.incr(method.__qualname__)
        return method(self, data)
    return f


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular function
    """
    inputs_k = method.__qualname__ + ":inputs"
    outputs_k = method.__qualname__ + ":outputs"

    @wraps(method)
    def f(self, args):
        self._redis.rpush(inputs_k, str(args))
        output = method(self, args)
        self._redis.rpush(outputs_k, output)
        return output
    return f


class Cache():
    """Cache class for redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
