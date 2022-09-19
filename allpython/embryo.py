# CLASS
# OBJECT
# This has  attributes 
# Take a task as an object.
# After initializing our object,
# We have to use self for function.
# to print your function,you must call it.
# Always remember to call your function

# MODULES


# FIRST LECTURE ABOUT CLASS
class Paul:
    def __init__(self):
        self.name = "Paul"
        self.age = 11
        self.leg = 2

    # def going(self):
    #     print(f"{self.name} is going")
        
    def throw(self):
        print(f"{self.age * self.leg}")

m = Paul()
m.going
m.throw()
# ANOTHER WAY TO CALL YOUR FUNCTION INSIDE YOUR initialized
# self.going()

# INHERITANCE
class Father:
    def __init__(self):
        self.name = "Mike"
        self.location = "Moniya"

    def mylocation(self):
        print(f"{self.name} is living at {self.location}")


class Son(Father):
    def __init__(self):
        # Father.__init__(self)
        super().__init__()
        self.name = "John"
        self.address = "Akingbile"

    def sonlocation(self):
        print(f"{self.name} is living at {self.address} {self.location}")


m = Son()
m.sonlocation()
















# t = []
# for i in range(5):
#     s = int(input('Enter a figure'))
#     t.append(i)
#     print(i)





#  MULTIPLICATIONS/TIMESTABLE
# t = int(input("Enter a number>>>>>>"))
# even = []
# odd = []
# for i in range (1,13):
#     n = t*i
#     print(t, 'x', i, '=', n)
#     if n%2==0:
#         odd.append(n)
#     else:
#         even.append(n)
#     print(even)
#     print(odd)




    








# student= {}
# register = input(input("Enter the number of student you want to register........"))
# name = input('Enter full name')
# level = input('Enter student level')
# address = input('Enter student address')
# department = input('Enter your department')
# print(register)
# print(name)
# print(level)
# print(address)
# print(department)
# for i in 















# Looping through a dictionary
# product = {'producer':'Toyota', 'model':'venza 2021', 'engine':'6 engine', 'color':'black', 'gear':6, "ok":True}

# for x in product.keys():
#     print(x)
# for x in product.values():
#     print(x)
    
# for x, y in product.items():
#     print(x, ":", y)

# for x in product.items():
#     print(x)

# numbers = []
# odd = []
# even = []
# prime = []
# for i in numbers:
#     if i%2 == 1:
#         odd.append(i)
#     elif i%2 == 0:
#             even.append(i)
# for x in numbers:
#     if x>1:
#         for n in range(2,x):
#             if x%n==0:
#                 break
#         else:
#             prime.append(x)
# print(numbers)
# print(f"odd numbers= {odd}")
# print(f"even numbers = {even}")
# print(f"prime numbers = {prime}")




# name = 'John Smith'
# age = 20
# is_new = True
# print(name)
# print(age)
# print(is_new)







# WHILE AND IF TO GET EVEN NUMBER
# num = 1
# even = []

# while num <= 10:
#     if num % 2 == 0:
#         even.append(num)
#     num += 1
# print(even)

# TO REQUEST THE USER TO ENTER AN INPUT( FOR AND WHILE TO GET EVEN NUMBER)
# even = []
# n = int(input('Enter a number'))
# for i in range(2, n):
#     while i % 2 == 0:
#         even.append(i)
#         break
# print(even)


# for x in range(4,10,2):
#  Continue
# count = 0
# while count < 20: 
#     print(count)
#     count += 1
   
    # if count == 10:
        # continue

# count = 0

# while count < 20:
#     print(count)
#     count += 1 
#     if count == 10:
#         continue


# name = ["kola", "bisi", "paul", "gabriel"]

# for x in name:
#     if x == 'paul':
#         break
#     print(x) 

    # print (x)

# for x in range(20, 35, 7):
    # print(x)

