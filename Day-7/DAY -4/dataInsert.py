import sqlite3

conn = sqlite3.connect("db1.db")

conn.execute('''
INSERT INTO user(usnm, pass) VALUES ("ABCD", "12345678")
''')

conn.execute('''
INSERT INTO user(usnm, pass) VALUES ("EFGH", "87654321")
''')

conn.execute("UPDATE Number = 23423849 WHERE name = EFGH")
conn.commit()
conn.close()
