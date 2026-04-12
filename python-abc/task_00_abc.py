#!/usr/bin/python3
"""
Module for Animal abstract base class and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal that serves as a blueprint for other animals.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass Dog that inherits from Animal.
    """

    def sound(self):
        """
        Implementation of the sound method for a Dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass Cat that inherits from Animal.
    """

    def sound(self):
        """
        Implementation of the sound method for a Cat.
        """
        return "Meow"
