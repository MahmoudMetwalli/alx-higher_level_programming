#!/usr/bin/python3
"""To print it sorted"""


class MyList(list):
    """Mylist as list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        try:
            print(sorted(self))
        except Exception:
            pass
