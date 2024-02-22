#!/usr/bin/env python3
"""
This script defines an asynchronous function called wait_n
that waits for a list of random delays.
It takes two integer arguments: n, the number of random delays to wait for,
and max_delay, the maximum value a delay can have.
Returns a list of the obtained delays, sorted in ascending order.
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for a list of random delays.

    Arguments:
    - n: number of random delays to wait
    - max_delay: the maximum value that a delay can have

    Returns:
    - List of delay times, in ascending order
    """
    delay_list = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list)