# n = int(input('Enter value for n: '))
# k = int(input('Enter value for k: '))
# for x in range(n, k, 5):
#     print(x)
# new = (1, 2, 3, 4)

# for j in new:
#     print(j)
# else:
#     print('No more item')






# for j in range(5, k, n):
#     print(j)




# ****************MUST READ******************
# DATA TYPE AND THEIR METHOD
# PYTHON OPERATORS
# p = []
# for x in range(1500,2701):
#     if(x % 5 == 0) and (x % 7 == 0):
#         p.append(x)
#         print(p)
# do prime,even number and odd

# n = []
# for i in range(200):
#     if n / 2 == 0:
#         n.append(i)
#         print(n)
# PRIME NUMBER
# lower = int(input("Enter the lower value:"))
# upper = int(input("Enter the upper value:"))
# for number in range(lower,upper+1):
#     if number>1:
#         for i in range(2,number):
#             if (number%i)==0:
#                 break
#         else:
#             print(number)

# # EVEN NUMBER
# t = []
# for i in range(t):
#   if i % 2 == 0:
#     t.append(i)
#     print(t)

# for x in range(2,50,2):
#         print(x)
        
# y=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         y.append(str(x))
# print (','.join(y))

# TEMPERATURE CONVERSION
# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]
# if i_convention.upper() == "C":
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")




# 18 AUGUST,2022


# CONDITIONAL STATEMENT
# LOGICAL CONDITIONAL OPERATION
# INDENTATION
# less than or equal to: <=

# x = 60
# if x > 50:
#     print('Very Good')
# elif x == 50:
#     print('Good')

# else:
#     print('Fair')

# MODULUS
# The modulus works with only the remainder.








# obj = ("This is your objective Questions Page")
# que = ("Each Questions carries 5 Marks")
# print(obj)
# print(que)
# p = 0
# # QUESTION NUMBER ONE
# exer = ("The number of states in Nigeria is_____________")
# print(exer)
# print("""
#         (a) 45 States
#         (b) 90 States
#         (c) 36 States
# """)
# exer = input("Choose an Answer from the Options above>>:")
# if exer == 'c':
#     print("Valid")
  
#     p += 5
#     # print(p)
#     print("You have 5 Marks")
# else:
#     # return p
#     print("Invalid")
#     p
#     print(p)
# # QUESTION NUMBER TWO
# exer = ("The capital of United States is_____________")
# print(exer)
# print("""
#         (a) Abuja
#         (b) Washington
#         (c) New York
# """)
# exer = input("Choose an Answer from the Options above>>>>>")
# if exer == 'b':
#     print("Valid")
#     p += 5
#     # print(p)
#     print("You have 5 Marks")
# else:
# # return p
#     print("Invalid")
#     p
#     print(p)
# # QUESTION NUMBER THREE
# exer = ("Which of the following is a fruit?_____________")
# print(exer)
# print("""
#         (a) Lagos
#         (b) Books
#         (c) Orange
# """)
# exer = input("Choose an Answer from the Options above>>>>>")
# if exer == 'c':
#     print("Valid")
#     p = 0
#     p += 5
#     # print(p)
#     print("You have 5 Marks")
# else:
#     print("Invalid")
#     p=0
#     p -= 0
#     print(p)
# # QUESTION NUMBER FOUR
# exer = ("What color represent Agriculture?_____________")
# print(exer)
# print("""
#         (a) Green
#         (b) Red
#         (c) Black
# """)
# exer = input("Choose an Answer from the Options above>>>>>")
# if exer == 'a':
#     print("Valid")
#     p = 0
#     p += 5
#     # print(p)
#     print("You have 5 Marks")
# else:
#     print("Invalid")
#     p=0
#     p -= 0
#     print(p)

# # QUESTION NUMBER FIVE
# exer = ("Which of the following animal has wings?_____________")
# print(exer)
# print("""
#         (a) A Bird
#         (b) A Goat
#         (c) A Rat
# """)
# exer = input("Choose an Answer from the Options above>>>>>")
# if exer == 'a':
#     print("Valid")
#     p = 0
#     p += 5
#     # print(p)
#     print("You have 5 Marks")
# else:
#     print("Invalid")
#     p=0
#     p -= 0
#     print(p)

