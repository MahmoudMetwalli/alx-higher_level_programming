#!/usr/bin/python3
"""Status of connection"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    values = {'q': q}
    URL = 'http://0.0.0.0:5000/search_user'
    try:
        response = requests.post(URL, data=values)
        try:
            html = response.json()
            if len(html) == 0:
                print('No result')
            else:
                print("[{}] {}".format(html['id'], html['name']))
        except requests.exceptions.JSONDecodeError:
            print('Not a valid JSON')
    except Exception:
        pass
