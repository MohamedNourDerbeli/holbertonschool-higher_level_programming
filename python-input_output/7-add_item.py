#!/usr/bin/python3
"""Add a new item to the list."""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
from sys import argv
from os.path import isfile

filename = "add_item.json"
if isfile(filename):
    appa = load_from_json_file(filename)
else:
    appa = []
save_to_json_file(list(appa + argv[1:]), filename)
