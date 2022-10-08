# import mysql.connector
# mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='tradingapp')
# mycursor = mycon.cursor()


# # mycursor.execute("CREATE TABLE bankpool (acc_no int primary key auto_increment,name varchar(30), city char(20), mobile_no char(10), balance int(6))")

# # mycursor.execute("CREATE TABLE transactions (acc_no int,amount int(6),ttype char(1),foreign key (acc_no) references bankpool(acc_no))")

# # mycursor.execute("SHOW TABLES")
# # for table in mycursor:
# #     print(table)

import mysql.connector
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Multibanks')
manage = connect.cursor()
import random
import re
press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# CREATE DATABASE
# manage.execute("CREATE DATABASE Multibanks")
# manage.execute("SHOW DATABASES")
# for db in manage:
#     print(db)

# CREATE TABLE
# manage.execute("CREATE TABLE bankusage (Account_Number INT primary key, Firstname VARCHAR(30), Surname VARCHAR(30), Email VARCHAR(50), Password VARCHAR(30), Phone INT(11) NOT NULL, Username VARCHAR(8),Pin INT(4) UNIQUE, Deposit INT(50), Withdrawal INT(50), Account_Balance INT(50))")
# # manage.execute("SHOW TABLES")
# # for table in manage:
# #     print(table)

# manage.execute ("CREATE TABLE transact (Account_Number int(10),Amount int(10),ttype char(1),foreign key(Account_Number) references bankusage (Account_Number))")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)

# CREATE TABLE
# manage.execute("CREATE TABLE gtbank (Account_Number VARCHAR(10), Firstname VARCHAR(30), Surname VARCHAR(30), Email VARCHAR(50), Password VARCHAR(30), Phone VARCHAR(11), Username VARCHAR(8),Pin INT(4), new_balance VARCHAR(50))")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)

# TO CREATE ANOTHER COLUMN in IN A TABLE
# manage.execute("ALTER TABLE accessbank add column new_balance varchar(10)")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)

