#!/usr/bin/env python3
""" Redis With Python """
import radis
from typing import Union


class Cache:
    def __init__(self) -> None:
        """ Init Radis """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores a data with a random key """
        random_key = str(uuid4())
        self._radis.set(random_key, data)
        return random_key
