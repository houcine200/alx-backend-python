#!/usr/bin/env python3
"""Defines an asynchronous coroutine."""
from typing import List
from asyncio import as_completed
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for random delays n times and returns sorted list of delays."""
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    delays = []
    for task in as_completed(tasks):
        delay = await (task)
        delays.append(delay)

    return delays