class Money:
    
    def __init__(self):
        self.bk = 'bk'
        # self.balance = 0

    # def menu(self):
    #     print("Welcome to GTBank!.What will you like to do today?")
    #     print("""
    #             ***Main Menu***
    #             1.Open an Account 
    #             2.Login to your Account.
    #             3.Check Account Balance 
    #             4.Make a transfer 
    #             5.Buy Data/Buy Airtime.
    #             6.Call Customer Service
    #             7.Exit 
    #             """)
    #     option = input("Please select an option>>>:")
    #     if option == "1":
    #         bank.customer_signup()
    #     elif option == "2":
    #         bank.login()
    #     elif option == "3":
    #         bank.Deposit()
    #     elif option == "4":
    #         bank.transfer()
    #     elif option == "5":
    #         bank.bundle()
    #         # elif option == "6":
    #         #     bank.service()
    #         # elif option == "7":
    #         #     quit()
        
    #     elif choice == '2':
    #         print("Welcome to GT Bank!.What will you like to do today?")
    #         print("""
    #             ***Main Menu***
    #             1.Open an Account 
    #             2.Login to your Account.
    #             3.Check Account Balance 
    #             4.Make a transfer 
    #             5.Buy Airtime.
    #             6.Buy Data
    #             7.Call Customer Service
    #             8.Exit 
    #             """)
    #         option = input("Please select an option>>>:")
    #         if option == "1":
    #             bank.customer_signup()
    #         elif option == "2":
    #             bank.login()
    #         elif option == "3":
    #             bank.accountbal()
    #         elif option == "4":
    #             bank.transfer()
    #         elif option == "5":
    #             bank.airtime()
    #         elif option == "6":
    #             bank.data()
    #         elif option == "7":
    #             bank.service()
    #         elif option == "8":
    #             quit()

    #     elif choice == '3':
    #         print("Welcome to Polaris Bank!.What will you like to do today?")
    #         print("""
    #             ***Main Menu***
    #             1.Open an Account 
    #             2.Login to your Account.
    #             3.Check Account Balance 
    #             4.Make a transfer 
    #             5.Buy Airtime.
    #             6.Buy Data
    #             7.Call Customer Service
    #             8.Exit 
    #             """)
    #         option = input("Please select an option>>>:")
    #         if option == "1":
    #             bank.customer_signup()
    #         elif option == "2":
    #             bank.login()
    #         # elif option == "3":
    #         #     bank.accountbal()
    #         # elif option == "4":
    #         #     bank.transfer()
    #         # elif option == "5":
    #         #     bank.airtime()
    #         # elif option == "6":
    #         #     bank.data()
    #         # elif option == "7":
    #         #     bank.service()
    #         elif option == "8":
    #             quit()
    #     else:
    #         print("Invalid option.")
    #         quit()
            
    def customer(self):
        print(f'Welcome to Guaranteed Trust Bank,Please sign up to enjoy our services')
        self.firstname = input('Enter your Firstname>>>:')
        self.surname = input('Enter your Surname>>>:')
        self.email = input('Enter your email>>>:')
        if(re.fullmatch(press, self.email)):
            print('Email Valid')
        else:
            print("Please Enter a valid Email")
            quit()
        self.password = input('Password>>:')
        self.con_password = input('Confirm Password')
        if self.con_password != self.password:
            print('Password not the same')
            quit()
        else:
            print('Password Verified!')
        self.phone = input("Enter your phone number")
        self.username = input('Enter your username>>>:')
        self.pin = int(input('Enter your pin>>>:'))
        self.confirm_pin = int(input('Confirm your Pin'))
        if self.pin == self.confirm_pin:
            print(f'Welcome {self.firstname}!\n Enjoy Banking with us!')
        else:
            print('Pin not Verified!')
            quit()
        self.new_balance = 0
        self.account_number = random.randrange(11111111111, 33333333333)
        bank_customer = 'INSERT into gtbank (Account_number, Firstname, Surname, Email, Password, Phone, Username, Pin, new_balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        details = (self.account_number, self.firstname, self.surname, self.email, self.password, self.phone, self.username, self.pin, 0)
        manage.execute(bank_customer, details)
        connect.commit()
        print(manage.rowcount, 'record(s) inserted successfully')
        print(f'Welcome {self.firstname}!')
        print(f'Your Account Number is {self.account_number}!\n Enjoy Banking with us!')
        # bank.login()

    
    # def login(self):

    #     print(f'Enter your Username and Password as Login Details')
    #     self.username = input("Enter your username>>>:")
    #     self.password = input("Enter your password>>>:")
    #     bank_customer = 'SELECT * FROM accessbank WHERE Username=%s AND Password=%s'
    #     details = (self.username, self.password)
    #     manage.execute(bank_customer, details)
    #     report = manage.fetchone()
    #     # print(report)
    #     print(f'Welcome {self.username},What will you like to do today?')
    #     print("1.Deposit 2.Make a Transfer 3.Make a Withdrawal 4.Check Balance 5.Exit")
    #     choice = input("Enter an option to proceed")
    #     if choice == '1':
    #         bank.Deposit()
    #     elif choice == '2':
    #         bank.transfer()
    #     elif choice == '3':
    #         bank.Withdrawal()
    #     elif choice == '4':
    #         bank.Balance()
    #     elif choice == '5':
    #         quit()
    #     else:
    #         print("Invalid Option")
    #         quit()

    # def bundle(self):
    #     print("Buy Bundles and Airtime")
    #     print("1.Buy Data 2.Buy Airtime")
    #     choice = input("Enter an option to proceed>>>>:")
    #     if choice == '1':
    #         print("""
    #             1.1GB @ 500
    #             2.3GB @ 1000
    #             3.10GB @ 2500

    #             """)
    #         option = input("Enter an option to buy Data>>>>:")
    #         if option == '1':
    #             bank.debit()
    #         elif option == '2':
    #             bank.debit()
    #         elif option == '3':
    #             bank.debit()
    #         else:
    #             print("Invalid option")
    #             print("Thank you for Banking with Us!","Go back to the Main Menu")
    #         quit()
    #     elif choice == '2':
    #         print("""
    #             1.500 Naira
    #             2.1000 Naira
    #             3.2000 Naira
    #             4.5000 Naira

    #             """)
    #         option = input("Enter an option to Buy Airtime>>>>:")
    #         if option == '1':
    #             bank.debit()
    #         elif option == '2':
    #             bank.debit()
    #         elif option == '3':
    #             bank.debit()
    #         elif option == '4':
    #             bank.debit()
    #         else:
    #             print("Invalid option")
    #             print("Thank you for Banking with Us!","Go back to the Main Menu")
    #         quit()




    # def transfer(self):
    #     self.pin = int(input("Enter Pin>>>>:"))
    #     data = "SELECT * FROM accessbank WHERE pin=%s"
    #     val =(self.pin,)
    #     manage.execute(data, val)
    #     report = manage.fetchone()
    #     print(report)
    #     if self.pin == report[-2]:
    #         transfer_amt = float(input("Enter Amount to Transfer>>>>:"))
    #         transfer_chgs = 57.25
    #         total_transfer_amount = transfer_amt + transfer_chgs
    #         self.Account_Balance = float(report[-1])
    #         print(self.Account_Balance)
    #         if total_transfer_amount <= self.Account_Balance:
    #             print(f'1.Transfer to Access Bank Account\n2. Transfer to Other Banks.')
    #             choice = int(input("Enter an option"))
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
    #                     self.Account_Balance -= total_transfer_amount
    #                     self.newbalance = self.accessbal + transfer_amt
    #                     data = "UPDATE accessbank SET balance=%s WHERE Pin=%s"
    #                     data1 = "UPDATE accessbank SET balance=%s WHERE Account_Number=%s"
    #                     val1 = (self.balance, self.pin)
    #                     val2 = (self.newbalance,benef)
    #                     manage.execute(data, val1)
    #                     manage.execute(data1, val2)
    #                     connect.commit()
    #                     print(connect.rowcount, 'record updated successfully')
    #                 else:
    #                     print(f'Incorrect Pin!\nTry again.')

