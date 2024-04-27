#!/usr/bin/python3
"""Status of connection"""
import requests
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    req = requests.get(URL)
    html = req.headers
    print(html['X-Request-Id'])
