#!/usr/bin/python3
""" Project 0x0C. Python - Almost a circle
    Task 0
"""


class Base:
    """ Base class to manage id attribute in all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes information for base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
