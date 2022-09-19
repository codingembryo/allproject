### Python Regular Expression
# import re
# print(dir(re))
# re function
# findall() : returns list containing all matches
# search() : returns object of a match if there is a match anywhere in the string
# split() : returns a list where the string has been split at each match
# sub() : replace one or many matches  with a string

# re matacharacters
# [] : refers to set of characters to match eg "[a-m]"
# \ : can be use to escape special charactter eg "\d"
# . : any character except newline character eg 'he.o'
# ^ : starts with eg "^the"
# $ : ends with eg "world$"
# * : zero or more occurrences eg "aix*"
# + : one or more occurrences eg "aix+"
# {} : exactly specified number of occurrence eg "al{2}"
# | : either or eg "this|that"
# () : capture and group 

# re special Sequences
# \A : returns a match if the specified characters are at the begining of the string eg "\AThe"
# \b : returns a match if the specified characters are at the begining or at the end of the string eg r"\bthe" or r"the\b"
# \B : returns a match if the specified characters are present but not at the begining or at the end of the string eg r"\Bthe" or r"the\B"
# \d : returns a match where the string contains digits (number from 0-9) eg "\d"
# \D : returns a match where the string does not contains digits eg "\D"
# \s : returns a match where the string contains a white space character eg "\s"
# \S : returns a match where the string does not contains a white space character eg "\S"
# \w : returns a match where the string contains characters from letter A-Z and digits from 0-9 and underscore eg "\w"
# \W : returns a match where the string does not contains any word characters 
# \Z : returns a match if the specified characters are at the end of the string

# re sets
# [arn] : returns a match where one of the specified characters (a or r or n ) are present
# [a-n] : returns a match for any lower case character alphabetically between a and n
# [^arn] : returns a match for any character except a, r and n
# [0123] : returns a match where any of the specified digits (0, 1, 2, 3) are present
# [0-9] : returns a match for any digits between 0 and 9
# [0-5][0-9] : returns a match for any two digits between 00 and 59
# [a-zA-Z] : returns a match for any character alphabetically between a and z lower case or upper case
# [+] : returns a match for any character in the string



# text = """the value of a thing will determing the capacity you put to it. the value of 2019 is what you get in 2020
#         and now you get the value of 2020 in 2021"""
# mm = input("enter your email>>>")

# val = re.findall(r"[01234]", mm)
# if val:
#     print("We have a match")
# else:
#     print("No match detected")

# text = """the value of a thing will determing the capacity you put to it. 
#         the value of 2019 is what you get in 2020
#         and now you get the value of 2020 in 2021"""
# x = re.findall(r'the', text)
# print(x)

# x = re.search(r'you', text)
# print(x)
# print(x.span())
# print(x.group())
# print(x.string)
# z = re.split(r'\s', text)
# print(z)
# z = re.split(r'\s', text,4)
# print(z)
# tx = re.sub(r'\d', '[]', text,4)
# print(tx)
# tx = re.sub(r'capacity', 'ability', text)
# print(tx)

# mm = input("enter text>> ")
# my =re.sub(r'\d', '[]', mm, 5)
# print(my)









### file handling
# open('filename', mode='r', 'a', 'w', 'x', encoding='t', 'b')
# 'r' read only and it is the default for open function. raise error if file do not exist 
# 'a' append new content to an existing file. create new file with the specific file.
# 'w'  open file for writing . create new file with specific name if not exist.
# 'x'  to create new file. raise error if file already exist





# with open("C:\\Users\\D\\Desktop\\paul\\pa.txt", mode='rt') as myFile:
    # for i in myFile:
    #     print(myFile.readline())

#   print(myFile.read(10))
# with open("C:\\USER\\Documents\\python code.txt", mode='rt') as myFile:
#   print(myFile.read())

# myFile = open("C:\\Users\\D\\Desktop\\paul\\pa.txt", 'rt') 
# myFile = open("C:\\Users\\ASUS\\Documents\\vuework.txt", mode='r')
# print(myFile.read())
# print(myFile.read(20))
# print(myFile.readline(20))

# for i in range(20):
#   print(myFile.readline())

# for i in myFile:
#   print(i)

# with  open("C:\\Users\\D\\Desktop\\paul\\commm.txt", 'a') as myFile:
#     myFile.write("\n this is new content to append to the old file")

# myFile = open("C:\\USER\\Documents\\PYTHON\\code.txt", 'rt') 
# print(myFile.read())
# myFile.close()



# myFile = open("code.txt", 'w') 
# myFile.write("\n this is cnew content to append to the old file")

# with open("code2.txt", 'w') as newFile:
#   newFile.write("here i am writing to new file")


# open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'x') 
# myFile = open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'a') 
# myFile.write("\n lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum")
# myFile = open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'r') 
# print(myFile.read())



# with open("C:\\USER\\Documents\\python code.txt", mode='rt') as myFile:
#   print(myFile.read())


# import os
# print(help(os))
# os.remove('newfile.txt') #raise error if not exist
# if os.path.exists('mypython.py'):
#   os.rmdir('mm')
#   print("file deleted successfully")
# else:
#   print('file not available')


# if os.path.exists('mypython.py'):
#   with open("mypython.py") as myFile:
#     print(myFile.read())
# else:
#   print("file does not exist")

# if os.path.exists("code.txt"):
#   os.remove("code.txt")
#   print("file deleted successfully")
# else:
#   print("file not available")



# os.rmdir("new folder")
# os.mkdir("new folder")
# os.mkdir("another folder")
# os.mkdir("Documents")




# with open("bankOOP.py", 'rt') as myFile:
#   print(myFile.read())



# with open("Documents", mode='rt') as inFile:
#   for files in inFile:
#     os.remove(files)

