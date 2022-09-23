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
        if list_objs is not None:
            for obj in list_objs:
                listDict.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf=8") as f:
            f.write(cls.to_json_string(listDict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummyInstance = cls(1, 1)
        else:
            dummyInstance = cls(1)
        dummyInstance.update(**dictionary)
        return dummyInstance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        """
        CompleteList = []
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                DictList = cls.from_json_string(f.read())
                for dict in DictList:
                    CompleteList.append(cls.create(**dict))
                return CompleteList
        except FileNotFoundError:
            return CompleteList
