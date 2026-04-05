#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.

        Args:
            size (int): The length of a side of the square.
            position (tuple): Two positive integers representing coordinates.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__size

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character, considering position."""
        if self.__size == 0:
            print("")
            return

        # Handle vertical offset (y-coordinate)
        [print("") for i in range(self.__position[1])]

        # Handle horizontal offset (x-coordinate) and print square
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
