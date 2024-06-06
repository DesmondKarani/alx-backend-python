#!/usr/bin/env python3
"""
This module defines a type-annotated function that returns
a tuple with a string and the square of an int or float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.

    Args:
        k (str): The string.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple containing
        the string and the squared number.
    """
    return (k, float(v ** 2))
