import mysql.connector as mysql
conn = mysql.connect(user="root", password="scott", host='127.0.0.1')
c = conn.cursor()
c.execute("use FYCS")
c.execute("DROP TABLE STUDENT")
c.execute("SHOW TABLES FROM FYCS")
print(c.fetchall())
conn.close()
