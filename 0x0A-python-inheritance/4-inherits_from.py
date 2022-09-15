#!/usr/bin/python3
""" Project 0x07. Python - Inheritance
    Task 4
"""


def inherits_from(obj, a_class):
    """ Checks if obj is an instance of a_class that inherited
        directly or indirectly from a_class
    """
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
