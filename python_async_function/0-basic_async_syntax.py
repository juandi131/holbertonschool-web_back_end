#!/usr/bin/env python3
""" basic async syntax """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waits a random time """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
