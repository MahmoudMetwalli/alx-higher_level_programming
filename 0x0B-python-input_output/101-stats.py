#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys
import signal


def handler(signum, frame):
    """handles ctrl c"""
    print(f"File size: {TOTAL_FILE_SIZE}")
    for key2, value2 in codes_dictionary.items():
        if value2 == 0:
            print("", end="")
        else:
            print(f"{key2}: {value2}")

signal.signal(signal.SIGINT, handler)

codes_list = ["200", "301", "400", "401", "403", "404", "405", "500"]
codes_dictionary = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
COUNT = 0
TOTAL_FILE_SIZE = 0
for line in sys.stdin:
    if (line.split())[7] in codes_list:
        codes_dictionary[(line.split())[7]] += 1
    TOTAL_FILE_SIZE += int((line.split())[8])
    COUNT += 1
    if COUNT == 10:
        print(f"File size: {TOTAL_FILE_SIZE}")
        for key, value in codes_dictionary.items():
            if value == 0:
                print("", end="")
            else:
                print(f"{key}: {value}")
        COUNT = 0
