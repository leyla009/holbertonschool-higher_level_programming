#!/usr/bin/python3
"""
Module for Rectangle class.
Inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry (7-base_geometry.py).
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            The area (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description for print() and str().

        Returns:
            str: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
