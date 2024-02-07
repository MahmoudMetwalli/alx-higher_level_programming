#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def print_metrs(TOTAL_FILE_SIZE, codes_dictionary):
    print("File size: {}".format(TOTAL_FILE_SIZE))
    for key in sorted(codes_dictionary):
        if codes_dictionary[key]:
            print("{}: {}".format(key, codes_dictionary[key]))


if __name__ == "__main__":
    codes_list = ["200", "301", "400", "401", "403", "404", "405", "500"]
    codes_dictionary = {"200": 0, "301": 0, "400": 0,
                        "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    COUNT = 0
    TOTAL_FILE_SIZE = 0
    try:
        for line in sys.stdin:
            if (line.split())[7] in codes_list:
                codes_dictionary[(line.split())[7]] += 1
            TOTAL_FILE_SIZE += int((line.split())[8])
            COUNT += 1
            if COUNT == 10:
                print_metrs(TOTAL_FILE_SIZE, codes_dictionary)
                COUNT = 0
    except KeyboardInterrupt:
        print_metrs(TOTAL_FILE_SIZE, codes_dictionary)
        raise
