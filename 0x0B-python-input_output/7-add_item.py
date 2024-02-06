#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


listed = []
for i in range(1, len(sys.argv)):
    listed.append(sys.argv[i])
try:
    if isinstance(load_from_json_file("add_item.json"), list):
        for j in load_from_json_file("add_item.json"):
            listed.append(j)
except Exception:
    pass
save_to_json_file(listed, "add_item.json")
