#!/usr/bin/python3
"""Function: append_write(filename="", text="")"""


def append_write(filename="", text=""):
    """The file is opened in append mode ('a')"""
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
