#!/usr/bin/env python3
"""
Coroutine that takes in two arguments: an integer n and an integer max_delay.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Asynchronous function that measures the total execution time for wait_n(n,
    max_delay), and returns total_time / n.

    Args:
        n (int, optional): The number of times wait_random() will be called.

        max_delay (int, optional): The maximum delay in seconds.

    Returns:
        float: The average wait time.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
