#!/usr/bin/python3
"""Status of connection"""
import requests
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    values = {'email': email}
    URL = sys.argv[1]
    try:
        req = requests.post(URL, data=values)
        html = req.text
        print(html)
    except Exception:
        pass
