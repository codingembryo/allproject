# PYTHON FUNCTION

# Python Functions is a block of statements that return the specific task OR a block of code which only runs when it is called..

# The idea is to put some commonly or repeatedly done tasks together and 
# make a function so that instead of writing the same code again and again for different inputs, 
# we can do the function calls to reuse code contained in it over and over again.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.
# Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) )
# creating a function
# def my_function():
#     print("Hello from a function")
      
# my_function()    
# # calling a function
# def my_function():
#       print("Hello from a function")

# my_function()

# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, 
# just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, 
# we pass along a first name, which is used inside the function to print the full name:

# Example
# def my_function(fname):
#   print(fname, " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# PARAMETERS
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.



# Example
# This function expects 2 arguments, and gets 2 arguments:

# def paul(fname, lname):
#   print(fname + " " + lname)

# paul("Emil", "Refsnes")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example
# If the number of arguments is unknown, add a * before the parameter name:

# def my_function(kids):
#   print("The youngest child is " , kids[2])

# my_function("Emil", "Tobias", "Linus")




# def my_func():
#       print("Hello! Hope you're doing well")
# my_func()     
# def greet(name):
#     """
#     This function greets to
#     the person passed in as
#     a parameter
#     """
#     print("Hello, " + name + ". Good morning!")
    
    
    
# def greet(name):
#     print("""
#     This function greets to
#     the person passed in as
#     a parameter
#     """)
#     print("Hello, " + name + ". Good morning!")

# greet('Paul')




# # A simple Python function to check
# # whether x is even or odd
 
 
# def evenOdd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")
 
 
# # Driver code to call the function
# evenOdd(2)
# evenOdd(3)
# evenOdd(3)
# evenOdd(2)
# evenOdd(3)



# def first_input(num):
#     okay = []
#     final = []

#     for i in range(5):
#         second_input = int(input('>>> '))
#         okay.append(second_input)
#         let = second_input * num
#         final.append(let)
    
#     print(final)
# first_input(4)

# def paul():
#     okay= []
#     mm = []
#     # print('hello world', name, 'is', age)
#     for i in range(5):
#         my = int(input('enter >>> '))
#         okay.append(my)
#         m = okay[0] * my
#         mm.append(m)

#     print(mm)
# paul()




# # # # callin a function inside another function

# def mike():
#     paul()
# mike()




# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), 
# and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# Example
# def my_function(food):
#   for x in food:

#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)


# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables are those which are not defined inside any function and have a global scope

# Global variables can be used by everyone, both inside of functions and outside.
# global variables are accessible throughout the program and inside every function.

# Example
# Create a variable outside of a function, and use it inside the function

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()



# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# # use function for ussd code
# # function for the assignment

# LOCAL VARIABLE
#  Local variables are those which are defined inside a function and its scope is limited to that function only. 
#  In other words, we can say that local variables are accessible only inside the function in which it was initialized...


# def f():
  
#     # local variable
#     s = "I love Geeksforgeeks"
#     print(s)
# f()

# If we will try to use this local variable outside the function then let’s see what will happen.

# Example:


# def f():
      
#     # local variable
#     s = "I love Geeksforgeeks"
#     print("Inside Function:", s)
  
# # Driver code
# f()
# print(s)



# These are those which are defined outside any function and which are accessible throughout the program, i.e., 
# inside and outside of every function. Let’s see how to create a global variable.

# Example: Defining and accessing global variables


# # This function uses global variable s
# def f():
#     print("Inside Function", s)
  
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print("Outside Function", s)


# def f():
#     s = "Me too."
#     print(s)
  
  
# # # Global scope
# s = "I love Geeksforgeeks"
# f()
# print(s)


# a = 1 
# # # Uses global because there is no local 'a'
# def f():
#     print('Inside f() : ', a)
# f()


# Function Arguments
# You can call a function by using the following types of formal arguments −

# Required arguments
# Keyword arguments
# Default arguments
# Variable-length arguments

# Default Arguments
# A default argument is a kind of parameter that takes as input a default value if no value is supplied for the argument when the function 
# is called. Default arguments are demonstrated in the following instance.

# Code

# # Python code to demonstrate the use of default arguments  
# # defining a function  
# def function( num1, num2 = 40 ):  
#     print("num1 is: ", num1)  
#     print("num2 is: ", num2)  

   
   
# # # Calling the function and passing only one argument  
# print( "Passing one argument" )  
# function(10)  




# Keyword Arguments
# The arguments in a function called are connected to keyword arguments. If we provide keyword arguments while calling a function, 
# the user uses the parameter label to identify which parameters value it is.

# Since the Python interpreter will connect the keywords given to link the values with its parameters, we can omit some arguments or 
# arrange them out of order. The function() method can also be called with keywords in the following manner:

# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

# Example
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Code

# # Python code to demonstrate the use of keyword arguments  
  
# # Defining a function  
# def function( num1, num2 ):  
#     print("num1 is: ", num1)  
#     print("num2 is: ", num2)  
  
# # Calling function and passing arguments without using keyword  
# print( "Without using keyword" )  
# function( 50, 30)     
      
# # Calling function and passing arguments using keyword  
# print( "With using keyword" )  
# function( num2 = 50, num1 = 30)  


# Required Arguments
# The arguments given to a function while calling in a pre-defined positional sequence are required arguments. 
# The count of required arguments in the method call must be equal to the count of arguments provided while defining the function.

# We must send two arguments to the function function() in the correct order, or it will return a syntax error, as seen below.

# Code

# # Python code to demonstrate the use of default arguments  
  
# # Defining a function  
# def function( num1, num2 ):  
#     print("num1 is: ", num1)  
#     print("num2 is: ", num2)  
  
# # Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30  
# print( "Passing out of order arguments" )  
# function( 30, 20 )     
  
# # Calling function and passing only one argument  
# print( "Passing only one argument" )  
# try:  
#     function( 30 )  
# except:  
#     print( "Function needs two positional arguments" )  


# Variable-Length Arguments
# We can use special characters in Python functions to pass as many arguments as we want in a function.
# There are two types of characters that we can use for this purpose:

# *args -These are Non-Keyword Arguments
# **kwargs - These are Keyword Arguments.
# Here is an example to clarify Variable length arguments

# Code

# # Python code to demonstrate the use of variable-length arguments  
   
# Defining a function  
# def function( *args_list ):  
#     ans = []  
#     for l in args_list:  
#         ans.append( l.upper() )  
#     return ans  
# # Passing args arguments  
# object = function('Python', 'Functions', 'tutorial')  
# print( object )  
# def function( *args_list ):  
#     ans = []  
#     for l in args_list:  
#         ans.append( l.upper() )  
#     print (ans ) 
# # Passing args arguments  
# function('Python', 'Functions', 'tutorial')  
  
# # defining a function  
# def function( **kargs_list ):  
#     ans = []  
#     for key, value in kargs_list.items():  
#         ans.append([key, value])  
#     return ans  
# # Paasing kwargs arguments  
# object = function(First = "Python", Second = "Functions", Third = "Tutorial")  
# print(object)











    













# # use function for ussd code
# # function for the assignment






