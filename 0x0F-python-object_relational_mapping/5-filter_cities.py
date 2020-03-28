#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.name \
    FROM cities\
    INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name = %(c_name)s \
    ORDER BY cities.id ASC;", {"c_name": argv[4]})

    states = cur.fetchall()

    cities = []

    for item in states:
        cities.append(item[0])

    new = ", ".join(cities)
    print(new)

    cur.close()
    db.close()
