#!/usr/bin/python3
"""
List all the cities
of a state
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities WHERE state_id IN \
    (SELECT id FROM states WHERE name="{}")""".format(sys.argv[4]))
    state = cur.fetchall()
    print(", ".join([city[0] for city in state]))
