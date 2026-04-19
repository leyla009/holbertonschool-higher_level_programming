#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Start the new row with 1
        current_row = [1]

        # Calculate the values between the first and last 1
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # End the new row with 1
        current_row.append(1)
        triangle.append(current_row)

    return triangle
