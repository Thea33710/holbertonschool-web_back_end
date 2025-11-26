#!/usr/bin/env python3
"""
Docstring for 4-tasks.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay.
    Return delays in ascending order as tasks complete.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
