#!/usr/bin/python3
"""Status of connection"""
import sys
import requests
import requests.exceptions


if __name__ == "__main__":
    URL = sys.argv[1]
    try:
        req = requests.get(URL)
        try:
            req.raise_for_status()
            print(req.text)
        except requests.exceptions.HTTPError:
            print("Error code: {}".format(req.status_code))
    except Exception:
        pass
