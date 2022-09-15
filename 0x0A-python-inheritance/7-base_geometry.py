#!/usr/bin/python3
""" Project 0x07. Python - Inheritance
    Task 6
"""


class BaseGeometry:
    """Class to contain geometric functions
    """
    def area(self):
        """area function with nothing currently implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates types and values of geometric attributes
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
