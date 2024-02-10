#!/usr/bin/python3
"""Function: read_file(filename="")"""


def read_file(filename=""):
    """The file is opened in read mode ('r')"""
    with open(filename, "r") as f:
        content = f.readlines()
        for i in content:
            print(i, end="")
