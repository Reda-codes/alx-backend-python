#!/usr/bin/env python3
''' async routine '''
from typing import Callable, Awaitable


wait_random: Callable[[int], Awaitable[float]]
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list:
    '''wait_n function'''
    res: list = []
    for i in range(n):
        res.append(await wait_random(max_delay))
    return res
