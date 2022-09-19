#!/usr/bin/python3
""" Project 0x08. Python - Input/Output
    Task 4
"""
import json


def from_json_string(my_str):
    """ returns an object (Python data structure) represented by a JSON string:
    """
    return json.loads(my_str)
