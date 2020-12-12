import sqlite3 as s

conn = s.connect('db.db')
curs = conn.cursor()

curs.execute('SELECT * FROM must')
rows = curs.fetchall()

print(rows)

        