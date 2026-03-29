#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([4]), 4)

    def test_positive_integers(self):
        """Test a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the maximum is at the beginning."""
        self.assertEqual(max_integer([9, 3, 5, 1]), 9)

    def test_max_at_end(self):
        """Test when the maximum is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_negative_integers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-4, -2, -8, -1]), -1)

    def test_mixed_integers(self):
        """Test a list of positive and negative integers."""
        self.assertEqual(max_integer([-10, 2, 7, -3]), 7)

    def test_repeated_values(self):
        """Test a list with repeated maximum values."""
        self.assertEqual(max_integer([2, 5, 5, 1]), 5)

    def test_float_list(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 3.2, 2.8]), 3.2)

    def test_single_negative(self):
        """Test a list with one negative number."""
        self.assertEqual(max_integer([-7]), -7)

    def test_string(self):
        """Test a string as sequence input."""
        self.assertEqual(max_integer("Baking"), "n")


if __name__ == "__main__":
    unittest.main()
