#!/usr/bin/python3
""" Class that inheritances from Base """
from models.base import Base


class Rectangle(Base):
    """ Class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Rectangle's width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Rectangle's height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ X getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ Returns the rectangle's area """
        return self.__width * self.__height

    def display(self):
        """ Draws a rectangle """
        for e in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """ string method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
               (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ updates the rectangle class """
        list_at = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, list_at[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary representation """
        keys = ['id', 'width', 'height', 'x', 'y']
        values = [self.id, self.__width, self.__height, self.__x, self.__y]
        return dict(zip(keys, values))
