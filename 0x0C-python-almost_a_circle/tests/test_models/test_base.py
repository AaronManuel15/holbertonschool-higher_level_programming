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
        classInstance1 = Base()
        self.assertEqual(classInstance1.id, 3)
        classInstance2 = Base()
        self.assertEqual(classInstance2.id, 4)
        classInstance3 = Base(89)
        self.assertEqual(classInstance3.id, 89)
        del classInstance1
        del classInstance2
        del classInstance3

    def test_to_json_string(self):
        listCheck = None
        self.assertEqual(Base.to_json_string(listCheck), '[]')
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(Base.to_json_string([dictionary]), '[{"x": 2, "y": 8, "id": 7, "height": 7, "width": 10}]')
        del r1
        del dictionary

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), \
                '[{"x": 2, "y": 8, "id": 5, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 6, "height": 4, "width": 2}]')
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        del r1
        del r2

    def test_load_from_file(self):
        pass
