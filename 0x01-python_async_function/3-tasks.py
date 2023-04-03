#!/usr/bin/env python3
'''
function task_wait_random that takes an integer
max_delay and returns a asyncio.Task
'''
from typing import Callable, Awaitable
import asyncio


wait_random: Callable[[int], Awaitable[float]]
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''task_wait_random function'''
    return asyncio.create_task(wait_random(max_delay))
