#!/usr/bin/env python3
"""
This script measures the average time taken by the wait_n function
to complete n times with a given maximum delay
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time taken by the wait_n function.

    Parameters:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay value.

    Returns:
        float: The average time taken per call to wait_n.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish = time.perf_counter()
    total_time = finish - start
    return total_time/n
