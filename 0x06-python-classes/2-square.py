#!/usr/bin/python3
class Square:

    """ Class Square

        The __init__ creates a square with one attribute.

         Attributes:
        size (int): private instance attribute."""

    def __init__(self, size=0):
        var = 0
        try:
            var += size
            if size < 0:
                raise ValueError("{}".format("size must be >= 0"))
            self.__size = size
        except TypeError:
            raise TypeError("{}".format("size must be an integer"))
