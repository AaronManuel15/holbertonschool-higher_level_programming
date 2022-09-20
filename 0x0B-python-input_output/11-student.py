#!/usr/bin/python3
"""Project 0x08. Python - Input/Output
Task 11
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary description"""

        if attrs is None:
            return (vars(self))
        attributes = {}
        for key, value in vars(self).items():
            if key in attrs:
                attributes[key] = value
        return (attributes)

    def reload_from_json(self, json):
        """Replaces the attributes with data from json file"""

        for key, value in json.items():
            setattr(self, key, value)
