#!/usr/bin/env python3
"""
Coroutine that takes in an integer argument that waits for a random delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that generates a random delay and waits
    for that amount of time before returning a float value.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: A float value representing the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
