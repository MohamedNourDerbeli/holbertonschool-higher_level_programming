#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

# Importing the max_integer function from the module to be tested
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_add_string(self):
        """Test the function returns the correct maximum integer in a list."""
        self.assertEqual(max_integer([1, 2]), 2)

    def test_empty_list(self):
        """Test the behavior when an empty list is passed."""
        self.assertIsNone(max_integer([]))

    def test_add_two_lists(self):
        """Test behavior when adding two lists, should raise ValueError."""
        self.assertRaises(TypeError, lambda: max_integer([1, 2], [1, 5]))

if __name__ == "__main__":
    unittest.main()
