import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

mycursor = mydb.cursor()
sql = "insert into student (name, age) values (%s, %s)"
values = ("Mary", 25)
mycursor.execute(sql, values)


mydb.commit()

mycursor.close()
mydb.close()