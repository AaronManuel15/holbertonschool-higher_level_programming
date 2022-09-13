#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer function
    """

    def test_valid(self):
        """Testing positive int"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        """Testing negatives"""
        self.assertEqual(max_integer([-1, -3, -5]), -1)
        """Testing single value"""
        self.assertEqual(max_integer([4]), 4)
        """Testing string"""
        self.assertEqual(max_integer("string", 't'))

    def test_invalid(self):
        """Testing mixed values"""
        self.assertRaises(TypeError, max_integer, [5, "string", 10])
        """Testing no lists"""
        self.assertRaises(TypeError, max_integer, 1)
        """Testing None"""
        self.assertRaises(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
