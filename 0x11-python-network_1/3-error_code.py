#!/usr/bin/python3
"""Status of connection"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    req = urllib.request.Request(URL)
    try:
        with urllib.request.urlopen(req) as resp:
            body_response = resp.read()
            print(body_response.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
