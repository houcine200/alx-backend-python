#!/usr/bin/env python3
"""Asynchronous coroutine that waits for a random delay and returns it."""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay and returns it."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
