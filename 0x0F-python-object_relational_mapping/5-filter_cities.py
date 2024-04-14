#!/usr/bin/python3
"""lists all states from the database with a name starting with N (upper N)"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    if (len(sys.argv[4].split()) == 1):
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities WHERE state_id IN\
                    (SELECT id FROM states WHERE name LIKE BINARY\
                    '{}')\
                    ORDER BY cities.id".format(sys.argv[4]))
        rows = cur.fetchall()
        for i in range(0, len(rows)):
            if (i == (len(rows) - 1)):
                print(f"{rows[i][0]}")
            else:
                print(f"{rows[i][0]}",end=", ")
        cur.close()
        db.close()
