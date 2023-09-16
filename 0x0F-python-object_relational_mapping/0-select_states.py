#!/usr/bin/python3
"""get all states"""

import MySQLdb
import sys

if __name__ == "__main__":
    vr = sys.argv
    dd = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=vr[1],
            passwd=vr[2],
            db=vr[3])

cr = dd.cursor()

y = "SELECT * FROM states ORDER BY id ASC"
cr.execute(y)

ty = cr.fetchall()

for i in ty:
    print(i)

dd.close()
