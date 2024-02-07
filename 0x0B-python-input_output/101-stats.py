#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys

codes_list = ['200', '301', '400', '401', '403', '404', '405', '500']
codes_dictionary = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
COUNT = 0
TOTAL_FILE_SIZE = 0
try:
    for line in sys.stdin:
        try:
            if (line.split())[7] in codes_list:
                codes_dictionary[(line.split())[7]] += 1
        except IndexError:
            pass
        try:
            TOTAL_FILE_SIZE += int((line.split())[8])
        except (IndexError, ValueError):
            pass
        COUNT += 1
        if COUNT == 10:
            print(f"File size: {TOTAL_FILE_SIZE}")
            for key, value in codes_dictionary.items():
                if value:
                    print(f"{key}: {value}")
            COUNT = 0
    print(f"File size: {TOTAL_FILE_SIZE}")
    for key, value in codes_dictionary.items():
        if value:
            print(f"{key}: {value}")
except KeyboardInterrupt:
    print(f"File size: {TOTAL_FILE_SIZE}")
    for key, value in codes_dictionary.items():
        if value == 0:
            print("", end="")
        else:
            print(f"{key}: {value}")
    raise
