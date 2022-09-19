#!/usr/bin/python3
""" Project 0x08. Python - Input/Output
    Task 5
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation:
    """
    with open(filename, "w", encoding="utf=8") as f:
        return json.dump(my_obj, f)