# # TOTAL MARKS
# print("Your Objective Examination is Over,Congratulations!")
# total_marks =  p * 5
# print("Your Total Mark is")
# print(total_marks )
















# COMPUTER OBJECTIVES AND THEORY QUESTIONS AND ANSWERS
# obj = ("Welcome to your objective page")
# print(obj)
# que = ("Each Questions carries 5 Marks")
# print(que)
# print("""
#     Enter a,b or c  to choose your option.

#     Question 1
#     The Capital of Oyo State is ......

#     (a)New York
#     (b)Ibadan
#     (c)Ondo
# """)
# answer = ["a", "b", "c"]
# options = input("Enter your option>>>>>>>>>")
# p = "correct answer"
# score = 0
# r = "incorrect answer"
# if options == answer[1]:
#   print(p)
# else:
#     print(r)






    





























# TUESDAY 16TH AUGUST
# dictionary
# Dic goes with key and value.
# key{value} first method
# dict(key=value)
# print(product["producer"])
# print(product.get("producer"))
# # .item will print key and value and put it in a bracket
# print("model in product")( A boolean result)
# # To check if a value is in a variable. It will be false because it only recognizes KEY
# # To change value
# # to change color
# product["color"] = "white"
# print(product)
# update
# Update can carry more than one items at a time i.e key and value.
# product.update({"year":2021, "color":"white", "speed":"500mph"})
# TO DELETE THE KEY AND THE VALUE
# product.pop('color')
# print(product)
# READ NESTED DICTIONARY**********




# MONDAY AUGUST 15,2022
#  TOPIC:SET

# CLASSWORK
# Write a python program that accepts 2 input and print SET as your final output. 
# SOLUTION
# listy = []
# listz = []
# for i in range(1,5):
#     p = int(input("Enter value p >>"))
#     q = int(input("Enter value q >>"))
#     listy.append(p)
#     listz.append(q)
# # print(listy)
# # print(listz)
# SetR = set(listy)
# SetZ = set(listz)
# print(SetR)

# ASSIGNMENT DONE

# y = {2,4,6,8,10,12,14}
# x = {3,5,7,9,11,13,15}
# # p = set((20,50,43))
# z = y.union(x)
# print(z)
# intercept = y.intersection((x))
# print(intercept)
# y.update(x)
# print(y)
# y.difference_update(x)
# print(y)
# x.update(p)
# print(x)
#  p.add{99,1002}
#  print(p)









# pray = []
# for pol in range(5):
#     name = input('Enter a number>>')
#     pray.append(name)
# print(pray)

# 11 AUGUST 2022
# tuple
# A tuple is created using using braces.
# name = ("Shade")
# we can use ordinary or tuple then another bracket.
# Use slicing method to select.

# UNPACKING VALUES OF tuple
# to by pass the error put * sign before the last value.
# + is used for tupple because you cannot use add
# Note***
# When for is used it prints vertically.
# membership operator---in /not in
# add puts the data type at the back of the values.
# update 

# fruits = tuple(('Name', 'name', 'age',12, 'Age'))
# print(fruits.index('name'))

# You have one input ,make that input to run 5 times.
# let the input be inside the for loop.





# 10 AUGUST 2022
# TOPIC: LOWER FUNCTION
# name = 'SUNDAY'
# print(name.lower())
# value = "method"
# user = input("please enter a method to continue: ")
# if value == user.lower():
#     print(user)
# else:
#     print("invalid input")

# value = "METHOD"
# user = input("please enter a method to continue: ")
# if value == user.upper():
#     print(user)
# else:
#     print("invalid input")
# REPLACE FUNCTION
# comment = """   commented that this is a python class. It was started last week and still continue through this week. The number of people in this class is  """

