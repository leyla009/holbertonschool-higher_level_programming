#!/usr/bin/python3
"""This module contains an abstract base class Shape and its subclasses."""
from abc import ABC, abstractmethod
import math as m


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = abs(radius)

    def area(self):
        """Return area of the circle."""
        return m.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of the circle."""
        return 2 * m.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
