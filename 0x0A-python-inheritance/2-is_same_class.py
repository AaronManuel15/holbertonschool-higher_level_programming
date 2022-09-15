#!/usr/bin/python3
""" Project 0x07. Python - Inheritance
    Task 2
"""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of a_class"""
    if type(obj) == a_class:
        return True
    else:
        return False