# # newval = comment.replace("commented" ,"java")
# # print(newval)

# # SPLIT FUNCTION
# comment = """   commented that this is a python class. It was started last week and still continue through this week. The number of people in this class is  """
# # print(comment.split())
# print(comment.split('.'))

# # Join() function
# word_split = comment.split()
# print(word_split)

# value = ["rice", "beans", "yam", "banana"]
# print(value)
# print(' '.join(value))

# # CAPITALIZE () FUNCTION
# comment = """commented that this is a python class. It was started last week and still continue through this week. The number of people in this class is  """
# print(comment.capitalize())

# Title()function
# print(comment.title())
# next line
# paul="i am coming\n\n pal"
# print(paul)

# # Count() f
# print(comment.count("python"))

# In operator
# val = "week" in comment
# print(val)
# val = "weak" not in comment
# print(val)

# concatination
# f represents format

# name = "paul"
# num = 6
# comment = f"""{name}commented that this is a python class. It was started last week and still continue through this week. The number of people in this class is {num}"""
# print(comment)

# escape character
# print('she\'s the owner paul says and i quote God is Good')

# break/cut

# # ARRAY:
# list
# tuple
# set
# dictionary

# List is a collection which is ordered and changeable.
# A list is created with a square bracket [] or list() constructor.
# my_list = ["Shade","energy", "magnet","charse", "energy"]
# my_list2 = list((12, 14, "sunday", "charse", True, False, 5.08))
# my_list3 = [1, 45, 54, 23, 67, 78, 46]
# my_list2.reverse()
# print(my_list)
# print(type(my_list))
# if "energy" in my_list:
#     print("present")
# else:
#         print("not available")
# .remove
# .append(use for statement) for name in my list 2))
# .extend
# .pop
# .insert
# .clear
# .sort- arrange items in ascending order.
# del
# .sort(reverse=True)
# .reverse
# .count
# .sort(reverse=True, key=str.lower)
# .copy----You can use list inside a variable name. same as copy.
# my_list = ["Shade","energy", "magnet","charse", "energy"]

# TO EXPLAIN LATER HOW IT PRINT
# my_list4 = [my_list, my_list2,my_list, ['Favour', 34],my_list2, 'Tunde', False]
# # print(my_list4)
# print(my_list4[4][-5])
# # print(my_list4[4])
# # print(my_list4[4][-6])
















# SIMPLE INTEREST ASSIGNMENT
# p = int(input("Enter Principal>>"))
# r = float(input("Enter Rate>>"))
# t = int(input("Enter Time>>"))
# d = 100
# si = p * r * t / d
# print(si)
# 09 august 2022
#STRING SLICING
# name = 'Monday'
# print(name)

# name = 'monday'
# print (name[2])

# name = 'monday'
# print(name[3:6])
# name = 'commented'
# print(name[-3:])

# name = 'commented'
# print(len(name))
# name = "234567"
# print(name[2])
# print(name[-3:])
# print(len(name))
# comment = """   commented that this is a python class. It was started last week and still continue through this week. The number of people in this class is   """

# print(len(comment))
# print(comment[27:39])

# STRING METHOD
# print(comment.startswith("commented"))
# print(comment.endswith("is"))

# The result is showing false because of the space added to the above statement.

# print("the length of the comment is ", len(comment))

# STRIP FUNCTION()
# print('length before strip is ', len(comment))
# print('length after strip is ',len(comment.strip()))


# val1 = float(input("enter value 1>>"))
# val2 = float(input("enter value 2>>"))
# print('''
#         addition
#            subtraction 
# ''')
# add = 'addition'

# oper = input('enter operation: ')
# # if oper.strip() == add:
# if oper.strip() == 'addition':
#     print(val1 + val2)
# elif oper.strip() == 'subtraction':
#     print(val1 - val2)
# else:
#     print('invalid selection')
    


















