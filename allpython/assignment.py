
# # ASSIGNMENT ONE
# CREATE A DATABASE AND LINK IT WITH CBT TEST
# LET IT CALCULATE IF THE OPTION IS CORRECT
# # AND AFTER THE EXAM PRINT THE TOTAL SCORE
# 5 QUESTIONS AND 10 MARKS FOR EACH QUESTIONS
# AND ANOTHER COLUMN IN DATABASE FOR GRADES
# 15-20 Fail
# 20 and above-pass


import re
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# email = input('Enter your email')
# password = input('Enter your password')
# # for i in email:
# #     valid = re.search r'\b('^\w+@\w+.\w+$', i)\b
# #     if valid !=0:
# #         print('Valid')
# def check(email):
#     if(re.fullmatch(regex, email)):
#         print("Valid Email")
 
#     else:
#         print("Invalid Email")

# check(email)

# TO CHECK IF VALID EMAIL
import re
# # regex 
# press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# email = input('Enter your email')
# password = input('Enter your password')
# # for i in email:
# #     valid = re.search r'\b('^\w+@\w+.\w+$', i)\b
# #     if valid !=0:
# #         print('Valid')
# def check(email):
#     if(re.fullmatch(press, email)):
#         print("Valid Email")
 
#     else:
#         print("Please Enter a valid Email")
#         email = input('Enter your email')
#         password = input('Enter your password')

# check(email)


















# 1.DATABASE MANUALLY

# # ASSIGNMENT TWO
# 2.
# CHARACTER SPLITTING AND PUT IN A LIST AND THAT LIST INSIDE A TUPLE

# # ASSIGNMENT THREE
# 3.
# arrange input of number into a triangle

# # ASSIGNMENT FOUR
# 4.
# theory to allow to enter answer.


# FIRST ASSIGNMENT DONE
# rows = int(input("Please Enter a Number  : "))
# level = 1
# for num in range(1, rows + 1):
#   print(num, end=" ")
#   num_end = level * (level + 1) / 2
#   if num == num_end or num == rows:
#     level += 1
#     print()

# SECOND ASSIGNMENT DONE
# y = list(input("Enter a word>>>>>"))
# x = (y,)
# print(x)































































# n = int(input("Enter the number of rows"))  
# # outer loop to handle number of rows  
# for i in range(1, n+1):  
#     # inner loop to handle number of columns  
#     # values is changing according to outer loop  
#         for j in range(0, i + 1):  
#             # printing stars  
#             print("", end="")       
  
#         # ending line after each row  
#         print()


















# ASSIGNMENT
# BANK APP
# REGISTER
# ASK FOR YOUR LOGIN DETAILS
# YOUR DETAILS WILL STORE INSIDE A NESTED DICTIONARY
# USERNAME AND PASSWORD
# 1. transfer
# 2.check account balance
# majorly bank transactions.


# choice = int(input("1-Login  2-Register"))
# if choice == 1:     
#     User.login()
# elif choice ==2:
#     User.register()



# a = []
# p =  input("Enter your username ")
# w = int(input('Enter Pin'))

# def reg()
#     name:
#     email:
#     Pin:


#     alluser = {name{name==,pin==,password==}}

# def trans():
    
    # QUESTION : Use the last number in a list to multiply other numbers and print the result in a list.
# first_result = []
# result = []
# for level in range(9):
#     enter = int(input('>>>'))
#     first_result.append(enter)
# print(first_result)
# for level_two in first_result:
#     second_result = first_result[-1] * level_two
#     result.append(second_result)
# print(result)







# QUESTION : Use the last number in a list to multiply other numbers and print the result in a list.
# first_result = []
# result = []
# for level in range(9):
#     enter = int(input('>>>'))
#     first_result.append(enter)
# print(first_result)
# for level_two in first_result:
#     second_result = first_result[-1] * level_two
#     result.append(second_result)
# print(result)



# first_num = int(input('Enter a number>>>>>:'))
# second_num = int(input('Enter another number>>>>>>:'))
# print('1.Addition')
# print('2.Subtraction')
# print('3.Multiplication')
# print('4. Division')
# print('5.Exponential')
# option = input("Please choose an operation from the above>>>>>:")
# if option == '1':
#     total = first_num + second_num
#     print(total)
# elif option == '2':
#     result = first_num - second_num
#     print(result)
# elif option == '3':
#     result = first_num * second_num
#     print(result)
# elif option == '4':
#     result = first_num / second_num
#     print(result)
# elif option == '5':
#     result = first_num ** second_num
#     print(result)

# else:
#     print('Operation is invalid')










































