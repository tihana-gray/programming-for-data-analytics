import os
import sqlite3

os.chdir(os.path.dirname(os.path.abspath(__file__)))

con = sqlite3.connect("lecture.db")
cur = con.cursor()

sql = "CREATE TABLE student (name, course, gender)"
cur.execute(sql)
con.close()