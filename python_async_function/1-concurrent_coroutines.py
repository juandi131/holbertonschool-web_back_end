#!/usr/bin/env python3
""" basic async syntax """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ calls wait_random n times """
    result = []
    for i in range(n):
        result.append(wait_random(max_delay))
    result = await asyncio.gather(*result)
    return sorted(result)
