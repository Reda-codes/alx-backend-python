#!/usr/bin/env python3
import time
import random
'''
coroutine called async_generator that takes no arguments
it will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10
'''


async def async_generator():
    '''async_generator function'''
    for i in range(10):
        time.sleep(1)
        yield random.uniform(0, 10)
