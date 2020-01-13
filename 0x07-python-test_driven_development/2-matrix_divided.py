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
    msg = "matrix must be a matrix (list of lists) of integers/float"
    msg1 = "Each row of the matrix must have the same size"
    matriz = len(matrix[0])
    matrix_div = []
    if matrix is None:
        raise TypeError(msg)
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not int and type(matrix) is not list:
        raise TypeError(msg)

    for x in range(len(matrix)):
        if len(matrix[x]) != matriz:
            raise TypeError(msg1)

    for x in matrix:
        if not isinstance(matrix, list):
            raise TypeError(msg)
        for y in x:
            if type(y) is not int or type(y) is not float:
                raise TypeError(msg)

    matrix_div = [[round(y / div, 2) for y in i] for i in matrix]
    return matrix_div
