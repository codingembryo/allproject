# LIST
# numbers = [5, 2, 1, 5, 7, 4]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)








# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# matrix = [
#     [1, 2, 3],
#     [4, 5 ,6],
#     [7, 8, 9]

# ]
# for row in matrix:
#     for item in row:
#         print(item)







# matrix[0][1] = 20
# print(matrix[0][1])
















# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names[:2])
# print(names)



# We can generate a list of corrdinates using nested loops
#
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y}) ')
# # NESTED LOOPS
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)




# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# for item in range(5,10, 2)
#     print(item)






# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")

# GUESSING GAME
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess'))
#     guess_count += 1
#     if guess == secret_number:
#         print("Yon Won!")
#         break
# else:
#     print('Sorry you failed')


# command = ""
# started = False
# print("Enter a command to start the car")
# print("""
#         start - To start the car
#         stop -  To stop the car
#         quit - to quit
        
#         """)
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#         print("car Started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
#         start - To start the car
#         stop -  To stop the car
#         quit - to quit
        
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I don't Understand that")







