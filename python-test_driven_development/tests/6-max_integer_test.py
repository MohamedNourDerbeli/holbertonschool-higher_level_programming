#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer
"""
Creating a test class that inherits from unittest.TestCase.
This class contains test cases for the max_integer function.
"""


class TestMaxInteger(unittest.TestCase):
    """
    Test case to check if the function returns the correct
    maximum integer in a list.
    """

    def test_add_string(self):
        self.assertEqual(max_integer([1, 2]), 2)

    """
    Test case to check the behavior when an empty list is passed.
    """

    def test_emty_list(self):
        self.assertIsNone(max_integer(), None)


if __name__ == "__main__":
    unittest.main()
