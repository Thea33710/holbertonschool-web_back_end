#!/usr/bin/env python3
"""
Docstring for 1-concurrent_coroutines.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay.
    Return the delays in ascending order without using sort().
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
