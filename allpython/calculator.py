first_num = int(input('Enter a number>>>>>:'))
second_num = int(input('Enter another number>>>>>>:'))
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4. Division')
print('5.Exponential')
option = input("Please choose an operation from the above>>>>>:")
if option == '1':
    total = first_num + second_num
    print(total)
elif option == '2':
    result = first_num - second_num
    print(result)
elif option == '3':
    result = first_num * second_num
    print(result)
elif option == '4':
    result = first_num / second_num
    print(result)
elif option == '5':
    result = first_num ** second_num
    print(result)

else:
    print('Operation is invalid')





# FACTORIAL!
# FUNCTION METHOD
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# num = int(input("Enter a number"))
# result = factorial(num)*+-
# print("The factorial of", num, "is", result)

# PROCEDURAL METHOD
# n = 23
# fact = 1
  
# for i in range(1,n+1):
#     fact = fact * i
      
# print ("The factorial of 23 is : ",end="")
# print (fact)