#!/usr/bin/python3
"""lists all cities from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities,\
                states WHERE cities.state_id = states.id ORDER BY\
                cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
