#!/usr/bin/python3
"""
Module for Square class.
Inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle (9-rectangle.py).
    """

    def __init__(self, size):
        """
        Initializes the Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area (size * size).
        """
        return self.__size ** 2
