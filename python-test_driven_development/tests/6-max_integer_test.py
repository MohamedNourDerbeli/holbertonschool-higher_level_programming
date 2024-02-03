#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

# Importing the max_integer function from the module to be tested
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_all(self):
        """Test case"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1]), 1)
        self.assertIsNone(max_integer([]),None)
        self.assertEqual(max_integer([-1, -25, -6]), -1)
        self.assertRaises(Exception, max_integer,["str",1])

if __name__ == "__main__":
    unittest.main()
