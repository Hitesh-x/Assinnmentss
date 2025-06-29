import sqlite3
conn = sqlite3.connect("db1.db")

data = conn.execute("select * from user")
for x in data:
    print(x)

id = int(input("ID to delete:"))

conn.execute("DELETE FROM user where usid =?", (id,))
conn.commit()

data = conn.execute("Select * from user order by usnm")
for x in data:
    print(x)

conn.close()