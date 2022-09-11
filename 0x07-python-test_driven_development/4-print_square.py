#!/usr/bin/python3
"""
    Project 0x05 - Test driven development
    Task 3
    Prints out a square built by #
"""


def print_square(size):
    """
        Prints out the square defined by size

        Args:
            size: _description_
    """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
