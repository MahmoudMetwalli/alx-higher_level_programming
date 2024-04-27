#!/usr/bin/python3
"""Status of connection"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        html = resp.headers
        print(html['X-Request-Id'])
