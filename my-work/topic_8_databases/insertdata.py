import os
import sqlite3

os.chdir(os.path.dirname(os.path.abspath(__file__)))

con = sqlite3.connect("lecture.db")
cur = con.cursor()

#sql = "select * from student"
#result = cur.execute(sql)
#print (f" first row: {result.fetchone()}")

sql = "insert into student values ('mary', 'SD', 'Female')"
cur.execute(sql)
con.commit()

#sql = "select * from student"
#result = cur.execute(sql)
#print (f" first row: {result.fetchone()}")


con.close()