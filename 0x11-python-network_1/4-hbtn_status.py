#!/usr/bin/python3
"""Status of connection"""
import requests


if __name__ == "__main__":
    URL = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(URL)
    html = req.text
    print("Body response:\n\t- type: {}\
\n\t- content: {}\
".format(type(html), html))
