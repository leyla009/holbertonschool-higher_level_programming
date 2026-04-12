#!/usr/bin/python3
"""
Module for VerboseList class.
Extends the built-in list class to provide notifications.
"""


class VerboseList(list):
    """
    A list subclass that prints messages when items are added or removed.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends the list and prints the number of items added."""
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints a notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification before popping an item."""
        # We find the item first so we can name it in the print statement
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
