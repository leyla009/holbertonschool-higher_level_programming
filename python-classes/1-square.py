#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initializes the square.

        Args:
            size: The length of a side of the square.
        """
        self.__size = size
