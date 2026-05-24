#!/usr/bin/python3
"""A module that defines a class that prevents dynamic attribute creation."""


class LockedClass:
    """A class that prevents the user from creating new instance attributes."""
    __slots__ = ['first_name']
