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
    matrix_div = []

    if matrix == []:
        raise TypeError(msg)

    elif matrix is None:
        raise TypeError(msg)

    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError('division by zero')

    elif not isinstance(matrix, list) and isinstance(matrix, list):
        raise TypeError(msg)

    elif not isinstance(matrix[0], list):
        raise TypeError(msg)

    for x in matrix:

        if not isinstance(x, list):
            raise TypeError(msg)

        if len(x) != len(matrix[0]):
            raise TypeError(msg1)

        for z in x:
            if type(z) is not int and type(z) is not float:
                raise TypeError(msg)

    division = [[round(z / div, 2) for z in x] for x in matrix]
    return division
