#!/usr/bin/python3
"""
This module provides the 'matrix_divided' function.
It divides all elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number (int or float) to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix with the results rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Check if matrix is a list of lists
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        
        # 2. Check if all elements in row are int/float
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 3. Check if all rows are the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # 4. Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 5. Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 6. Return new matrix with rounded values
    return [[round(x / div, 2) for x in row] for row in matrix]
