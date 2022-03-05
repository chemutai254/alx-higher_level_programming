#!/usr/bin/python3
"""script that takes in the name of a state as an argument 
and lists all cities of that state, using the database """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    i = db.cursor()
    i.execute("SELECT * FROM `cities` as `i` \
                INNER JOIN `states` as `s` \
                   ON `i`.`state_id` = `s`.`id` \
                ORDER BY `i`.`id`")
    print(", ".join([ct[2] for ct in i.fetchall() if ct[4] == sys.argv[4]]))
