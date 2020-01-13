#!/usr/bin/python3
"""
Function that adds 2 integers,
the integers must be integers or floats
and returns the addition of them,
"""


def add_integer(a, b=98):
    """
    Check the conditionals.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
