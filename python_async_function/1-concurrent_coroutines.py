#!/usr/bin/env python3
"""
Coroutine that takes in an integer argument that waits for a random delay
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that takes in an integer argument that waits
    for a random delay and then returns a list of all the delays.

    Args:
        n (int, optional): The number of times wait_random() will be called.

        max_delay (int, optional): The maximum delay in seconds.

    Returns:
        float: A list of all the delays.
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
