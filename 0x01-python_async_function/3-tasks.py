#!/usr/bin/env python3
"""
This module contains a function to create an asyncio.Task.
"""


import asyncio

# Dynamic import using __import__
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
