# WRITE A FILE
# with open("C:\\Users\\23470\\Documents\\file handling\\test.txt", mode='w') as myfile:
#         myfile.write('lorem ipsum A comma-separated values file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas.')
#         myfile.write('\n peir lowter The use of the comma as a field separator is the source of the name for this file')


# READ A FILE
# with open("C:\\Users\\23470\\Documents\\file handling\\test.txt", mode='rt') as myfile:
#         # print(myfile.read())
#         # print(myfile.readline())
#         for i in range(5):
#             print(myfile.readline())


# APPEND IN A FILE
# with open("C:\\Users\\23470\\Documents\\file handling\\test.txt", mode='a') as myfile:
#     myfile.write("\n The CSV file format is not fully standardized. Separating fields with commas is the foundation, but commas in the data or embedded line breaks have to be handled specially. Some implementations disallow such content while others surround the field with quotation marks, which yet again creates the need for escaping if quotation marks are present in the data The term also denotes several closely-related delimiter-separated formats that use other field delimiters such as semicolons.[2] These include tab-separated values and space-separated values. A delimiter guaranteed not to be part of the data greatly simplifies parsing.Alternative delimiter-separated files are often given a extension despite the use of a non-comma field separator. This loose terminology can cause problems in data exchange. Many applications that accept CSV files have options to select the delimiter character and the quotation character. Semicolons are often used instead of commas in many European locales in order to use the comma as the decimal separator and, possibly, the period as a decimal grouping character.")
# ====================================================
# TO READ A FILE IMPORTING OS
# import os

# if os.path.exists('C:\\Users\\23470\\Documents\\file handling'):
#   with open("C:\\Users\\23470\\Documents\\file handling\\test.txt") as myfile:
#     print(myfile.read())
# else:
#   print("file does not exist")


# code to get system environment
import os
homedir = os.environ["PATH"]
print(homedir)
# =====================================================




# BANKING APP ASSIGNMENT

# class Banking:
#     def __init__(self):
#         # def menu():
#         n = int(input('Enter 1 to Register>>>>>>:'))
#         reg = {}
#         for x in range(n):
#             self.username = input('Enter your username to Register>>>>>: ')
#             self.password = input('Enter your password to Register>>>>>: ')
#             reg[self.username] = self.password
#             print("Registration Successful")
#             print(reg)
#             print("Login to your account")
#             self.user = input("Enter your username>>")
#             self.passcode = input("Enter your passcode>>")
#             if self.user == self.username and self.passcode == self.password:
#                 print("Login Successful")
#                 # menu()
#             else:
#                 print("Invalid Login")


# Banking()











# def login(self):
#         self.username = input("enter your username to login")
#         self.password = input("Enter your password to login ")
# # if reg[username] == username:
#     print("Username is Valid")
# elif password == password:
#     print("Password is Valid")
# else:
#     print("Invalid Login Details")

# login(self)




# username = input("Enter your Username")
#         password = input("Enter your password")
#         email = input("Enter your email address")
#         print("Registration Successful")
#         username = input("Enter your username")
#         password = input("Enter your password")
#         if username == password:
#             print("Login Successful")
#         else:
#             print("Incorrect username or password")
#     login()




# class Animal:
#     def  __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display_age(self):
#         print("{} Age: {}".format(self.name,self.age))

# def create(storage):
#     name = input("enter name: ")
#     age = input("enter age: ")
#     storage[name] = Animal(name,age)

# storage = {}
# create(storage)
# storage['Ben'].display_age()




# # in Python with input from the user
# class Student:
#     'A student class'
#     stuCount = 0
  
#     # initialization or constructor method of
#     def __init__(self):  
          
#         # class Student
#         self.name = input('enter student name:')
#         self.rollno = input('enter student rollno:')
#         Student.stuCount += 1
  
#     # displayStudent method of class Student
#     def displayStudent(self):  
#         print("Name:", self.name, "Rollno:", self.rollno)
  
  
# stu1 = Student()
# stu2 = Student()
# stu3 = Student()
# stu1.displayStudent()
# stu2.displayStudent()
# stu3.displayStudent()
# print('total no. of students:', Student.stuCount)


class StackOverflowUser():
    def __init__(self, name, userid, rep):
        self.name = name
        self.userid = userid
        self.rep = rep

name = input("Enter name: ")
userid = int(input("Enter user id: "))
rep = int(input("Enter rep: "))
 
 
dave = StackOverflowUser(name, userid, rep)


    # def login():
    #     data = { }
    # while True:
    #     username = input("Username: ")
    #     password = input("Password: ")
    #     data[username] = password
    #     print("Login Successful")

    # login()
    # Banking()
# def login():
#     data = {}
#     while True:
#         username = input("Username: ")
#         password = input("Password: ")
#         data[username] = password
#         print(data)

# login()



# class Employee:  
#     def __init__(self, name, id):  
#         self.id = id  
#         self.name = name  
  
#     def display(self):  
#         print("ID: %d \nName: %s" % (self.id, self.name))  
  
  
# emp1 = input("Enter your first name") 
# emp2 = Employee("David", 102)  
  
