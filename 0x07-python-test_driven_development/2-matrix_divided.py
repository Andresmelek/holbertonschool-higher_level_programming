#!/usr/bin/python3
"""
Function that divides all the elements
of a matrix, the list must be of integers
or floats, each row of the matrix must be
the same size, the division cannot be 0,
returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Check conditionals
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    matriz = len(matrix)
    matrix_div = []
    if not isinstance(matrix(int, float)):
        raise TypeError(msg)
    if matrix is None:
        raise TypeError(msg)
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix(int, list)):
        raise TypeError(msg)

    for i in range(len(matrix)):
        if len(matrix[i]) != matriz:
            raise TypeError(msg)

    for y in i:
        if not isinstance(y, (int, list)):
            raise TypeError(msg)

    matrix_div = [[round(y / div, 2) for y in i] for i in matrix]
    return matrix_div
