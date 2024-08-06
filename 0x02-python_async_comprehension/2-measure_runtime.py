#!/usr/bin/env python3
'''Implementation of Task 2
'''
import asyncio
from typing import Tuple
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension four times in
        parallel and measures total runtime.
    '''
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
