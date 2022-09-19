from questions import Student
import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Exam')
mycursor = mycon.cursor()
Student()
print("Login Successful")
print("Welcome to your Exam Page!!!")

# Student()

myquery = "INSERT INTO studentinfo (first, last, user, passwd ) VALUES(%s, %s, %s, %s,)"
val = (first,last,user,passwd)
mycursor.execute(myquery, val)
mycon.commit()
username = usernam
passwd = password
print("Please login")
first = input("Enter your login")
second = input("Enter your password")
if user == username and passwd == password:
    print("Please Answer the questions below")
    print("Read Instructions Carefully, Goodluck!")
else:
    quit()