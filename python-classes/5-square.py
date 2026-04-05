#!/usr/bin/python3
"""Module that defines a Square class with a printing method."""


class Square:
    """A class that defines a square and can print its visual representation."""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): The length of a side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout.
        
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
