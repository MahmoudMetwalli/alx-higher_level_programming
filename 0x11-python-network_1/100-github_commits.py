#!/usr/bin/python3
"""Status of connection"""
import requests
import sys


if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    try:
        req = requests.get('https://api.github.com\
/repos/{}/{}/commits'.format(owner, repo), timeout=1)
        html = req.json()
        for i in range(0, 10):
            print(html[i]['sha'], end=": ")
            print(html[i]['commit']['author']['name'])
    except Exception as err:
        print('failed')
        print(err)
