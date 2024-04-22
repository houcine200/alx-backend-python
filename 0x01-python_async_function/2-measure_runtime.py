#!/usr/bin/env python3
"""Script to measure the runtime of an asynchronous coroutine"""
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int):
    """Measure the execution time of an asynchronous coroutine"""
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    execution_time = end_time - start_time
    return execution_time / n
