from questions import Student
import mysql.connector
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='mainexam')
manage = connect.cursor()
# CREATE DATABASE
# mycursor.execute("CREATE DATABASE mainexam")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)
# CREATE TABLE
# mycursor.execute("CREATE TABLE mainexam (first VARCHAR(20), last VARCHAR(20), user VARCHAR(40), pin INT(4), score INT(4))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor: 
#     print(table)
# Student()
# print("Login Successful")
# print("Welcome to your Exam Page!!!")
# Print("Enter 1 to register or Enter 2 to login")
# register = '1'
# login = '2'
# options = input("Choose an option to begin")
# if options == '1':
#     wy.reg()
# elif options == '2':
#     wy.login()
# myquery = "INSERT INTO studentinfo (first, last, user, pin, score ) VALUES(%s, %s, %s, %s,%s)"
# val = (self.first,self.last,self.user,self.pin)
# mycursor.execute(myquery, val)
# mycon.commit()
# # username = usernam
# # passwd = password
# print("Please login")
# first = input("Enter your username")
# second = input("Enter your pin")
# if user == username and passwd == password:
#     print("Please Answer the questions below")
#     print("Read Instructions Carefully, Goodluck!")
# else:
#     quit()

wy = Student()
wy.options()
# wy.reg()
# Student().login()