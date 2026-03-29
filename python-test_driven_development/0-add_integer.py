#!/usr/bin/python3
"""
This module provides a function add_integer(a, b).
The function adds two integers or floats together after
casting them to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first integer
        b: second integer, defaults to 98

    Returns:
        The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
