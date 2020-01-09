#!/usr/bin/python3
class Square:

    """ Class Square
        The __init__ creates a square with one attribute.
         Attributes:
        size (int): private instance attribute."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("{}".format("size must be an integer"))
        if size < 0:
            raise ValueError("{}".format("size must be >= 0"))
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
