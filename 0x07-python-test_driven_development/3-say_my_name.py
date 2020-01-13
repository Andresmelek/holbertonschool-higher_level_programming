#!/usr/bin/python3
"""
Function that prints
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Check conditionals
    """
    if not isinstance(first_name(str):
         raise TypeError('first_name must be a string')
    if first_name is None:
         raise TypeError('first_name must be a string')
    if not isinstance(last_name(str):
         raise TypeError('last_name must be a string')
    if last_name is None:
         raise TypeError('last_name must be a string')
    print("My name is {0:s} {1:s}".format(first_name, last_name))
