#!/usr/bin/python3
"""loading json"""
import json


def load_from_json_file(filename):
    """loading json"""
    with open(filename, encoding='utf-8') as a_file:
        return json.loads(a_file.read())
