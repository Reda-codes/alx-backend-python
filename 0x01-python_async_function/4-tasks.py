#!/usr/bin/env python3
''' async routine '''
from typing import Callable, Awaitable, List
import asyncio


wait_random: Callable[[int], Awaitable[float]]
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''task_wait_n function'''
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
