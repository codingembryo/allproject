# LOOP
# Loop is a statement that contains instructions that continually repeats until a certain condition is reaches.
# And with the use of loops we can cut short hundred lines of code to a few...

# e.g 
# for x in range(10):
#     print('Hello world')


# Two types of loop:
# for loop and while loop

# A for loop is used for iterating over a sequence(i.e list, a tuple, a dictionary, set, or a string. It can also
# be used to iterate over a sequence of numbers using range.

# Looping through a List
# name = ["kola", "bisi", "paul", "gabriel"]

# for x in name:
#     print(x)
    
# for x in name[-1]:
#     print(x)

# Looping through a string
# for x in "banana":
#     print(x)
    
# Looping through a tupple
# name = tuple((5, "jude", "paul", True, 20, 10.50))

# for x in name:
#     print(x)
Looping through a dictionary
product = {'producer':'Toyota', 'model':'venza 2021', 'engine':'6 engine', 'color':'black', 'gear':6, "ok":True}

# for x in product.keys():
#     print(x)
# for x in product.values():
#     print(x)
    
for x, y in product.items():
    print(x, ":", y)

for x in product.items():
    print(x)

# using range(number)
# for x in range(5):
#     print(x)

# # print out 3,4,5
# for x in range(3, 6):
#     print(x)

# # print out 3,5,7
# for x in range(4, 10, 2):
#     print(x) 
# n = int(input('Enter value for n: '))
# k = int(input('Enter value for k: '))
# # for x in range(n, k, 5):
# #     print(x)
    
# for j in range(5, k, n):
#     print(j)

# new = (1, 2, 3, 4)

# for j in new:
#     print(j)
# else:
#     print('No more item')

# Nested For loop
# A nested loop is a loop inside a loop. The inner loop will be executed one time for each iteration of the outer loop..

# pro = ["green", "small", "sweet"]

# fruits = ["mango", "orange", "cherry"]

# for x in pro:
#     for j in fruits:
#         print(x, j)

# ass solution

# n = int(input('Enter value for n: '))
# k = int(input('Enter value for k: '))

# even = []
# odd = []
# prime = []

# for i in range(n, k):
#     if i % 2 == 0:
#         even.append(i)
#     elif i % 2 != 0:
#         odd.append(i)
#     elif (k % i != 0 ):
#         prime.append(i)

# print('Even: ', even)
# print('Odd: ', odd)
# print('Prime: ', prime)

# else:
#     prime.append(i)
#     print('Prime: ', prime)
# print('Even: ', even)
# print('Odd: ', odd)
# print('Prime: ', prime)

# number_one = int(input('>>> '))
# for i in range(2, number_one):
#     if number_one % i ==0:
#         print(number_one, 'is not a prime number')
#         break
# else:
#     print(number_one, 'is a prime number')



#  while loop
# While loop continually executes the statement(code) as long as the given condition is TRUE. 
# n = int(input('>>> '))
# while n <= 10:
#     print('Hello World')
#     break

# num = 1
# even = []

# while num <= 10:
#     if num % 2 == 0:
#         even.append(num)
#     num += 1
# print(even)

# even = []

# for i in range(1, 10):
#     while i % 2 == 0:
#         even.append(i)
#         break
# print(even)

# i = 1

# while i < 6:
#     print(i)
#     i += 1

# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("Not less than 6")


# BREAK statement
# Continue
# Pass

# Break

# count = 0

# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
    # count += 1: if we put  += 1 here that means we want to include 5 to the output
    # print(count): if we put print here that means we want to remove 0 from the output

# while count <= 20:
#     print(count)
#     count += 1 
#     if count == 10:
#         break
    # count += 1: if we put  += 1 here that means we want to add 10 to the output
    # print(count): if we put print here that means we want to remove 0 from the output
    
    
    

# name = ["kola", "bisi", "paul", "gabriel"]

# for x in name:
#     if x == 'mary':
#         break
#     print(x) 

 Continue

count = 0

while count < 20:
    print(count)
    count += 1 
    # if count == 10:
        # continue



# name = ["kola", "bisi", "paul", "gabriel"]

# for x in name:
#     if x == 'bisi':
#         continue
        
#     print(x)   

# Pass
# statement is used when we want to do nothing when the condition is met. it doesnt skip or stop
# the execution.

# num = 1
# while num <= 10:
#     if num == 6:
#         pass
#     print(num)
#     num += 1
    



        