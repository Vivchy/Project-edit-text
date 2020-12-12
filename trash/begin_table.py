import sqlite3 as s

conn = s.connect('db.db')
curs = conn.cursor()
# curs.execute('''
#     CREATE TABLE must
#     (name VARCHAR(20) PRIMARY KEY,
#     age INT,
#     damages FLOAT) ''')

ins = 'INSERT INTO must (name, age, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('igor', 12, 120))
curs.execute(ins, ('victor', 112, 13420))
curs.execute('SELECT * FROM must')
rows = curs.fetchall()
print(rows)