# # accessing display() method to print employee 1 information  
  
# emp1.display()  
  
# # accessing display() method to print employee 2 information  
# emp2.display()  


# class car:  
#     def __init__(self):  
#         self.modelname = modelname  
#         self.year = year 
#     def display(self):  
#         print(self.modelname,self.year)  
  
# c1 = car("Toyota", 2016)
# c1.display()  





# class Person:

#     def __init__(self):
#         self.pets = []

#     def add_pet(self, pet):
#         self.pets.append(pet)

# jane = Person()
# bob = Person()

# jane.add_pet("cat")
# print(jane.pets)
# print(bob.pets)





    #     self.username = input("Enter username: ")
    #     self.password = input("Enter password: ")
    #     self.email = input('Enter your email address')

    # def login()



        # def bank(self):   
        #     print(f'The Banking{self.username}')




# CALCULATIONS USING FUNCTION
# 
# print("""
#     1.Additions
#     2.Subtractions
#     3.Multiplications
#     4.Factorial!
#     5.Permutation
# """)
# options = input('Choose from the options above to perform an operation>>>:')
# # if options == '1'
# def operation():
#     if options == '1':
#         num_a = int(input("Enter the first number>>>:"))
#         num_b = int(input('Enter the second number>>>:'))
#         p = num_a + num_b
#         print('Your Addition result is =' ,p)
#     elif options == '2':
#         num_a = int(input("Enter the first number>>>:"))
#         num_b = int(input('Enter the second number>>>:'))
#         q = num_a - num_b
#         print('Your Subtraction result is =', q)
#     elif options == '3':
#         num_a = int(input("Enter the first number>>>:"))
#         num_b = int(input('Enter the second number>>>:'))
#         r = num_a * num_b
#         print('Your Multiplication result is =', r)
#     elif options == '4':
#         num_a = int(input("Enter your number to Factorize>>>:"))
#         z = 1
#         for i in range(1, num_a+1):
#             z *= i
#         print('Your Factorial result is =', z)
#     elif option == '5':
#         num1 = int(input('Enter first number for permutation'))
#         num2 = int(input('Enter second number for permutation'))
#         # rez = 1
#         # for i in range(1, num1+1):
#         #     perm = rez *= i * (num1-num2)
#         # print(f"Your Permutation is {perm}")
#     else:
#         print('Invalid Input')

# operation()



# P(n,r)=n! (n-r)!
# n! = n x (n - 1)!


# # Now giving two arguments to the function  
# print( "Passing two arguments" )  
# function(10,30) 
# m = int(input('Enter value for r>>>>>:'))
# def function(pi, r = m):
#     a = (pi * r ** 2)
#     print("Area is: ", a)


# function(3.142)

# SI = (P X R X T)
# p = int(input('Enter the Principal>>>>:'))
# r = float(input('Enter the rate>>>>:'))
# t = int(input('Enter the year>>>:'))
# def function(p ,r , t, y = 100):
#     si = (p * r * t / y)
#     print('Your Interest is',si)

# function(p, r, t)













# # EVEN AND ODD AND PRIME
# even = []
# odd = []
# prime = []
# n = int(input('Enter a start value:'))
# k = int(input('Enter an end value'))
# for b in range(n,k):
#      if b % 2==0:
#         even.append(b)
#      elif b % 2==1:
#           odd.append(b)
# for y in range(n,k):
#      if y>1:
#             for x in range(2,y):
#                 if y % x==0:
#                     break
#             else:
#                 prime.append(y)
# print('even:')
# print('odd:')
# print('prime:')


# THURSDAY AUGUST 25.
# CLASSWORK
# ASSIGNMENT


# TEMPERATURE CONVERSION WITH USERNAME AND PASSWORD

# username = input('Enter your username>>>: ')
# password = int(input('Enter your password>>>:'))
# t = ['pole', 'pen', 'part']
# pas = [2009, 2008, 2007]
# for i in range(1):
#     if username == t and password == pas:
#         print('Proceed')
#     else:
#         print('Incorrect Username')
#     temp = input('Enter the unit you want to convert from :')
# if temp.upper() == 'C':
#     temps = input('Enter the unit you want to convert to :')
#     if temps.upper() == 'F' :
#         c = int(input('Enter the value for temp(c):'))
#         result = (9/5 * c) + 32
#         print(result, 'F')
#     else:
#         print('Error')
# elif temp.upper() == 'F':
#     temps = input('Enter the unit you want to convert to :')
#     if temps.upper() == 'C':
#         f = int(input('Enter the value for temp(f):'))
#         result = (f-32) * 5/9
#         print(result, 'C')
#     else:
#         print('Error')
# elif temp.upper() == 'K':
#     t = input('Enter the unit you want to convert to: ')
#     if t.upper() == 'C':
#         k = int(input('Enter the value for temp(k): '))
#         result = (k - 273.15)
#         print(result, 'C')
#     elif t.upper() == 'F':
#         k = int(input('Enter the value for temp(k):'))
#         result = (k - 273.15) * 9/5 + 32
#         print(result, 'F')
# else:
#     print('Unknown Input')
#     quit()



