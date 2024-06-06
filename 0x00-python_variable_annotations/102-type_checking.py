#!/usr/bin/env python3
"""
This module defines a function that zooms into a
tuple by a given factor and returns a list.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms into a tuple by a given factor and returns a
    list of the repeated elements.

    Args:
        lst (Tuple[int, ...]): The tuple of integers to zoom into.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List[int]: A list of integers with each
        element repeated according to the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
