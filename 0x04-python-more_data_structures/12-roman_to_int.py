#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    x = 0
    if not isinstance(roman_string, str) or not roman_string or roman_string is None:
        return int(x)
    for i in range(len(roman_string)):
        for j, k in romans.items():
            if roman_string[i] == j:
                if i + 1 < len(roman_string) and romans[j] < romans[roman_string[i + 1]]:
                    x = k - x
                else:
                    x += k
    return int(x)
