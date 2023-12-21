#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

cache.store("data")
cache.store("foo")
cache.store(43)
cache.store("cold")

replay(cache.store)
