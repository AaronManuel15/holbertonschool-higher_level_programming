#!/usr/bin/python3
""" Project 0x07. Python - Inheritance
    Task 8
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class to contain attributes of the rectangle geometric shape
    """
    def __init__(self, width, height):
        """Validates values/types and initializes
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
