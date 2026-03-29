#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function ensures that arguments are either integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
