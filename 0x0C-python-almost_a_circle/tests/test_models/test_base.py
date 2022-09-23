#!/usr/bin/python3
"""unit testing for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestBase(unittest.TestCase):
    """class for testing Base class"""

    def test_docstrings(self):
        self.assertIsNotNone(__import__('models').base.__doc__)
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_instance(self):
        classInstance = Base()
        self.assertEqual(classInstance.id, 1)
        classInstance = Base()
        self.assertEqual(classInstance.id, 2)
        classInstance = Base(89)
        self.assertEqual(classInstance.id, 89)

    def test_to_json_string(self):
        listCheck = None
        self.assertEqual(Base.to_json_string(listCheck), '[]')
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(Base.to_json_string([dictionary]), '[{"x": 2, "y": 8, "id": 3, "height": 7, "width": 10}]')

    def test_save_to_file(self):
        listCheck = None
        Base.save_to_file(listCheck)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[]')
