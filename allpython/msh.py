# Machine Learning is a subset of AI
1.Import the data
2.Clean the data
3.Split the data into Training/Test sets
4.Create a Model using an algorithm
5.Train the Model
6.Make Predictions
7. Evaluate and Improve i. e. Fine tune the parameters of the model

LIBRARY AND TOOLS FOR ML
Numpy....Provides a multidimensional array.
Pandas....Data analysis library that provides a concept called" DATAFRAMES"
Matplotlib...2 dimensional plotting lib for creating graph and plot.
Scikit- Learn..Most Popular machine learning library that provides common algorithms like decision trees,neuro networks.











# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference

# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet 1']

#     # print(cell.value)
#     # print(sheet.max_row)

#     for row in range(2, sheet.max_row + 1):
#         # print(row)
#         cell = sheet.cell(row, 3)
#         # print(cell.value)
#         corrected_price = cell.value * 0.9
#     # get a reference in the given row
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price

#     Reference(sheet, min_row=2, max_row=sheet.max_row min_col=4, max_col=4)

#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')


#     wb.save(filename)











# from pathlib import Path

# path = Path("ecommerce")
# print(path.rmdir())

#Absolute path
#Relative path
#c:\Program Files\Microsoft

















# import random

# members =['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)


# import random

# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second


# dice = Dice()
# print(dice.roll())

