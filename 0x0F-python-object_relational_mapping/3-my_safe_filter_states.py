#!/usr/bin/python3
"""SQL injection to delete all records of a table"""
import sys
import MSQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    i = db.cursor()
    i.execute("SELECT * FROM `states`")
    [print(state) for state in i.fetchall() if state[1] == sys.argv[4]]
