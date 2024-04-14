#!/usr/bin/python3
"""lists all states from the database with a name starting with N (upper N)"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    if (len(sys.argv[4].split()) == 1):
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                    '{}' ORDER BY states.id".format(sys.argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(f"{row}")
        cur.close()
        db.close()