# print("Welcome to Coding Embryo Telecoms")
# login = input('Enter the ussd code to begin>>>>:')
# ussd_code = "*478#"
# if login == ussd_code:
#     print("1. Data Plans")
#     print("2. Social Bundles")
#     print("3.Roaming/Int")
#     print("4.Transfer Airtime")
#     print("5.Transfer Data")
#     options = input('Choose from the options above>>:')
#     if options == '1':
#             print('Buy Data Plans')
#             print('1.Daily')
#             print('2.Weekly')
#             print('3.Monthly')
#             print('4.Quaterly')
#             print('5.Yearly')
#     elif options == '2':
#         print('Buy Social Bundles')
#         print('1.Facebook')
#         print('2.Instagram')
#         print('3.Twitter')
#         print('4.Youtube')
#         print('5.Others')
#     elif options == '3':
#         print("3.Roaming/Int")
#         number = []
#         if len(number) <= 10:
#             number = input("Enter your phone number to roam>>>:")
#             print("Roaming Successful")
#         else:
#             print("Phone Number must be 11 digits")
#     elif options == '4':
#         print("4.Transfer Airtime")
#         number = []
#         number = input("Enter phone number to transfer to>>>:")
#         amount = int(input("Enter the amount>>>>:"))
#         if len(number) >= 10:
#             print("Transfer Successful")
#         else:
#             print("Phone Number must be 11 digits")

# else:
#     print('Incorrect Option')



























# CONVERSION OF TEMPERATURE
# k to f : (k - 273.15) * 9/5 + 32
# temp = input('Enter the unit you want to convert from :')
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
#     # quit()

# REGISTRATION OF STUDENT DETAILS ASSIGNMENT
# sd = {}
# size = int(input("Enter the number of student to register>>>:"))
# for i in range(size):
#     student_data = int(input('Enter Student Tag Number:'))
#     sd[student_data] = {}
#     Name = input("Enter student Full Name >>:")
#     Level = int(input("Enter student's level>>:"))
#     Address = input("Enter student's address>>:")
#     Department = input("Enter Department>>:")
#     ID = input("Student ID>>:")
#     GPA = input("Student GPA>>:")
#     sd[student_data]["Name"] = Name
#     sd[student_data]["Level"] = Level
#     sd[student_data]["Address"] = Address
#     sd[student_data]["Department"] = Department
#     sd[student_data]["ID"] = ID
#     sd[student_data]["GPA"] = GPA
# print(sd)

obj = ("This is your objective Questions Page")
que = ("Each Questions carries 5 Marks")
print(obj)
print(que)
p = 0
# QUESTION NUMBER ONE
exer = ("The number of states in Nigeria is_____________")
print(exer)
print("""
        (a) 45 States
        (b) 90 States
        (c) 36 States
""")
exer = input("Choose an Answer from the Options above>>:")
if exer == 'c':
    print("Valid")
  
    p += 5
    # print(p)
    print("You have 5 Marks")
else:
    # return p
    print("Invalid")
    p
    print(p)
# QUESTION NUMBER TWO
exer = ("The capital of United States is_____________")
print(exer)
print("""
        (a) Abuja
        (b) Washington
        (c) New York
""")
exer = input("Choose an Answer from the Options above>>>>>")
if exer == 'b':
    print("Valid")
    p += 5
    # print(p)
    print("You have 5 Marks")
else:
# return p
    print("Invalid")
    p
    print(p)
# QUESTION NUMBER THREE
exer = ("Which of the following is a fruit?_____________")
print(exer)
print("""
        (a) Lagos
        (b) Books
        (c) Orange
""")
exer = input("Choose an Answer from the Options above>>>>>")
if exer == 'c':
    print("Valid")
    p = 0
    p += 5
    # print(p)
    print("You have 5 Marks")
else:
    print("Invalid")
    p=0
    p -= 0
    print(p)
# QUESTION NUMBER FOUR
exer = ("What color represent Agriculture?_____________")
print(exer)
print("""
        (a) Green
        (b) Red
        (c) Black
""")
exer = input("Choose an Answer from the Options above>>>>>")
if exer == 'a':
    print("Valid")
    p = 0
    p += 5
    # print(p)
    print("You have 5 Marks")
else:
    print("Invalid")
    p=0
    p -= 0
    print(p)

# QUESTION NUMBER FIVE
exer = ("Which of the following animal has wings?_____________")
print(exer)
print("""
        (a) A Bird
        (b) A Goat
        (c) A Rat
""")
exer = input("Choose an Answer from the Options above>>>>>")
if exer == 'a':
    print("Valid")
    p = 0
    p += 5
    # print(p)
    print("You have 5 Marks")
else:
    print("Invalid")
    p=0
    p -= 0
    print(p)

# TOTAL MARKS
print("Your Objective Examination is Over,Congratulations!")
total_marks =  p * 5
print("Your Total Mark is")
print(total_marks )