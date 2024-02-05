#!/usr/bin/python3
"""To print it sorted"""


class MyList(list):
    """Mylist as list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        for i in list(self):
            if not isinstance(i, int):
                raise TypeError("unorderable types: NoneType() < int()")
        print(sorted(self))
