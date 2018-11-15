#!/usr/bin/python3.3

import csv, sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

with open('test.csv','r') as f:
    reader = csv.reader(f)
    reader.next()
    for column in reader:
        cur.execute('INSERT INTO jaws VALUES (?,?,?)',tuple(i for i in column))
        con.commit()

cur.execute("SELECT * FROM jaws")
for r in cur.fetchall():
    print r


