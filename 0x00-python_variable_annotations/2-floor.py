#!/usr/bin/env python3
"""
This module defines a type-annotated function for calculating the floor of a float.
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor of a float number.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of the float number.
    """
    return math.floor(n)
