from gtbbank import Money
from testing import Banking
import mysql.connector
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Multibanks')
manage = connect.cursor()
import random
import re
press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# # # CREATE DATABASE
# # manage.execute("CREATE DATABASE multibanks")
# # manage.execute("SHOW DATABASES")
# # for db in manage:
# #     print(db


# print(f'Welcome to MultiBanks Solutions System Inc')
# print(f'Please Choose a Bank of your Interest and Sign Up to Start Enjoying our Services')
# print(f'1.AccessBank\n2. GT Bank\n3.Polaris Bank')
# option = input("Please Enter an option to proceed>>>>:")
# if option == '1':
#      bank.menu()
    # print("Welcome to Access Bank!.What will you like to do today?")
    # print("""
    #                 ***Main Menu***
    #                 1.Open an Account 
    #                 2.Login to your Account.
    #                 3.Check Account Balance 
    #                 4.Make a transfer 
    #                 5.Buy Airtime.
    #                 6.Buy Data
    #                 7.Call Customer Service
    #                 8.Exit 
    #                 """)

    # option = input("Please select an option>>>:")
#     if option == "1":
#         bank.customer_signup()
# elif option == "2":
#     bank.login()
# elif option == "3":
#     bank.Deposit()
# elif option == "4":
#     bank.transfer()
                



bank = Banking()

# # CREATE TABLE
# manage.execute("CREATE TABLE accessbank (Firstname VARCHAR(30), Surname VARCHAR(30), Email VARCHAR(50), Password VARCHAR(30), BVN INT(11), Username VARCHAR(20), Pin INT(4), Account_number INT(11), Deposit INT(50), Withdrawal INT(50), Account_Balance INT(50))")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)
# bank.customer()
# bank.menu()
# bank.customer_signup()
# bank.login()
# bank.payment()
# bank.Deposit()
# 
# bank.bundle()
# bank.debit()

# class Banking:
    
#     def __init__(self):
#         self.bk = 'bk'
        # self.balance = 0

    # def transfer(self):
    #     self.pin = int(input("Enter Pin>>>>:"))
    #     data = "SELECT * FROM accessbank WHERE pin=%s"
    #     val =(self.pin,)
    #     manage.execute(data, val)
    #     report = manage.fetchone()
    #     print(report)
    #     if self.pin == report[-3]:
    #         transfer_amt = int(input("Enter Amount to Transfer>>>>:"))
    #         transfer_chgs = 57
    #         total_transfer_amount = transfer_amt + transfer_chgs
    #         self.new_balance = int(report[-1])
    #         print(self.new_balance)
    #         if total_transfer_amount <= self.new_balance:
    #             print(f'1.Transfer to Access Bank Account\n2. Transfer to Other Banks.')
    #             choice = int(input("Enter an option>>>>:"))
    #             if choice == 1:
    #                 benef = int(input("Enter Beneficiary Account Number>>>>:"))
    #                 data = "SELECT * FROM accessbank WHERE Account_Number=%s"
    #                 # print(figure)
    #                 val = (benef,)
    #                 manage.execute(data, val)
    #                 report = manage.fetchone()
    #                 # print(report)
    #                 self.accessbal = report[-2]
    #                 print(f'Name:{report[1]} {report [2]}, Access Bank')
    #                 data1 = "SELECT * FROM accessbank WHERE Pin=%s"
    #                 val = (self.pin,)
    #                 manage.execute(data1, val)
    #                 report1 = manage.fetchone()
    #                 print(report1)
    #                 # print(f'Name:{report[1]} {report [2]}, Access Bank')
    #                 if self.pin == report1[-2]:
    #                     self.new_balance -= total_transfer_amount
    #                     self.new_balance = self.accessbal + transfer_amt
    #                     data = "UPDATE accessbank SET balance=%s WHERE Pin=%s"
    #                     data1 = "UPDATE accessbank SET balance=%s WHERE Account_Number=%s"
    #                     val1 = (self.new_balance, self.pin)
    #                     val2 = (self.new_balance,benef)
    #                     manage.execute(data, val1)
    #                     manage.execute(data1, val2)
    #                     connect.commit()
    #                     print(connect.rowcount, 'record updated successfully')
    #                 else:
    #                     print(f'Incorrect Pin!\nTry again.')


# DATA SCIENCE
# Data Science is an interdisciplinary field at the intersection of Statistics, Computer Science, Machine Learning, and Business.

# bank.login()
# bank.Deposit()
# bank.Balance()
# bank.Withdrawal()
# bank.customer_signup()
# bank.debit()
# bank.transfer()

# bankme = Money()
# bankme.customer()
# bankme.login()
# bankme.Deposit()
# bankme.transfer()
# bankme.debit()
# bankme.Balance()



