#!/usr/bin/env python3
""" Redis With Python """
import functools
import redis
from typing import Union, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """ Count every time Cache is called """
    @functools.wraps(method)
    def increament(self, *args, **kwargs):
        """ Increases the count """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return increament

class Cache:
    def __init__(self) -> None:
        """ Init Radis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores a data with a random key """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Callable = None) -> Callable:
        """ Convert the data back to the desired format """
        value = self._redis.get(key)
        if value is None or fn is None:
            return value

        return fn(value)

    def get_str(self, key: str):
        """ Return value as string """
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str):
        """ Return value as int """
        return self.get(key, lambda x: int(x))
