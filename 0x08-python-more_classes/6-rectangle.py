#!/usr/bin/python3
"""define a Rectangle"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init for Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """prints the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        size = "#" * self.__width
        rect = []
        for index in range(self.__height):
            rect.append(size)
        return "\n".join(rect)

    def __repr__(self):
        """returns representation of the Rectangle"""
        return "{:s}({:d}, {:d})".format((type(self).__name__),
                                         self.__width, self.__height)

    def __del__(self):
        """kill the Rectangle, decrease instance count"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area getter"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the Rectangle,
        or nothing if height/width are 0"""
        if self.__height == 0 or self.__width == 0:
            return
        return (self.__height * 2) + (self.__width * 2)
