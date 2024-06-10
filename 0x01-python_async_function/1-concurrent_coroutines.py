#!/usr/bin/env python3
"""
Module containing the wait_n coroutine which spawns wait_random n times.
"""


import asyncio
from typing import List
from _import_('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called wait_n that takes in 2 int arguments n and max_delay.
    Spawns wait_random n times, and returns a list of delays.
    """

    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))

    return sorted(delays)
