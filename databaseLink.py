import pymysql

db= pymysql.Connect(host="localhost",user="root",password="123",database="build")
cursor=db.cursor()
cursor.execute("select * from books")
data=cursor.fetchall()
print(data)
db.close()