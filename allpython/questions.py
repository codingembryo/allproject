import mysql.connector
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='mainexam')
manage = connect.cursor()

class Student():
    def __init__(self):
        self.you = "you"


    def options(self):
        self.register = 1
        self.login = 2
        options = int(input("Choose 1 to Register and 2 to Login>>>>>>:"))
        if options == 1:
            print("Welcome,Please Register")
            wy.reg()
            wy.login()
        elif options == 2:
            print('Welcome,Login')
            wy.login()
            

    def reg(self):
        self.first = input("Enter your first name>>>>>:")
        self.last= input("Enter your last name>>>>>:")
        self.user = input("Enter your username>>>>>:")
        self.pin = input("Enter your pin>>>>>:")
        studentinfo = "INSERT INTO mainexam (first, last, user, pin, score ) VALUES(%s, %s, %s, %s,%s)"
        data = (self.first, self.last, self.user, self.pin, 0)
        manage.execute(studentinfo, data)
        connect.commit()
        print(manage.rowcount, 'record(s) inserted successfully')
        
             
    def login(self):
        self.username = input("Enter your username")
        self.pin = input("Enter your pin")
        studentinfo = 'SELECT * FROM mainexam WHERE user=%s AND Pin=%s'
        data = (self.username, self.pin)
        manage.execute(studentinfo, data)
        report = manage.fetchone()
        print(report)
        # if user == username and password == passwd:
        print("Login Successful")
        print("Welcome to your Exam Page,Goodluck!l")
        
        # def reg(self):
        #     self.first = input("Enter your first name>>>>>:")
        #     self.last= input("Enter your last name>>>>>:")
        #     self.user = input("Enter your username>>>>>:")
        #     self.pin = input("Enter your pin>>>>>:")
        #     studentinfo = "INSERT INTO mainexam (first, last, user, pin, score ) VALUES(%s, %s, %s, %s,%s)"
        #     data = (self.first, self.last, self.user, self.pin, 0)
        #     manage.execute(studentinfo, data)
        #     connect.commit()
            # print(manage.rowcount, 'record(s) inserted successfully')
    
        # def login(self):
        #     self.username = input("Enter your username")
        #     self.pin = input("Enter your pin")
        # studentinfo = 'SELECT * FROM mainexam WHERE user=%s AND Pin=%s'
        # data = (self.user, self.pin)
        # manage.execute(studentinfo, data)
        # report = manage.fetchone()
        # print(report)
        # # if user == username and password == passwd:
        # print("Login Successful")
        # print("Welcome to your Exam Page,Goodluck!l")
wy = Student()
# wy.options()
# if options == 1:
#     print("Welcome,Please Register")
#     wy.reg()
#     wy.login()
# elif options == 2:
#     Student().login()

# wy.reg()
# Student().login()


    




# student_ID = input("Enter 5 digits for your student ID")
# full_name = input("Enter your full name>>>:")
# level = input("Enter your level")
# department = input("Enter your department>>>:")
# user = input("Enter your username>>>:")
# passwd = input("Enter your password>>>:")
# myquery = "INSERT INTO studentinfo (student_ID, full_name, level, department, username, password) VALUES(%s, %s, %s, %s, %s, %s)"
# reg = (student_ID, full_name, level, department, username, password)
# mycursor.execute(myquery, reg)
# mycon.commit()
# print("Login Successful")
# print("Welcome to your Exam Page!!!")

# reg = Student()
# print("Registration Successful")
# print("Please Login")
# username = input("Enter your username to login")
# password = input("Enter your password")
# if user == username and passwd == password:
#     print("Login Successful")
#     print("Welcome to your Exam Page,Goodluck!")
# else:
#     print("Login Error")



