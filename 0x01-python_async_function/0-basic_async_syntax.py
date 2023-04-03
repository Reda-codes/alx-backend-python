#!/usr/bin/env python3
import asyncio
import random
''' asynchronous coroutine '''


async def wait_random(max_delay=10: int) -> float:
    ''' wait_random function '''
    rdm: float = random.uniform(0, max_delay)
    await asyncio.sleep(rdm)
    return rdm
