#!/usr/bin/python3
"""Unit testing for Square class"""
from re import S
import unittest
from models.base import Base
from models.square import Square
from unittest.mock import patch
from io import StringIO

class TestSquare(unittest.TestCase):
    """class for testing Square class"""

    def test_docstrings(self):
        self.assertIsNotNone(__import__('models').square.__doc__)
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_init(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(s1.id, 1)
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            Square("string")
        with self.assertRaises(TypeError):
            Square(1, "string")
        with self.assertRaises(TypeError):
            Square(1, 1, "string", 1)
        with self.assertRaises(TypeError):
            Square(None)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)
        with self.assertRaises(ValueError):
            Square(1, -1, 1)

    def test_area(self):
        rect2 = Square(5)
        self.assertEqual(rect2.area(), 25)
        del rect2

    def test_display(self):
        pass

    def test_str(self):
        r = Square(4, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Square] (12) 2/1 - 4")
        r = Square(5, 1)
        self.assertEqual(r.__str__(), f"[Square] ({r.id}) 1/0 - 5")
