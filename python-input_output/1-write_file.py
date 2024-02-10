#!/usr/bin/python3
"""Script: Write to File Example"""


def write_file(filename="", text=""):
    """Execute this script to create a file"""
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
