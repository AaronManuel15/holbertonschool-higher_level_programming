#!/usr/bin/python3
"""Unit testing for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """class for testing Rectangle class"""
    
    def test_docstrings(self):
        self.assertIsNotNone(__import__('models').rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_init(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
        Rectangle(3, 5)
        self.assertEqual(Base._Base__nb_objects, 1)
        rect1 = Rectangle(5, 5, 0, 0, 1)
        self.assertEqual(rect1.id, 1)

    def test_InputErrors(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 2)
        with self.assertRaises(TypeError):
            Rectangle("string", 1)
        with self.assertRaises(TypeError):
            Rectangle(1, "string again")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "string", 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "String")
        with self.assertRaises(TypeError):
            Rectangle(None)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)
