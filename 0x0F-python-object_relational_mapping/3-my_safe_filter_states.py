#!/usr/bin/python3
"""
Displays all values in the states table of
 hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE BINARY "%{:s}%" \
    ORDER BY states.id ASC""".format(sys.argv[4].split(' ')[0].split(";")[0]))
    rows = c.fetchall()
    for state in rows:
        print(state)
