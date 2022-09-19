# import math

# print(dir(math))
# print(help(math))

# import os
#HOW TO PRINT VARIABLE NAME
# print(dir(os))
# print(help(os))
# name = "Embryo"
# HOW TO PRINT FUNCTION WHILE IMPORTING
# def Embryo():
#     return 7

#HOW TO PRINT CLASS NAME.
# class MyEmbryo:
#     def __init__(self):
#         self.name = "embryo"

#     def Embryo(self):
#         return 7

# y = MyEmbryo

# HOW TO BUILD OUR OWN MODULES
class MyEmbryo:
    def __init__(self):
        self.name = "embryo"

    def add(self , x, y):
        """return add of x and y """
        return x + y

    def sub(self , x, y):
        """return sub of x and y"""
        return x - y

    def mul(self , x, y):
        """return mul of x and y"""
        return x * y

    def mud(self, x, y):
        """return mud of x and y """
        return x % y

    def exp(self, x, y):
        """return exp of x and y """
        return x ** y

    def fac(self, x):
        """return fac of x"""
        if x < 0:
            return f'Operation not valid for negative int'
        elif x == 0:
            return 1
        else:
            fac = 1
            for number in range(1, x+1):
                fac *= number
        return fac
    
    def perm(self, x, y):
        """return perm  of x and y"""
        if x < y:
            return f'{x} must be greater than{y}'
        elif x < 0 and y < 0:
            return f'Operation not valid for negative int'
        elif x == 0:
            return 1
        else:
            fac = 1
            for number in range(1, x+1):
                fac *= number
                fac1 = 1
                for other_number in range(1, (x-y)+1):
                    fac1 *= other_number
            perm = fac / fac1
        return perm

    def comm(self, x, y):
        """return comm  of x and y"""
        if x < y:
            return f'{x} must be greater than{y}'
        elif x < 0 and y < 0:
            return f'Operation not valid for negative int'
        elif x == 0:
            return 1
        else:
            fac = 1
            for number in range(1, x+1):
                fac *= number
                fac1 = 1
                for other_number in range(1, (x-y)+1):
                    fac1 *= other_number
                    fac2 = 1
                    for another_number in range(1, y+1):
                        fac2 *= another_number
            comm = fac / (fac1 * fac2)
        return comm










