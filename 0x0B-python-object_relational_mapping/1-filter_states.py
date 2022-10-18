#!/usr/bin/python3
""" Project 0x0B. Python - Object-relational mapping
    Task 1
"""
import MySQLdb


def state_print_N():
    """prints states from given db"""
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        if row[1][0] == "N":
            print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    state_print_N()
