#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest

# Importing the max_integer function from the module to be tested
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_all(self):
        """Test case"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([11, 1]), 11)
        self.assertEqual(max_integer([91, 41, 21]), 91)
        self.assertEqual(max_integer([11, 11, 11]), 11)
        self.assertEqual(max_integer([-1, -25, -6]), -1)
        self.assertEqual(max_integer([-1, -25, 11, 11]), 11)
        self.assertEqual(max_integer([-1, -25, 0.1, 11.4]), 11.4)
        self.assertEqual(max_integer(list(range(100000))), 99999)

    def test_emty_list(self):
        """Emty list"""
        self.assertIsNone(max_integer())

    def test_error(self):
        """Error case"""
        self.assertRaises(TypeError, max_integer, ["r", 1])
        self.assertRaises(TypeError, max_integer, [23, [11, 23]])
