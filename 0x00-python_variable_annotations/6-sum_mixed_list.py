#!/usr/bin/env python3
"""
This module defines a type-annotated function for
summing a list of integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the list of numbers.
    """
    return sum(mxd_lst)