# DEPOSIT MENU(CONFIRMED)
    # def Deposit(self):
    #     print("1.Make a Deposit")
    #     self.pin = input("Enter Pin>>>>:")
    #     report = "SELECT * FROM accessbank WHERE Pin=%s"
    #     details = (self.pin,)
    #     manage.execute(report, details)
    #     report = manage.fetchone()
    #     accessbal = int(report[9])
    #     print(accessbal)
    #     choice = input("Please Enter 1 to Make a Deposit>>>>:")
    #     if choice == '1':
    #         self.Account_Number = input("Enter Account Number")
    #         amount = int(input("Enter the amount to deposit>>>:"))
    #         self.new_balance = accessbal + amount
    #     payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
    #     details = (self.new_balance, self.pin)
    #     manage.execute(payment, details)
    #     connect.commit()
    #     print(f'Your Deposit is Successful')
    #     print(f'Thank you for Banking with us!')
    #     quit()

# WITHDRAWAL MENU(CONFIRMED)

    # def Withdrawal(self):

    #     print("2.Make a Withdrawal 3.Go back to the Main Menu")
    #     self.pin = input("Enter Pin>>>>:")
    #     report = "SELECT * FROM accessbank WHERE Pin=%s"
    #     details = (self.pin,)
    #     manage.execute(report, details)
    #     report = manage.fetchone()
    #     accessbalance = int(report[9])
    #     print(accessbalance)
    #     choice = input("Please Enter 2 to Make a Withdrawal>>>>:")
    #     if choice == '2':
    #         self.Account_Number = input("Enter Account Number")
    #         amount = int(input("Enter the amount to Withdraw>>>:"))
    #         self.new_balance = accessbalance - amount
    #     payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
    #     details = (self.new_balance, self.pin)
    #     manage.execute(payment, details)
    #     connect.commit()
    #     print(f'Your Withdrawal is Successful')
    #     print(f'Withdrawal Confirmation Receipt Printed')
    #     quit()

    # def Balance(self):
    #     self.pin = input("Enter Pin>>>>:")
    #     report = "SELECT * FROM accessbank WHERE Pin=%s"
    #     details = (self.pin,)
    #     manage.execute(report, details)
    #     report = manage.fetchone()
    #     accessbal = int(report[9])
    #     print(accessbal)
    #     print(f'Your account balance is', accessbal)


    # def debit(self):
    #     self.pin = input("Enter Pin>>>>:")
    #     report = "SELECT * FROM accessbank WHERE Pin=%s"
    #     details = (self.pin,)
    #     manage.execute(report, details)
    #     report = manage.fetchone()
    #     accessbalance = int(report[9])
    #     print(accessbalance)
    #     self.Account_Number = input("Enter Account Number")
    #     data_amount = int(input("Enter the amount >>>:"))
    #     self.new_balance = accessbalance - data_amount
    #     payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
    #     details = (self.new_balance, self.pin)
    #     manage.execute(payment, details)
    #     connect.commit()
    #     print(f'Your Bundle has been successfully purchased!')
    #     quit()

bankme = Money()
bankme.customer()
        





































# def bundle():
#     print("Buy Bundles and Airtime")
#     print("1.Buy Data 2.Buy Airtime")
#     if choice = '1':
#         print("""
#                 1.1GB @ 500
#                 2.3GB @1000
#                 3.10GB @2500

