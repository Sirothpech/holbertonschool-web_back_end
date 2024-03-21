#!/usr/bin/env python3
"""4. Retrieving lists
"""

from functools import wraps
from typing import Callable, Optional, Union
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorator that counts how many times a function is called."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that store the history of inputs and outputs for a function"""

    @wraps(method)
    def wrapper(self, *args):
        """Wrapper function"""
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        result = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(result))
        return result
    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls of a particular function"""

    name = method.__qualname__
    r = redis.Redis()

    inputs = method.__qualname__ + ':inputs'
    outputs = method.__qualname__ + ':outputs'

    inputs_list = r.lrange(inputs, 0, -1)
    outputs_list = r.lrange(outputs, 0, -1)

    print(f"{name} was called {len(inputs_list)} times:")

    for i, o in zip(inputs_list, outputs_list):
        print(f"{name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


class Cache:
    """Cache class to store data in Redis"""
    def __init__(self) -> None:
        """Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the input data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis database"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """Get data from redis database"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """Convert bytes to string"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """Convert bytes to int"""
        return int.from_bytes(data, byteorder='big')
