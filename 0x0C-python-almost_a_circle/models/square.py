#!/usr/bin/python3
"""Class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ str method """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ updated the square class """
        list_a = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, list_a[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary representation """
        keys = ['id', 'size', 'x', 'y']
        values = [self.id, self.width, self.x, self.y]
        return dict(zip(keys, values))
