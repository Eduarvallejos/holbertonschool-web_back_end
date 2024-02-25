#!/usr/bin/env python3
"""
This asynchronous function measures the runtime of executing
async_comprehension() four times concurrently.
It returns the total time taken.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine returning execution time
    of the async_comprehesion coroutine executed 4 times.

    Returns:
        float: Execution time of async_comprehension x 4.
    """
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    finish = time.perf_counter()
    return (finish - start)
