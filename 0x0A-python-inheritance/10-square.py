#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Public methods instance
"""


class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
