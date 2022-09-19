# A module is a file containing Python code.
# A package, however, is like a directory that holds sub-packages and modules.
# You can call it library or a package.
# A package or library contains multiple modules. Multiple modules inside a folder is package.
# Anytime you want to do anything with Data Science,you're actually working with libraries.


# exponential
# modulus
# division
# floor division



# n = input("Enter a number")
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
      
# print ("The factorial of 23 is : ",end="")
# print (fact)

# class Jets:
    
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
        
        
# first_item = Jets("F16", "USA")


# # a=first_item.name
# # print(a)

# b=first_item.origin
# print(b)




class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jets("A45","FRANCE")
second_item=Jets("B34","RUSSIA")
third_item=Jets( "C45","USA")
fourth_item=Jets( "D11","UK")
fifth_item=Jets( "E57","EUROPE")
sixth_item=Jets( "F56","DUBAI")
    
first_army=[first_item.name,first_item.origin,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
print(first_army)
