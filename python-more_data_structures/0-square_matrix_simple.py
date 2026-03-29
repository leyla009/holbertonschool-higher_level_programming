#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size
    # Each element is the square of the value in the original matrix
    return [[col ** 2 for col in row] for row in matrix]