# deleting file and folder in a system
# for root, dirs, files in os.walk(" folder name"):
#   for file in files:
#       pass
#     # os.remove("new folder\\"+file)
# # os.rmdir("new folder")

# print(root)
# deleting file in folder
# for root, dirs, files in os.walk("another folder"):
#   for fil in files:
#     os.remove("another folder\\"+fil)
# os.rmdir("another folder")

# searching for  path of a file
# print(os.path.dirname(os.path.abspath("text.txt")))




# with open("Documents", mode='rt') as inFile:
#   for files in inFile:
#     os.remove(files)


# code to get username of any system(pc)
# import os.path
# homedir = os.path.expanduser("~")
# print(homedir)
# code to get system environment
# import os
# homedir = os.environ["PATH"]
# print(homedir)

# code to get the path of a file on your device
# print(os.path.dirname(os.path.abspath("mypython.py")))




###Python Error Handling
# Two types of error in programming:
# compile time error and run time error
# try and except, finally

# a = int(input("number1>>"))
# b = int(input("number1>>"))
    
# try:   
#     print(a/c)
# except NameError:
#     print("error")

# except ZeroDivisionError:
#     print(f"it can not divide any number with zero")
  

# except (TypeError, ZeroDivisionError):
#    # handle multiple exceptions
#    # TypeError and ZeroDivisionError
#    pass

# except:
#    # handle all other exceptions
#    pass


# def simpleCal():
#     	for i in range(6):
#             a = int(input("enter quotient value"))
#             b = int(input("enter divisor value"))
#             try:
#                 print(a/b)
#             except NameError:
#                 print("error")
#             except ZeroDivisionError:
#                 print(f"it can not divide any number with zero")
    
# simpleCal()

# def cal():
#     for i in range(2):
#         a = int(input("enter quotient value"))
#         b = int(input("enter divisor value"))
#         try:
#             print(a/b)
#         except:
#             print("divisor can not be zero")
# cal()

# def cal():
#     for i in range(5):
#         a = int(input("enter quotient value"))
#         b = int(input("enter divisor value"))
#         try:
#             print(a/b)
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except TypeError:
#             pass
#         except:
#             pass
#         else: # execute if no error was raised
#             print("no error was raised")
#         finally: # execute either there is error or not
#             print("the execution was successful")
# cal()

# a = int(input("enter quotient value"))
# b = input("enter divisor value")
# if type(b) is not int:
#     raise TypeError("divisor must be an integer type")
# else:
#     print(a/b)


# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:       
#        raise ValueError("That is not a positive number!")
#     else:
#         print(a)
# except ValueError as ve:
#     print(ve)
# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
#     print(num)
# except:
#     print("Not an even number!")
    
# else:
#     print(num/2)
# import cv2
# print(dir(cv2))

# program to print the reciprocal of even numbers

# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)

# try:
#    f = open("metadata.txt","rt") 
#    print(f.read())
#    # perform file operations
# except:
#     print("file not found")
# finally:
#    print("this is finally")
#    f.close()

# import module sys to get the type of exception
# import sys
# print(help(sys.exc_info))

# randomList = ['a', 0, 2]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occurred.")
#         print("Next entry.")
#         print()
# print("The reciprocal of", entry, "is", r)







# Python Database (Mysql)
# To download mysql connector user: pip install mysql-connector
# import mysql.connector


# mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='')
# mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE cbtTe")
# mycursor.execute("SHOW DATABASES")
#
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE customers (ctm_id INT(4), Ful_Name VARCHAR(20), Address VARCHAR(50), Phone VARCHAR(11), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor: 
#     print(table)

# mycursor.execute("ALTER TABLE customers CHANGE ctm_id ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE customers ADD UNIQUE(Phone);")

# myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = ('mike Adesola', 'USA', '07067307888', '76748899789')
# mycursor.execute(myquery, val)
# mycon.commit()

# fulname = input('enter your name >') 
# address = input('enter your address')
# phone = input('enter your phone number')
# password = input('enter your Password')
# myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = (fulname, address, phone, password)
# mycursor.execute(myquery, val)
# # mycursor.executemany((myquery, val),())
# mycon.commit()
# print(mycursor.rowcount, "records inserted successfully")

# query = "SELECT * FROM customers"
# mycursor.execute(query)
# output = mycursor.fetchall()
# print(output)
# for inf in output:
#   print(inf)

# mmm = "SELECT * FROM customers WHERE Ful_Name = %s"
# val = ("paul",)
# mycursor.execute(mmm,val)
# nm = mycursor.fetchall()
# print(nm)

# query = "SELECT * FROM customers WHERE Ful_Name LIKE '%th%'"
# query = "SELECT Ful_Name, Phone FROM customers"
# query = "SELECT * FROM customers ORDER BY ful_Name DESC"
# val = ('09013140700', val)

# phone = input("Enter your phone number ")
# pin = input("Enter your pin ")
# query = "SELECT Ful_Name, Address FROM customers WHERE Phone=%s AND Password=%s "
# val = (phone, pin)
# mycursor.execute(query, val)
# myreg = mycursor.fetchall()
# # myreg = mycursor.fetchone()
# print(myreg)
# for info in myreg:
#     print(info)
# mycon.commit()
# print(mycursor.rowcount, 'selected successfuly')
# mycon.close()

# sql = "UPDATE customers SET  Password='2123' WHERE Phone=%s"
# val =('08081306253',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record updated successfuly')

# sql = "DELETE FROM customers WHERE Phone=%s"
# val =('08081306253',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record deleted successfuly')

# sql = "DROP DATABASE cbtte"
# mycursor.execute(sql)
