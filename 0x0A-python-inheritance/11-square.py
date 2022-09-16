#!/usr/bin/python3
""" Project 0x07. Python - Inheritance
    Task 11
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class to contain attributes of the square geometric shape
    """
    def __init__(self, size):
        """Validates values/types and initializes
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Redifines the calculation for area of a square
        """
        return (self.__size ** 2)

    def __str__(self):
        """Returns the details of the rectangle
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
