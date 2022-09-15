#!/usr/bin/python3
""" Project 0x07. Python - Inheritance
    Task 3
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or it's parent class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
