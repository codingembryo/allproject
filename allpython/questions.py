import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Exam')
mycursor = mycon.cursor()

class Student():
    def __init__(self):
        self.you = "you"
        
    def reg(self):
        self.first = input("Enter your first name")
        self.last= input("Enter your last name")
        self.user = input("Enter your username")
        self.passwd = input("Enter your password")
        print("Registration Successful")
    
    
    def login(self):
        self.username = input("Enter your username")
        self.password = input("Enter your password")
        # if user == username and password == passwd:
        print("Login Successful")
wy = Student()
wy.reg()
wy.login()


    




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



