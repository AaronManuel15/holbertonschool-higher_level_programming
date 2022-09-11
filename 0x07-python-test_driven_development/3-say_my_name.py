#!/usr/bin/python3
"""
    Project 0x05 - Test driven development
    Task 2
    Prints out a sentence declaring name
"""


def say_my_name(first_name, last_name=""):
    """
        Prints out given names

        Args:
            first_name: _description_
            last_name: _description_
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    fullname = first_name + ' ' + last_name
    print("My name is", fullname)
