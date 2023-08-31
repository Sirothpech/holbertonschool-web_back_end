#!/usr/bin/env python3
"""
Coroutine that will collect 10 random numbers using an async comprehensing
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[summary]

    Yields:
        Generator[float, None, None]: [description]
    """

    return [num async for num in async_generator()]
