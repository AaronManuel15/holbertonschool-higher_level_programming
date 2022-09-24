#!/usr/bin/python3
"""Unit testing for Square class"""
import unittest
from models.base import Base
from models.square import Square
from unittest.mock import patch
from io import StringIO

class TestSquare(unittest.TestCase):
    """class for testing Square class"""

    def test_docstrings(self):
        self.assertIsNotNone(__import__('models').rectangle.__doc__)
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)