#                 """)
#         option = input("Enter an option to buy Data")
#         if option = '1':
#             self.pin = input("Enter Pin>>>>:")
#             report = "SELECT * FROM accessbank WHERE Pin=%s"
#             details = (self.pin,)
#             manage.execute(report, details)
#             report = manage.fetchone()
#             accessbalance = int(report[9])
#             print(accessbalance)
#             self.Account_Number = input("Enter Account Number")
#             amount = int(input("Enter the amount to Withdraw>>>:"))
#             self.new_balance = accessbalance - amount
#         payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
#         details = (self.new_balance, self.pin)
#         manage.execute(payment, details)
#         connect.commit()



# # def debit(self):
# #     self.pin = input("Enter Pin>>>>:")
# #             report = "SELECT * FROM accessbank WHERE Pin=%s"
# #             details = (self.pin,)
# #             manage.execute(report, details)
# #             report = manage.fetchone()
# #             accessbalance = int(report[9])
# #             print(accessbalance)
# #             self.Account_Number = input("Enter Account Number")
# #             data_amount = int(input("Enter the data amount >>>:"))
# #             self.new_balance = accessbalance - data_amount
# #         payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
# #         details = (self.new_balance, self.pin)
# #         manage.execute(payment, details)
# #         connect.commit()
# #         print(f'Your data has been successfully purchased!')

        



    




# def home():
#     print(f'Welcome to MultiBanks System Solutions')
#     print(f'Please select your choice of bank from the options below')
#     print("1.Access Bank 2.Polaris Bank 3.GT Bank 4.Exit")
#     choice = input("Please select an option>>>>:")
#     if choice = '1':
#         bank.menu()
#     elif choice = '2':




# print("Welcome to Embryo Bank")
# while True:
#     print("1.Create Account 2.Deposit Money 3.Withdraw Money 4.View Account Details 5.Exit")
#     ch = input("Please select an option>>>>:")
#     if ch == '1':
#         name = input("Enter your names")
#         city = input("Enter your city")
#         mobile_no = input("Enter your mobile number")
#         balance = 0
#         sql = "insert into bankpool(name,city,mobile_no,balance) values (%s,%s,%s,%s)"
#         val = (name, city, mobile_no, balance)
#         mycursor.execute(sql, val)
#         mycursor.execute("select * from bankpool where name='" + name + "'")
#         print("Account is successfully created")
#         for i in mycursor:
#             print(i)
        
#     elif ch == '2':
#         accno = input("Enter account number")
#         dp = int(input("Enter amount to be deposited"))
#         ttype = "d"
#         mycursor.execute = ("insert into transactions values ('" + accno + "', '" + str(dp) + "', '" + ttype + "')")
#         mycursor.execute = ("update bankpool set balance=balance+'" + str(dp) + "' where acc_no='" + accno + "'") 
#             # print("Rs.", dp, has been deposited successsfully in account no: ", accno)
#         #Withdraw Money
#     elif ch == '3':
#         accno = input(":Enter account number:")
#         wd = input("Enter amount to be withdrawn:")
#         select_query = "select balance from bankpool where acc_no = '" + accno + "' "
#         mycursor.execute(select_query)
#         bal = mycursor.fetchone()[0]
#         if wd < bal:
#             ttype = "w"
#             mycursor.execute("insert into transactions values ('" + accno + "', '" + str(dp) + "', '" + ttype + "')")
#             mycursor.execute = ("update bankpool set balance=balance+'" + str(wd) + "' where acc_no='" + accno + "'") 
#                 # print(f"Rs. " wd, has been withdrawn successsfully from account no: ", accno")
#         else:
#             print("Can't withdraw money.Insufficient balance!")

#         #Display Account Details
#     elif ch == '4':
#         accno = input("Enter account number")
#         mycursor.execute("Select * from bankpool where acc_no='" + accno + "'")
#         for i in mycursor:
#                 print(i)
#     else:
#         quit()




# PAST CODE WRITTEN WHILE DOING THE BANKING APP(*****MUST NOT DELETE)

    # DEPOSIT MENU
    # def Deposit(self):
    #     print("2.Make a Deposit")
    #     # payment = deposit
    #     choice = input("Please Enter 2 to Make a Deposit>>>>:")
    #     if choice == '2':
    #         self.Account_Number = input("Enter Account Number")
    #         self.amount = int(input("Enter the amount to deposit>>>:"))
    #     payment = "INSERT into accessbank (Account_Balance,Account_Number) VALUES (%s,%s)"
    #     payment = "UPDATE accessbank SET Account_Balance=%s WHERE Account_Number=%s"
    #     details = (self.amount, self.Account_Number)
    #     manage.execute(payment, details)
    #     connect.commit()
    #     print(f'Your Deposit is Successful')
