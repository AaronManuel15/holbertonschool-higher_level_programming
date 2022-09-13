#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -3, -5]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer(a), a)
        self.assertEqual(max_integer("string", "s"))

    def test_invalid(self):
        self.assertRaises(TypeError, max_integer, [5, "string", 10])
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
