import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',passwd='ved08',database='colleges')           #connectivity established
cur=mycon.cursor() 

college_id = int(input("college id"))
name = input("name")
course = input("course")

website = input("website")
scholarship = input("scholarship")
city = input("city")
exam = input("exam")
percentage = input("percentage")
fee = input("fee")
rank = input("rank")

query = "INSERT INTO COLLEGES values({},{},{},{},{},{},{},{},{},{},{});".format(college_id, name, course, website, scholarship, city, exam, percentage, fee, rank)

cur.execute(query)
