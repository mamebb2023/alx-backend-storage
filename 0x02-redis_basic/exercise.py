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


def call_history(method: Callable) -> Callable:
    """ Stores input and output when a function is called """
    @functools.wraps(method)
    def add_to_history(self, *args, **kwargs):
        """ Adds to the list a new input and output """
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ":outputs", str(output))
        return output

    return add_to_history


def replay(method: Callable):
    """display the history of calls of a particular function."""
    r = redis.Redis()
    inputs = r.lrange(method.__qualname__ + ":inputs", 0, -1)
    outputs = r.lrange(method.__qualname__ + ":outputs", 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(inputs)))
    for input, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method.__qualname__,
              input.decode("utf-8"), output.decode("utf-8")))


class Cache:
    def __init__(self) -> None:
        """ Init Radis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
