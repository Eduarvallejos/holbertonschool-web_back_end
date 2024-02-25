#!/usr/bin/env python3
"""
This asynchronous generator function generates random numbers
between 0 and 10 and yields them with a delay of 1 second.
"""
import random
import asyncio


async def async_generator():
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == '__main__':
    async_generator()
