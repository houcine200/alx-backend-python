#!/usr/bin/env python3
"""
Measure total runtime of executing async_comprehension four times in parallel.
"""
from time import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Total runtime in seconds."""
    start_time = time()

    gather_param = [async_comprehension()]*4
    await asyncio.gather(*gather_param)

    end_time = time()
    execution_time = end_time - start_time
    return execution_time
