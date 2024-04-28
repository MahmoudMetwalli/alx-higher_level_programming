#!/usr/bin/python3
"""Status of connection"""
import requests
import sys


if __name__ == "__main__":
    passwd = sys.argv[2]
    usr = sys.argv[1]
    try:
        req = requests.get('https://api.github.com/user',
                           auth=(usr, passwd), timeout=1)
        html = req.json()
        print(html['id'])
    except Exception as e:
        if req.status_code == 401:
            print('None')
        else:
            pass
