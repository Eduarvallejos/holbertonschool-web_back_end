#!/usr/bin/env python3
"""
This asynchronous function takes an integer n and
an integer max_delay and returns a sorted list of floats
"""
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Measure the time taken by the wait_n function.

    Parameters:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay value.

    Returns:
        float: The average time taken per call to wait_n.
    """
    delay_list = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list)
