#!/usr/bin/env python3
"""
Module containing the wait_n coroutine which spawns wait_random n times.
"""


import asyncio
from typing import List

# Dynamic import using __import__
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with specified max_delay & returns delays list.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: List of delay values in ascending order.
    """
    delays: List[float] = await asyncio.gather(
            *(wait_random(max_delay
                          ) for _ in range(n)))
    return sorted(delays)
