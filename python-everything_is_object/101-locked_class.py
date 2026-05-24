#!/usr/bin/python3
"""A module that defines a class that prevents dynamic attribute creation."""


class LockedClass:
    __slots__ = ['first_name']
