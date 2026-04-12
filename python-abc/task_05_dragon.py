#!/usr/bin/python3
"""
Module for Mixin classes and the Dragon class.
Demonstrates how to compose behaviors using mixins.
"""


class SwimMixin:
    """Mixin to provide swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to provide flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from both SwimMixin and FlyMixin.
    Composes swimming and flying behaviors.
    """

    def roar(self):
        """Prints a roaring message unique to the Dragon."""
        print("The dragon roars!")
