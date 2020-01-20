#!/usr/bin/python3
"""
Function that returns the list of available
attributes and methods of an object and
returns a list object.
"""


def lookup(obj):
    return (list(dir(obj)))
