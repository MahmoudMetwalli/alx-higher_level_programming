#!/usr/bin/python3
"""Status of connection"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    values = {'email': email}
    URL = sys.argv[1]
    DATA = urllib.parse.urlencode(values)
    DATA = DATA.encode('utf-8')
    req = urllib.request.Request(URL, DATA)
    with urllib.request.urlopen(req) as resp:
        body_response = resp.read()
        print(body_response.decode('utf-8'))
