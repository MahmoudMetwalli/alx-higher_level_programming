#!/usr/bin/python3
"""append after"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    if len(search_string) == 0 or len(new_string) == 0:
        return
    total = ""
    try:
        with open(filename, mode='r+', encoding='utf-8') as a_file:
            for line in a_file.readlines():
                flag_2 = 0
                for compare in range(0, len(line)):
                    flag = 0
                    if line[compare] == search_string[0]:
                        for i in range(0, len(search_string)):
                            if line[compare] == search_string[i]:
                                flag += 1
                            compare += 1
                    if flag == len(search_string):
                        flag_2 = 1
                total += line
                if flag_2:
                    total += new_string
    except Exception:
        return
    with open(filename, mode='w', encoding='utf-8') as b_file:
        b_file.write(total)
