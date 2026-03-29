#!/usr/bin/python3
"""
Module 0-add_integer: Provides one function, add_integer(a, b).
This module is part of the TDD project.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).

    Args:
        a: First number.
        b: Second number, defaults to 98.

    Returns:
        The integer addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
