#!usr/bin/env python3
"""0. Writing strings to Redis
"""

from typing import Union
import redis
import uuid


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
