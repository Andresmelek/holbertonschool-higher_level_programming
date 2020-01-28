#!/usr/bin/python3
"""Class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ square side """
        return self.width

    @size.setter
    def size(self, value):
        """ square sizes """
        self.width = value
        self.height = value

    def __str__(self):
        """ str method """
        return ("[Square] ({}) {}/{} - {}".format
               (self.id, self.x, self.y, self.width))
