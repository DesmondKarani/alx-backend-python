#!/usr/bin/env python3
"""
This module defines a type-annotated function for summing a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of float numbers.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the list of float numbers.
    """
    return sum(input_list)
