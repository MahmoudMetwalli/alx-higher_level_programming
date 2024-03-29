#!/usr/bin/python3
"""append after"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    if not isinstance(search_string, str) or not isinstance(new_string, str):
        return
    if len(new_string) == 0:
        new_string = "\n"
    flag_3 = 0
    if len(search_string) == 0:
        flag_3 = 1
    total = ""
    with open(filename, mode='r+', encoding='utf-8') as a_file:
        for line in a_file.readlines():
            flag_2 = 0
            for compare in range(0, len(line)):
                flag = 0
                if line[compare] == search_string[0]:
                    for i in range(0, len(search_string)):
                        try:
                            if line[compare] == search_string[i]:
                                flag += 1
                            compare += 1
                        except IndexError:
                            pass
                    if flag == len(search_string):
                        flag_2 = 1
            total += line
            if flag_3:
                total += new_string
            else:
                if flag_2:
                    total += new_string
    with open(filename, mode='w', encoding='utf-8') as b_file:
        b_file.write(total)
