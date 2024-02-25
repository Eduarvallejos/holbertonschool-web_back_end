#!/usr/bin/env python3
"""
This asynchronous comprehension function asynchronously generates a list
by iterating over the items yielded by the async_generator.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutotina that retrieves 10 random numbers asynchronously.

    Uses an asynchronous understanding on the async_generator coroutine
    to collect 10 random numbers.

    Returns:
        List[float]: List of 10 random numbers
    """
    return [i async for i in async_generator()]
