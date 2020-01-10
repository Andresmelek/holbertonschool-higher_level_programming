#!/usr/bin/python3
class Square:

    """ Class Square
        The __init__ creates a square with one attribute.
         Attributes:
        size (int): private instance attribute."""

    def  __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("{}".format("size must be an integer"))
        elif size < 0:
            raise ValueError("{}".format("size must be >= 0"))
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            if self.__position[1] > 0:
                print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            print("#" * self.__size)
