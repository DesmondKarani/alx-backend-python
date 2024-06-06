#!/usr/bin/env python3
"""
This module defines a function with type annotations
that safely gets a value from a dictionary.
"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Returns the value for a given key in a dictionary if
    it exists, otherwise returns a default value.

    Args:
        dct (Mapping[Any, Any]): The dictionary.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value for the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
