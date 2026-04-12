#!/usr/bin/python3
"""
Module for Shape abstract class and its subclasses Circle and Rectangle.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape that defines the blueprint for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Concrete class Circle that inherits from Shape.
    """

    def __init__(self, radius):
        """Initializes Circle with a radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle: pi * r^2"""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle: 2 * pi * abs(r)"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Concrete class Rectangle that inherits from Shape.
    """

    def __init__(self, width, height):
        """Initializes Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle: width * height"""
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Returns the perimeter of the rectangle: 2 * (w + h)"""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """
    Standalone function that uses Duck Typing to print shape information.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
