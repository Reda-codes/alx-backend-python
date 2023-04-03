#!/usr/bin/env python3
'''
measure_time function with integers n and max_delay
as arguments that measures the total execution time
for wait_n(n, max_delay)
'''
from typing import Callable, Awaitable, List
import asyncio
import time


wait_n: Callable[[int, int], Awaitable[List[float]]]
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure_time function'''
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed/n
