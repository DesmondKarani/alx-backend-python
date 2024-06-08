#!/usr/bin/env python3
"""
This module provides a function to safely retrieve values from a dictionary.
It utilizes type annotations to specify the types of parameters and
return values.
"""


from typing import TypeVar, Any, Mapping, Union

# Create a TypeVar T that can be any type.
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Retrieve a value from a dictionary or return a default value if
    the key is not found.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value
        to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found,
        otherwise the default.
    """
    return dct.get(key, default)
