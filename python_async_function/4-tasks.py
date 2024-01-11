#!/usr/bin/env python3
""" basic async syntax """


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ calls wait_random n times """
    result = []
    for i in range(n):
        result.append(task_wait_random(max_delay))
    result = await asyncio.gather(*result)
    return sorted(result)
