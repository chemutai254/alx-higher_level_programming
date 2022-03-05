#!/usr/bin/python3
"""Script that lists all cities from the database"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    i = db.cursor()
    i.execute("SELECT `i`.`id`, `i`.`name`, `s`.`name` \
                 FROM `cities` as `i` \
                INNER JOIN `states` as `s` \
                   ON `i`.`state_id` = `s`.`id` \
                ORDER BY `i`.`id`")
    [print(city) for city in i.fetchall()]
