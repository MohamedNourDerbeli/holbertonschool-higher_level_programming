#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd= argv[2], database= argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
