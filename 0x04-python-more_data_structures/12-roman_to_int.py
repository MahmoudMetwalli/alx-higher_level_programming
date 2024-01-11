#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    x = 0
    if not isinstance(roman_string, str) or not roman_string:
        return int(x)
    for i in roman_string:
        for j, k in romans.items():
            if i == j:
                if x < k:
                    x = k - x
                else:
                    x += k
    return int(x)
