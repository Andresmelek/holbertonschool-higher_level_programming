#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = '#'
    """ Class Rectangle
        The __init__ creates a rectangle with two attriutes.
        Attributes:
        width = has the width of the rectangle
        height = has the height of the rectangle. """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            result += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2

    @classmethod
    def square(cls, size=0):
        new_s = cls()
        new_s.width = size
        new_s.height = size
        return new_s
