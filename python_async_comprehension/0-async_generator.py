#!/usr/bin/env python3
"""
Docstring for 0-async_generator.
"""
import asyncio
import random


async def async_generator():
    """
    Yield a random number between 0 and 10,
    10 times, with a 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
