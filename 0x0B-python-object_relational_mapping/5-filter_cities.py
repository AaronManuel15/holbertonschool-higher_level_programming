#!/usr/bin/python3
""" Project 0x0B. Python - Object-relational mapping
    Task 5
"""
import MySQLdb


def cities_print():
    """prints states from given db"""
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
                cities.state_id = states.id WHERE states.name \
                LIKE %s ORDER BY cities.id", (argv[4],))
    print(', '.join(row[0] for row in cur))

    cur.close()
    db.close()


if __name__ == "__main__":
    cities_print()
