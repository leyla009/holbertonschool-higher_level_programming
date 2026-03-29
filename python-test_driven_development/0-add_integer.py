#!/usr/bin/python3
"""
This is the "0-add_integer" module.
This module provides one function, add_integer(a, b).
The function takes two arguments, casts them to integers if they are floats,
and returns their sum. It is a part of a TDD project.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats together.

    Args:
        a: The first integer or float.
        b: The second integer or float (defaults to 98).

    Raises:
        TypeError: If either a or b is not an integer or a float,
        or if they are NaN or Infinity.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or abs(a) == float('inf'):
        raise TypeError("a must be an integer")
    if b != b or abs(b) == float('inf'):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