# def airtime(self):
# def data(self):
# def service(self):
# TO CHECK ACCOUNT BALANCE
    # def accountbal(self):
    #     print("1.Check Account Balance")
    #     choice = input("Please Enter 1 to check your Account Balance>>>>:")
    #     if choice == '1':
    #         self.Account_number = input("Enter your account number>>>>:")
    #         self.phone = input("Enter your Phone number")
    #     bank_customer = 'SELECT Firstname, Account_Balance FROM maindata WHERE Account_number=%s AND phone=%s'
    #     details = (self.Account_number, self.phone)
    #     manage.execute(bank_customer, details)
    #     report = manage.fetchall()
    #     print('report')
    #     for i in report:
    #         print(i)
    #     connect.commit()
    #     print(f'Your Account Balance is', report)

# bank.menu()
# bank.customer_signup()
# bank.login()
# bank.airtime()
# bank.data()
# bank.service()
# bank.accountbal()
# bank.payment()
# bank.Deposit()

# DEPOSIT MENU
    # def Deposit(self):
        
    #     print("2.Make a Deposit")
    #     # payment = deposit
    #     choice = input("Please Enter 2 to Make a Deposit>>>>:")
    #     if choice == '2':
    #         self.Account_Number = input("Enter Account Number")
    #         self.amount = int(input("Enter the amount to deposit>>>:"))
    #     payment = "INSERT into accessbank (,Account_Number) VALUES (%s,%s)"
    #     payment = "UPDATE accessbank SET new_balance=%s WHERE Account_Number=%s"
    #     details = (self.amount, self.Account_Number)
    #     manage.execute(payment, details)
    #     connect.commit()
    #     print(f'Your Deposit is Successful')

    



# DEPOSIT FUNCT
    # def payment(self):
    #     print("2.Make a Deposit")
    #     choice = input("Please Enter 2 to Make a Deposit>>>>:")
    #     if choice == '2':
    #         self.account_number = input("Enter Account Number to Deposit")
    #         self.deposit = input("Enter the amount to deposit>>>:")
    #     bank_customer = "UPDATE maindata SET Account_balance=%s WHERE Account_Number=%s AND deposit=%s"
    #     details = (self.account_number, self.deposit)
    #     manage.execute(bank_customer, details)
    #     connect.commit()
    #     print('Deposit Successful')










    # def Balance(self):
    #     print("1.Check Account Balance")
    #     choice = input("Please Enter 1 to check your Account Balance>>>>:")
    #     if choice == '1':
    #         self.Account_number = input("Enter your account number>>>>:")
    #         self.pin = input("Enter your pin>>>>:")
    #     bank_customer = 'SELECT new_balance FROM accessbank WHERE account_number=%s AND Pin=%s'
    #     details = (self.Account_number, self.pin)
    #     manage.execute(bank_customer, details)
    #     report = manage.fetchone()
    #     print(report)
    #     if self.pin == report[-3]:
    #         print(f'Your account balance is {self.new_balance}')


