#!/usr/bin/python3
"""
This module contains the MyList class
"""


class MyList(list):
    """
    A class that inherits from list and adds a sorting print method
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        Assumes all elements are integers.
        """
        print(sorted(self))
