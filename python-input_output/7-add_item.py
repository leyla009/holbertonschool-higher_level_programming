#!/usr/bin/python3
"""
A script that adds all arguments to a Python list and saves them to a file.
"""
import sys


# Importing functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if file exists and load its content; otherwise, start with an empty list
try:
    items = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    items = []

# sys.argv[1:] captures all arguments passed after the script name
items.extend(sys.argv[1:])

# Save the updated list back to the same file
save_to_json_file(items, filename)
