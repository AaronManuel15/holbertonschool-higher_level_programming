#!/usr/bin/python3
"""Project 0x08. Python - Input/Output
Task 8
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the description"""

        return (vars(self))
