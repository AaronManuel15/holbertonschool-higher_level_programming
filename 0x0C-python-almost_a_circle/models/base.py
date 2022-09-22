#!/usr/bin/python3
""" Project 0x0C. Python - Almost a circle
    Task 0
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string rep of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string rep of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        listDict = []
        for obj in list_objs:
            listDict.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf=8") as f:
            f.write(cls.to_json_string(listDict))
