import mysql.connector as mysql
conn = mysql.connect(user="root", password="scott", host='localhost')
c = conn.cursor()
c.execute("CREATE DATABASE FYCS")
print("database created successfully")
conn.close()
