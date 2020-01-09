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
        if type(value) is not int:
            raise TypeError("{}".format("size must be an integer"))
        if value < 0:
            raise ValueError("{}".format("size must be >= 0"))
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("{}".format('#') * self.__size)