#ARITHMETIC OPERATORS: +, -, /,
# numberone = 15
# numbertwo = 10
# total_number = (numberone + numbertwo)

# print(total_number)
# print(type(total_number))

# x = int(input('X: '))
# y = int(input('Y: '))
# z = x / y
# print('Z:' , z)

# x = 5
# x += 5

# print(x)
# x = 30
# x -= 10
# print(x)
# x = 15
# y = 10
# total = x > y
# print(total)
# print(type(total))

# x = 5
# y = 10
# total = x != y
# print(total)

# x = 5
# y = 10
# total = (x >= y)

# x = 15
# y = 10
# total_number = (x >= y) or (x != y)
# print(total_number)

# one = [1,2,3,4,5,6,7,8,9,]
# two = 1
# total = two in one
# print(total)

# fruit = ['mango','banana', 'orange', 'pawpaw']

# mix = 'pear'
# print(mix in fruit)


# mm = [1,2,3,4,5,6]
# for i in mm:
#     print(type(i))

    # x = 5
    # y = 5
    # z = 15
    # if (x==y) & (z <= y) | (y)
    




























# CANNOT CONVERT
# name = "paul"
# age = int(name)

# print(age)
# ***NOTE**
# It can only convert a string of numbers and not letters.

# example

# name = int("12")
# age = int(name)
# print(age)

# name = list ["paul"]
# print(name)
# print(type(name))

# NAIRA TO DOLLAR
# naira = float (input("Enter your naira amount here>>"))
# rate = float (input("Enter your rate>>"))
# dollar = naira / rate
# print(f"The convertion of #{naira} to dollar is {dollar} using {rate} conversion rate")

# dollar = int(input("Enter your dollar amount here>>"))
# rate = int(input("Enter your rate>>"))
# naira = dollar * rate
# print(f"The convertion of ${dollar} to naira is {naira} using {rate} conversion rate")





















# NAIRA TO USD
# USD = int(input("Enter the amount in dollars="))
# NAIRA = 700
# USD = USD * NAIRA
# print(USD)
# print(type(USD))



# # USD TO NAIRA
# NAIRA = int(input("Enter the NAIRA amount to be converted="))
# USD= 0.0050
# NAIRA = USD * NAIRA
# print(NAIRA)
# print(type(NAIRA))

# EXCHANGE RATE
# Currency= input("Enter the currency: ")
# Amount= int(input("Enter the amount : "))
# Rate = 700 
# Total = 700 * Amount
# print(Total)
































# NAIRA = (input("Enter the Naira amount="))
# USA = 0.0024
# NAIRA = USA * NAIRA
# print(NAIRA)
# print(type(NAIRA))



# print("Hello world")

# number1 = 30
# number2 = 40

# total = number1 + number2

# print(total)


# number4 = 120
# number8 = 300


# total = number4 + number8

# print(total)

# name = "paul"
# print(name)

# age = 7
# print(age)
# print(type(age))

# number = {"name":"paul","age":7,"price":34.78}
# print(number)
# print(type(number))


# name = input("What is your name")
# print(name)
# print(type(name))

# number1 = int(input("What is your name"))
# number2 = int(input("What is your name"))
# total =number1 + number2

# print(total)
# print(type(total))



# amount = int(input("Enter Amount in Dollars: "))

# Naira = input("Please enter the currency code that has to be converted: ").upper()

# Dollars = input("Please enter the currency code to convert: ").upper()

# print("You are converting", amount, Dollars, "to", NAIRA,".")

# amount = cr*USD

# print('The product is: ', amount)








# from forex_python.converter import CurrencyRates

# cr = CurrencyRates()

# amount = int(input("Please enter the amount you want to convert: "))

# from_currency = input("Please enter the currency code that has to be converted: ").upper()

# to_currency = input("Please enter the currency code to convert: ").upper()

# print("You are converting", amount, from_currency, "to", to_currency,".")

# output = cr.convert(from_currency, to_currency, amount)

# print("The converted rate is:", output)





