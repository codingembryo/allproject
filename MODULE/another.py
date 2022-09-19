# from modulee import Embryo

# print(Embryo())

# from modulee import y

# x = y()

# print(x.Embryo())

# import modulee

# print(dir(modulee))

from modulee import MyEmbryo

n =MyEmbryo()


print("Welcome to your Calculation Page")
print("Choose an option below to proceed")
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Modulus')
print('5.Exponential')
print('6.Factorial')
print('7.Permutation')
print('8.Combination')

option = input("Please choose an operation from the above>>>>>:")
if option == '1':
    number1 = int(input("Enter any number here>>>"))
    number2 = int(input("Enter any number here>>>"))
    print(n.add(number1, number2))
elif option == '2':
    number1 = int(input("Enter any number here>>>"))
    number2 = int(input("Enter any number here>>>"))
    print(n.sub(number1, number2))
elif option == '3':
    number1 = int(input("Enter any number here>>>"))
    number2 = int(input("Enter any number here>>>"))
    print(n.mul(number1, number2))
elif option == '4':
    number1 = int(input("Enter any number here>>>"))
    number2 = int(input("Enter any number here>>>"))
    print(n.mud(number1, number2))
elif option == '5':
    number1 = int(input("Enter any number here>>>"))
    number2 = int(input("Enter any number here>>>"))
    print(n.exp(number1, number2))

elif option == '6':
    number1 = int(input("Enter any number here>>>"))
    print(n.fac(number1))

elif option == '7':
    number1 = int(input("Enter any number here>>>"))
    number2 = int(input("Enter any number here>>>"))
    print(n.perm(number1, number2))

elif option == '8':
    number1 = int(input("Enter any number here>>>"))
    number2 = int(input("Enter any number here>>>"))
    print(n.comm(number1, number2))
    
    



# p =Cacu()

# # print(n.add(number1, number2))

# print(n.mud(number1, number2))