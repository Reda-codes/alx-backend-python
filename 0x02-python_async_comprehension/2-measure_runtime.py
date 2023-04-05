#!/usr/bin/env python3
'''
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
'''
from asyncio import gather
from typing import List, Callable
import time


async_comprehension: Callable[[], List[float]]
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure_runtime function'''
    s = time.perf_counter()
    await gather(async_comprehension(),
                 async_comprehension(),
                 async_comprehension(),
                 async_comprehension(),
                 )
    elapsed = time.perf_counter() - s
    return elapsed
