#!/usr/bin/python3
""" Project 0x08. Python - Input/Output
    Task 1
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8) and
        returns the number of characters written:
    """
    with open(filename, "w", encoding="utf=8") as f:
        stringLength = f.write(text)
    return stringLength
