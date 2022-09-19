#!/usr/bin/python3
""" Project 0x08. Python - Input/Output
    Task 2
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8) and
    returns the number of characters added:
    """
    with open(filename, "a", encoding="utf=8") as f:
        stringLength = f.write(text)
    return stringLength