# DEPOSIT THAT GOES INTO ACCOUNT BALANCE
        # if payment == 'deposit'
        # account_balance = self.deposit
        # print("Account_balance")
        # print(manage.rowcount, 'account updated successfully')





    # def Deposit(self):
    #     print("2.Make a Deposit")
    #     # payment = deposit
    #     choice = input("Please Enter 2 to Make a Deposit>>>>:")
    #     if choice == '2':
    #         self.account_number = input("Enter Account Number to Deposit")
    #         self.deposit = input("Enter the amount to deposit>>>:")
    #     bank_customer = "UPDATE maindata SET Account_Balance=%s WHERE pin=%s"
    #     details = (self.deposit, self.pin)
    #     manage.execute(bank_customer, details)
    #     connect.commit()
       
       
       
       # WITHDRAWAL MENU
    # def withdrawal(self):
    #     print("3.Make a Withdrawal")
    # choice = input("Please Enter 3 to Make a Withdrawal>>>>:")
    # if choice == '3':
    #     self.Account_Number = input("Enter Account Number>>>>:")
    #     withdraw = int(input("Enter amount to withdraw>>>:"))
    #     query = "select Account_Balance from maindata where Account_Number=%s"
    #     manage.execute(query)
    #     balance = manage.fetchone()[11]
    #     if withdraw < balance:
       
    #    def Withdrawal(self):
        
    #     print(f"Make a Withdrawal")
    #     self.pin = input("Enter Pin>>>>:")
    #     report = "SELECT * FROM accessbank WHERE Pin=%s"
    #     details = (self.pin,)
    #     manage.execute(report, details)
    #     report = manage.fetchone()
    #     accessbalance = int(report[-1])
    #     print(accessbalance)
    #     if self.pin == report[-1]:
    #         withdrawal_amt = int(input("Enter Amount to Withdraw"))
    #         self.new_balance = accessbalance - withdrawal_amt
    #         payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
    #         details = (self.new_balance, self.pin)
    #         manage.execute(payment, details)
    #         connect.commit()
    #         print(f'You have Withdrawn',{withdrawal_amt} 'from your Account!')


        
        
        
        
        # accessbal = int(report[-2])
        # print(accessbal)
        # choice = input("Please Enter 2 to Make a Deposit>>>>:")
        # if choice == '2':
        #     self.Account_Number = input("Enter Account Number")
        #     amount = int(input("Enter the amount to deposit>>>:"))
        #     self.new_balance = accessbal + amount
        # # payment = "INSERT into accessbank (,Account_Number) VALUES (%s,%s)"
        # payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
        # details = (self.new_balance, self.pin)
        # manage.execute(payment, details)
        # connect.commit()
        # print(f'Your Deposit is Successful')
       
       
       
       # print("1.Make a Withdrawal")
        # self.Account_Number = input("Enter Account_Number>>>>:")
        # report = "SELECT * FROM accessbank WHERE Account_Number=%s"
        # details = (self.Account_Number,)
        # manage.execute(report, details)
        # report = manage.fetchone()
        # accessbalance = int(report[9])
        # print(accessbalance)
        # choice = input("Please Enter 1 to make a Withdrawal>>>>:")
        # amount = input("Enter Amount to Withdraw")
        # self.new_balance = accessbalance - amount
        # self.pin = int(input("Enter pin>>>>:")
        # # print(self.pin)
        # if self.pin == report[7]:
        #     print(report)
        #     payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
        #     details = (self.new_balance, self.pin)
        #     manage.execute(payment, details)
        #     connect.commit()
        #     print(f'Your Withdrawal is Successful!')
       
       
       
       
       # if payment == 'deposit'
        # account_balance = self.deposit
        # print("Account_balance")
        # print(manage.rowcount, 'account updated successfully')
# deposit = self.deposit
# old_balance = Account_balance
# total_amount = (deposit + old_balance)
# print(f'total_amount')



# sql = "UPDATE freshbank SET Amount = '12000000' WHERE Pin=%s"
# val =('3300',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record updated successfuly')

#         sql = "UPDATE freshbank SET Amount = '12000000' WHERE Pin=%s"

#         print("2.Make a Deposit")
#         print("3.Make a Transfer")
#         print("4.Buy Data")
#         print("5.Buy Airtime")
#         print("6.Call Customer Service")

# # CREATE TABLE
# # manage.execute("CREATE TABLE newbankme (Account_Number INT(10), Firstname VARCHAR(30), Surname VARCHAR(30), Email VARCHAR(50), Password VARCHAR(30), Phone INT(11) NOT NULL, Username VARCHAR(8),Pin INT(4) UNIQUE, Deposit INT(50), Withdrawal INT(50), Account_Balance INT(50))")
# # manage.execute("SHOW TABLES")
# # for table in manage:
# #     print(table)



# # CREATE TABLE
# # manage.execute("CREATE TABLE newbank ( Account_Number(10), Firstname VARCHAR(30), Surname VARCHAR(30), Email VARCHAR(50), Password VARCHAR(30), Phone INT(11), Username VARCHAR(8), Pin INT(4), Deposit INT(50), Withdrawal INT(50), Account_Balance INT(50))")
# # manage.execute("SHOW TABLES")
# # for table in manage:
# #     print(table)
# # class Banking:
    
# #     def __init__(self):
# #         self.bk = 'bk'

# #     def customer_signup(self):
# #         print(f'Welcome to Access Bank,Please sign up to enjoy our services')
# #         self.firstname = input('Enter your Firstname>>>:')
# #         self.surname = input('Enter your Surname>>>:')
# #         self.email = input('Enter your email>>>:')
# #         if(re.fullmatch(press, self.email)):
# #             print('Email Valid')
# #         else:
# #             print("Please Enter a valid Email")
# #             quit()
# #         self.password = input('Password>>:')
# #         self.con_password = input('Confirm Password')
# #         if self.con_password != self.password:
# #             print('Password not the same')
# #             quit()
# #         else:
# #             print('Password Verified!')
# #         self.bvn = int(input('Enter your bvn>>>:'))
# #         if self.bvn >= 11:
# #             print(f'BVN VERIFIED {self.surname}!\n Proceed!')
# #         else:
# #             print('Invalid BVN')
# #             quit()
# #         self.username = input('Enter your username>>>:')
# #         self.pin = int(input('Enter your pin>>>:'))
# #         self.confirm_pin = int(input('Confirm your Pin'))
# #         if self.pin == self.confirm_pin:
# #             print(f'Welcome {self.firstname}!\n Enjoy Banking with us!')
# #         else:
# #             print('Pin not Verified!')
# #             quit()

