#!/usr/bin/python3
"""
This is the "0-add_integer" module.
This module provides one function, add_integer(a, b), which adds two numbers.
The function is designed to demonstrate Test Driven Development (TDD).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    The function first checks if a and b are integers or floats.
    If they are floats, they are casted to integers before addition.
    If they are not integers or floats, a TypeError is raised.

    Args:
        a: The first integer or float.
        b: The second integer or float (default is 98).

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
