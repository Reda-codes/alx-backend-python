#!/usr/bin/env python3
'''
coroutine called async_generator that takes no arguments
it will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''async_generator function'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
