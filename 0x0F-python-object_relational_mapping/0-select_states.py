#!/usr/bin/python3
"""Lists all states fro the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ = "__main__":

    conn = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8")
    # begin cursor
    curs = conn.cursor()

    # query
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = curs.fetchall()

    # print query
    for row in query_rows:
        print(row)

    # end cursor
    curs.close()
    conn.close()
