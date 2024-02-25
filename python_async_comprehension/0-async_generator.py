#!/usr/bin/env python3
"""
This asynchronous generator function generates random numbers
between 0 and 10 and yields them with a delay of 1 second.
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that generates random values ​​between 0 and 10
    asynchronously.

    Each iteration waits 1 second to produce the next number.

    Yields:
        float: Float between 0 and 10.
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
