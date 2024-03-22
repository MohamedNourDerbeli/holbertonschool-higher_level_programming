#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    cur.execute(
        f"SELECT * FROM states \
                 WHERE name LIKE BINARY '{argv[4]}' \
                 ORDER BY states.id ASC"
    )
    [print(state) for state in cur.fetchall()]
