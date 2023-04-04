#!/usr/bin/env python3
'''
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
'''
import asyncio
from typing import List, Callable
import time


async_comprehension: Callable[[], List[float]]
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure_runtime function'''
    s = time.()
    await asyncio.gather(
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         )
    e = time()
    return s - e
