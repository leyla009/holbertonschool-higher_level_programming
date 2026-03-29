#!/usr/bin/python3
"""This module divides a matrix elements to a number."""


def matrix_divided(matrix, div):
    """Divide matrix by a num"""

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)-1):
        if len(matrix[i]) != len(matrix[i+1]):
            raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError(
                    "matrix must be a matrix" +
                    " (list of lists) of integers/floats"
                    )

    new = []
    for i in matrix:
        row = []
        for j in i:
            row.append(round(j/div, 2))
        new.append(row)

    return new
