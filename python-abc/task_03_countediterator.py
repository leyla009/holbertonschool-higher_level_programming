#!/usr/bin/python3
"""
Module for CountedIterator class.
Tracks the number of items iterated over from an iterable.
"""


class CountedIterator:
    """
    An iterator wrapper that keeps track of the number of items fetched.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """
        Returns the current number of items iterated.
        """
        return self.__count

    def __next__(self):
        """
        Fetches the next item and increments the counter.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.__count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self
