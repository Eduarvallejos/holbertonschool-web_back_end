#!/usr/bin/env python3
"""This script defines an asynchronous function called wait_random
that waits for a random delay time between 0 and
a maximum value (default 10) seconds, and finally returns that delay time.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous random function, which uses random."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
