#!/usr/bin/python3
""" Project 0x0C. Python - Almost a circle
    Task 1
"""
from models.base import Base


class Rectangle(Base):
    """ Defines a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes attributes for a rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Setter for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Setter for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle
        """
        return (self.__height * self.__width)

    def display(self):
        """ Displays a graphical representation of the rectangle
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ String description of the rectangle
        """
        return "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/" \
            + str(self.__y) + " - " + str(self.__width) + "/" \
            + str(self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute
        """
        if len(args) > 0:
            attribute = ['id', 'width', 'height', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, attribute[arg], args[arg])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
