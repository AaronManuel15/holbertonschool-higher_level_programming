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
        del rect1

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

    def test_area(self):
        rect2 = Rectangle(5, 5)
        self.assertEqual(rect2.area(), 25)
        del rect2

    def test_display(self):
        pass

    def test_str(self):
        rect3 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(rect3.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        del rect3

    def test_update(self):
        rect4 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(rect4.id, 10)
        self.assertEqual(rect4.width, 10)
        self.assertEqual(rect4.height, 10)
        self.assertEqual(rect4.x, 10)
        self.assertEqual(rect4.y, 10)
        rect4.update(89, 2, 3, 4, 5)
        self.assertEqual(rect4.id, 89)
        self.assertEqual(rect4.width, 2)
        self.assertEqual(rect4.height, 3)
        self.assertEqual(rect4.x, 4)
        self.assertEqual(rect4.y, 5)
        rect4 = Rectangle(10, 10, 10, 10, 10)
        rect4.update(height=1, width=1, x=2, id=89, y=3)
        self.assertEqual(rect4.id, 89)
        self.assertEqual(rect4.width, 1)
        self.assertEqual(rect4.height, 1)
        self.assertEqual(rect4.x, 2)
        self.assertEqual(rect4.y, 3)
        del rect4

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertIsInstance(r1_dictionary, dict)
        self.assertIsNot(r2, r1)
