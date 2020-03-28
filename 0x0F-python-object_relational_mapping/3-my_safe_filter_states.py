#!/usr/bin/python3
"""
 script that takes in an argument and displays all values in the states table
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states \
    WHERE name LIKE BINARY %(states_name)s \
    ORDER BY states.id ASC;", {'states_name': argv[4]})

    states = cur.fetchall()

    for states in states:
        print(states)

    cur.close()
    db.close()
