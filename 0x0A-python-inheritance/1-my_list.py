#!/usr/bin/python3
""" Project 0x07. Python - Inheritance
    Task 1
"""


class MyList(list):
    """Class that inherits from list
    """

    def print_sorted(self):
        """ Function to print the list, but sorted in ascending
        """
        print(sorted(self))