# #         bank_customer = 'INSERT into passyear (Account_number, Firstname, Surname, Email, Password, bvn, Username, Pin, Deposit, Withdrawal, Account_Balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# #         details = (0,self.firstname, self.surname, self.email, self.password, self.bvn, self.username, self.pin,0, 0, 0)
# #         manage.execute(bank_customer, details)
# #         connect.commit()
# #         print(manage.rowcount, 'record(s) inserted successfully')
# #         print(f'Welcome {self.firstname}!')
# #         # print(f'Your Account Number is {}!\n Enjoy Banking with us!')





def Withdrawal(self):
        print("2.Make a Withdrawal 3.Go back to the Main Menu")
        self.password= input("Enter Password>>>>:")
        report = "SELECT balance FROM accessbank WHERE Password=%s"
        details = (self.password,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        self.total_balance = (report[-3])
        print(self.total_balance)
        choice = input("Please Enter 1 to Make a Withdrawal>>>>:")
        if choice == '1':
            self.Account_Number = input("Enter Account Number")
            self.flow = int(input("Enter the amount to Withdraw>>>:"))
            self.balance = self.total_balance - self.flow
            # self.balance = 
        # payment2 = "UPDATE accessbank SET balance=%s WHERE Account_Number=%s"
        payment1 = "UPDATE accessbank SET flow=%s WHERE Account_Number=%s"
        payment = "UPDATE accessbank SET balance=%s WHERE Pin=%s"
        details = (self.balance, self.pin)
        details1 = (self.flow, self.Account_Number)
        manage.execute(payment, details)
        manage.execute(payment1, details1)
        connect.commit()
        print(f'The Withdrawal of {self.flow} is Successful')
        print(f'Thank you for Banking with us!')
        quit()






        def Withdrawal(self):
        print("2.Make a Withdrawal 3.Go back to the Main Menu")
        self.password= input("Enter Password>>>>:")
        report = "SELECT balance FROM accessbank WHERE Password=%s"
        details = (self.password,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        self.total_balance = (report[-1])
        print(self.total_balance)
        choice = input("Please Enter 1 to Make a Withdrawal>>>>:")
        if choice == '1':
            self.Account_Number = input("Enter Account Number")
            self.inflow = int(input("Enter the amount to Withdraw>>>:"))
            self.balance = self.total_balance + self.inflow
            # self.balance = 
        # payment2 = "UPDATE accessbank SET balance=%s WHERE Account_Number=%s"
        payment1 = "UPDATE accessbank SET inflow=%s WHERE Account_Number=%s"
        payment = "UPDATE accessbank SET balance=%s WHERE Pin=%s"
        details = (self.balance, self.pin)
        details1 = (self.inflow, self.Account_Number)
        manage.execute(payment, details)
        manage.execute(payment1, details1)
        connect.commit()
        print(f'The Withdrawal of {self.flow} is Successful')
        print(f'Thank you for Banking with us!')
        quit()







# FRESH AND NEWLY DEPOSIT MENU( WITH TABLE AND SQL UPDATED)
    def Withdrawal(self):
        
        print("2.Make a Withdrawal 3.Go back to the Main Menu")
        self.password= input("Enter Password>>>>:")
        report = "SELECT total_balance FROM accessbank WHERE Password=%s"
        details = (self.password,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        self.balance = (report[-1])
        print(self.balance)
        choice = input("Please Enter 1 to Make a Withdrawal>>>>:")
        if choice == '1':
            self.Account_Number = input("Enter Account Number")
            self.outflow = int(input("Enter the amount to Deposit>>>:"))
            self.total_balance = (self.balace - self.outflow)
            payment2 = "UPDATE accessbank SET balance=%s WHERE outflow=%s"
            details2 = (self.balance, self.outflow)
            payment = "UPDATE accessbank SET outflow=%s WHERE Account_Number=%s"
            payment1 = "UPDATE accessbank SET total_balance=%s WHERE Account_Number=%s"
            details = (self.outflow, self.Account_Number)
            details1 = (self.total_balance, self.Account_Number)
            manage.execute(payment, details)
            manage.execute(payment1, details1)
            manage.execute(payment2, details2)
            connect.commit()
            print(f'The Deposit of {self.inflow} is Successful')
            print(f'Thank you for Banking with us!')
            quit()


    def transfer(self):
        # self.balance = GO AND FETCH
        # print("2.Make a Withdrawal 3.Go back to the Main Menu")
        self.password= input("Enter Password>>>>:")
        report = "SELECT total_balance FROM accessbank WHERE Password=%s"
        details = (self.password,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        self.balance = (report[-1])
        print(self.balance)
        print(f'1.Transfer to Access Bank Account\n2. Transfer to GT Banks.')
        choice = input("Enter an option>>>>:")
        if choice == '1':
            beneficiary = input("Enter Beneficiary Account Number>>>>:")
            data = "SELECT Firstname, Surname FROM accessbank WHERE Account_Number=%s"
            val = (beneficiary,)
            manage.execute(data, val)
            report = manage.fetchone()
            # print(report)
            self.outflow = input("Enter amount to be transferred>>>>:")
            self.total_balance = (self.balance - self.outflow)
            payment2 = "UPDATE accessbank SET balance=%s WHERE outflow=%s"
            details2 = (self.balance, self.outflow)
            payment = "UPDATE accessbank SET inflow=%s WHERE Account_Number=%s"
            payment1 = "UPDATE accessbank SET total_balance=%s WHERE Account_Number=%s"
            details = (self.inflow, self.Account_Number)
            details1 = (self.total_balance, self.Account_Number)
            manage.execute(payment, details)
            manage.execute(payment1, details1)
            manage.execute(payment2, details2)
            connect.commit()
            print(f'The Deposit of {self.inflow} is Successful')
            print(f'Thank you for Banking with us!')
            quit()
            # beneficiary = input("Enter Beneficiary Account Number>>>>:")
            # data = "SELECT Firstname, Surname FROM accessbank WHERE Account_Number=%s"
            # val = (beneficiary,)
            # manage.execute(data, val)
            # report = manage.fetchone()
            # # print(report)
            # funds = input("Enter amount to be transferred>>>>:")
            # charges = 58
            # self.outflow = (tf + charges)
            # print(self.outflow)
            # self.balance = (self.balance - total_funds)
            # self.Pin = input("Enter Pin>>>>:")
            # self.total_balance = (self.balance + flow)
            # data1 = "UPDATE accessbank SET balance=%s WHERE Pin=%s"
            # data2 = "UPDATE accessbank SET total_balance=%s WHERE Account_Number=%s"
            # val1 = (self.balance, self.Pin)
            # val2 = (self.total_balance, benef)
            # manage.execute(data1, val1)
            # manage.execute(data2, val2)
            # connect.commit()




            
        # elif choice == '2':
        #     benef = input("Enter Beneficiary Account Number>>>>:")
        #     data = "SELECT Firstname, Surname FROM gtbank WHERE Account_Number=%s"
        #     val = (benef,)
        #     manage.execute(data, val)
        #     report = manage.fetchone()
        #     print(report)
        #     flow = int(input("Enter amount to be transferred>>>>:"))
        #     self.balance = (self.balance - flow)
        #     data1 = "UPDATE accessbank SET balance=%s WHERE Pin=%s"















        # FRESH AND NEWLY DEPOSIT MENU( WITH TABLE AND SQL UPDATED)FOR PROJECT
    # def Deposit(self):

    #     print("1.Make a Deposit")
    #     self.password= input("Enter Password>>>>:")
    #     report = "SELECT total_balance FROM accessbank WHERE Password=%s"
    #     details = (self.password,)
    #     manage.execute(report, details)
    #     report = manage.fetchone()
    #     print(report)
    #     self.balance = (report[-1])
    #     print(self.balance)
    #     choice = input("Please Enter 1 to Make a Deposir>>>>:")
    #     if choice == '1':
    #         self.Account_Number = input("Enter Account Number")
    #         self.inflow = int(input("Enter the amount to Deposit>>>:"))
    #         self.total_balance = (self.balance + self.inflow)
    #         payment2 = "UPDATE accessbank SET balance=%s WHERE inflow=%s"
    #         details2 = (self.balance, self.inflow)
    #         payment = "UPDATE accessbank SET inflow=%s WHERE Account_Number=%s"
    #         payment1 = "UPDATE accessbank SET total_balance=%s WHERE Account_Number=%s"
    #         details = (self.inflow, self.Account_Number)
    #         details1 = (self.total_balance, self.Account_Number)
    #         manage.execute(payment, details)
    #         manage.execute(payment1, details1)
    #         manage.execute(payment2, details2)
    #         connect.commit()
    #         print(f'The Deposit of {self.inflow} is Successful')
    #         print(f'Thank you for Banking with us!')
    #         quit()