#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that takes in an integer argument that waits
    for a random delay and then returns a list of all the delays.

    Args:
        n (int, optional): The number of times wait_random() will be called.

        max_delay (int, optional): The maximum delay in seconds.

    Returns:
        float: A list of all the delays.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
        delays = await asyncio.gather(*tasks)
    return sorted(delays)
