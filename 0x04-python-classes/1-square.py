#!/usr/bin/python3

"""Creating class square with exceptions"""


class Square:
    """This is the Square"""
    def __init__(self, size=0):
        """Adding private size attribute with if guards"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
