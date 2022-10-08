from gtbbank import Money
from polaris import Pool
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
# manage.execute("ALTER TABLE accessbank add column total_balance INT (10) NOT NULL")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)

class Banking:
    
    def __init__(self):
        self.bk = 'bk'



    # print(f'Welcome to MultiBanks Solutions System Inc')
    # print(f'Please Choose a Bank of your Interest and Sign Up to Start Enjoying our Services')
    # print(f'1.AccessBank\n2. GT Bank\n3.Polaris Bank') 
    # option = input("Please Enter an option to proceed>>>>:")
    # if option == '1':
    #     print("Welcome to Access Bank!.What will you like to do today?")
    #     print(f'1.Open an Account')
    #     print(f'2.Login to your Account')
    #     print(f'3.Check Account Balance')
    #     option = input("Enter an option to proceed>>>:")
    #     if option == '1':
    #         bkk.customer_signup()
        # print("""
        #         ***Main Menu***
        #         1.Open an Account 
        #         2.Login to your Account.
        #         3.Check Account Balance 
        #         4.Make a transfer 
        #         5.Buy Airtime.
        #         6.Buy Data
        #         7.Call Customer Service
        #         8.Exit 
        #         """)
        # option = input("Please select an option>>>:")
        # if option == "1":
        #     bkk.customer_signup()
        # elif option == "2":
        #     bkk.login()
        # elif option == "3":
        #     bkk.Deposit()
        # elif option == "4":
        #     bkk.transfer()
        #     # elif option == "5":
        #     #     bank.airtime()
        #     # elif option == "6":
        #     #     bank.data()
        #     # elif option == "7":
        #     #     bank.service()
        #     # elif option == "8":
        #     #     quit()
        
        # elif choice == '2':
        #     print("Welcome to Polaris Bank!.What will you like to do today?")
        #     print("""
        #         ***Main Menu***
        #         1.Open an Account 
        #         2.Login to your Account.
        #         3.Check Account Balance 
        #         4.Make a transfer 
        #         5.Buy Airtime.
        #         6.Buy Data
        #         7.Call Customer Service
        #         8.Exit 
        #         """)
        #     option = input("Please select an option>>>:")
        #     if option == "1":
        #         bank.customer_signup()
        #     elif option == "2":
        #         bank.login()
        #     elif option == "3":
        #         bank.accountbal()
        #     elif option == "4":
        #         bank.transfer()
        #     elif option == "5":
        #         bank.airtime()
        #     elif option == "6":
        #         bank.data()
        #     elif option == "7":
        #         bank.service()
        #     elif option == "8":
        #         quit()

        # elif choice == '3':
        #     print("Welcome to GT Bank!.What will you like to do today?")
        #     print("""
        #         ***Main Menu***
        #         1.Open an Account 
        #         2.Login to your Account.
        #         3.Check Account Balance 
        #         4.Make a transfer 
        #         5.Buy Airtime.
        #         6.Buy Data
        #         7.Call Customer Service
        #         8.Exit 
        #         """)
        #     option = input("Please select an option>>>:")
        #     if option == "1":
        #         bank.customer_signup()
        #     elif option == "2":
        #         bank.login()
        #     # elif option == "3":
        #     #     bank.accountbal()
        #     # elif option == "4":
        #     #     bank.transfer()
        #     # elif option == "5":
        #     #     bank.airtime()
        #     # elif option == "6":
        #     #     bank.data()
        #     # elif option == "7":
        #     #     bank.service()
        #     elif option == "8":
        #         quit()
        # else:
        #     print("Invalid option.")
        #     quit()
            
    def customer_signup(self):
        print(f'Welcome to Access Bank,Please sign up to enjoy our services')
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
        self.inflow = 0
        self.outflow = 0
        self.total_balance = 0
        self.account_number = random.randrange(11111111111, 33333333333)
        bank_customer = 'INSERT into accessbank (Account_number, Firstname, Surname, Email, Password, Phone, Username, Pin, inflow, outflow, total_balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        details = (self.account_number, self.firstname, self.surname, self.email, self.password, self.phone, self.username, self.pin, self.inflow, self.outflow, self.total_balance)
        manage.execute(bank_customer, details)
        connect.commit()
        print(manage.rowcount, 'record(s) inserted successfully')
        print(f'Welcome {self.firstname}!')
        print(f'Your Account Number is {self.account_number}!\n Enjoy Banking with us!')
        bank.login()

    
    def login(self):

        print(f'Enter your Username and Password as Login Details')
        self.username = input("Enter your username>>>:")
        self.password = input("Enter your password>>>:")
        bank_customer = 'SELECT * FROM accessbank WHERE Username=%s AND Password=%s'
        details = (self.username, self.password)
        manage.execute(bank_customer, details)
        report = manage.fetchone()
        # print(report)
        print(f'Welcome {self.username},What will you like to do today?')
        print("1.Deposit 2.Make a Transfer 3.Make a Withdrawal 4.Check Balance 5.Exit")
        choice = input("Enter an option to proceed")
        if choice == '1':
            bank.Deposit()
        elif choice == '2':
            bank.transfer()
        elif choice == '3':
            bank.Withdrawal()
        elif choice == '4':
            bank.Balance()
        elif choice == '5':
            quit()
        else:
            print("Invalid Option")
            quit()

    def bundle(self):
        print("Buy Bundles and Airtime")
        print("1.Buy Data 2.Buy Airtime")
        choice = input("Enter an option to proceed>>>>:")
        if choice == '1':
            print("""
                1.1GB @ 500
                2.3GB @ 1000
                3.10GB @ 2500

                """)
            option = input("Enter an option to buy Data>>>>:")
            if option == '1':
                bank.debit()
            elif option == '2':
                bank.debit()
            elif option == '3':
                bank.debit()
            else:
                print("Invalid option")
                print("Thank you for Banking with Us!","Go back to the Main Menu")
            quit()
        elif choice == '2':
            print("""
                1.500 Naira
                2.1000 Naira
                3.2000 Naira
                4.5000 Naira

                """)
            option = input("Enter an option to Buy Airtime>>>>:")
            if option == '1':
                bank.debit()
            elif option == '2':
                bank.debit()
            elif option == '3':
                bank.debit()
            elif option == '4':
                bank.debit()
            else:
                print("Invalid option")
                print("Thank you for Banking with Us!","Go back to the Main Menu")
            quit()


# FRESH AND NEWLY DEPOSIT MENU( WITH TABLE AND SQL UPDATED)
    def Deposit(self):

        print("Make a Deposit")
        choice = input("Please Enter 1 to Make a Deposit>>>>:")
        if choice == '1':
            self.Account_Number = input("Enter Account Number>>>:")
            self.pin = input("Enter Pin>>>>:")
            data6 = "SELECT total_balance FROM accessbank WHERE Account_Number=%s AND Pin=%s"
            val6 = (self.Account_Number, self.pin)
            manage.execute(data6, val6)
            report = manage.fetchone()
            balance = report[-1] 
            print(balance)
            amount = int(input("Enter the amount to be deposited>>>>:"))
            self.inflow = amount
            self.Account_Number = input("Confirm Benef account Number>>>:")
            balance = report[-1]
            self.total_balance = self.inflow + balance
            payment = "UPDATE accessbank SET inflow=%s WHERE Account_Number=%s"
            payment1 = "UPDATE accessbank SET total_balance=%s WHERE Account_Number=%s"
            # payment2 = "UPDATE gtbank SET total_balance=%s WHERE inflow=%s"
            details = (self.inflow, self.Account_Number)
            details1 = (self.total_balance, self.Account_Number)
            manage.execute(payment, details)
            manage.execute(payment1, details1)
            connect.commit()
            print(f'Your Deposit of {self.inflow} is Successful')
            print(f'Thank you for Banking with us!')
            quit()



# WITHDRAWAL THIRD MENU
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
            self.outflow = int(input("Enter the amount to Withdraw>>>:"))
            self.total_balance = (self.balance - self.outflow)
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
            print(f'The Withdrawal of {self.outflow} is Successful')
            print(f'Thank you for Banking with us!')
            quit()

# BALANCE MENU DONE FOR LATEST TABEL AND SQL
    def Balance(self):
        self.pin = input("Enter Pin>>>>:")
        report = "SELECT total_balance FROM accessbank WHERE Pin=%s"
        details = (self.pin,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        print(f'Your account balance is', report)

# DEBIT MENU FOR DATA AND AIRTIME FULLY UPDATED IN LATEST TABLE AND SQL
    def debit(self):
        self.password= input("Enter Password>>>>:")
        report = "SELECT total_balance FROM accessbank WHERE Password=%s"
        details = (self.password,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        self.balance = (report[-1])
        print(self.balance)
        # print("1.Make a Withdrawal 2.Go back to the Main Menu")
        # option = input("Enter an option to proceed>>>>:")
        # if option == '1':
        amount = int(input("Enter amount>>>>:"))
        charges = 5
        outflow = int(amount + charges)
        print(outflow)
        self.Pin = input("Enter Pin>>>>:")
        data = "UPDATE accessbank SET outflow=%s WHERE Pin=%s"
        val = (outflow, self.Pin)
        manage.execute(data, val)
        connect.commit()
        self.total_balance = (report[-1])
        self.total_balance = self.total_balance - outflow
        data1 = "UPDATE accessbank SET total_balance=%s WHERE Pin=%s"
        val1 = (self.total_balance, self.Pin,)
        manage.execute(data1, val1)
        connect.commit()
        print(f'Your Purchase is Successful!')
       
    def menu(self):
        print("Welcome to Access Bank!.What will you like to do today?")
        print(f'1.Open an Account')
        print(f'2.Login to your Account')
        print(f'3.Make a Deposit')
        print(f'4.Make a Transfer')
        print(f'5.Buy Bundles')
        print(f'6.Call Customer Service')
        print(f'7.Check Account Balance')
        print(f'8.Exit')


    def transfer(self):
        # self.balance = GO AND FETCH
        print("To Make a Transfer,Please Enter your Password")
        self.password= input("Enter Password>>>>:")
        report = "SELECT total_balance FROM accessbank WHERE Password=%s"
        details = (self.password,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        self.balance = (report[-1])
        print(self.balance)
        print(f'1.Transfer to Access Bank Account\n2. Transfer to GT Banks\n3. Transfer to Polaris Bank')
        choice = input("Enter an option>>>>:")
        if choice == '1':
            amount = int(input("Enter amount to be transferred>>>>:"))
            charges = 30
            outflow = int(amount + charges)
            print(outflow)
            self.Pin = input("Enter Pin>>>>:")
            data = "UPDATE accessbank SET outflow=%s WHERE Pin=%s"
            val = (outflow, self.Pin)
            manage.execute(data, val)
            connect.commit()
            self.total_balance = (report[-1])
            self.total_balance = self.total_balance - outflow
            data1 = "UPDATE accessbank SET total_balance=%s WHERE Pin=%s"
            val1 = (self.total_balance, self.Pin,)
            manage.execute(data1, val1)
            connect.commit()

            benef_acct = input("Enter Benef account Number>>>:")
            data = "SELECT Firstname, Surname FROM accessbank WHERE Account_Number=%s"
            val = (benef_acct,)
            manage.execute(data, val)
            report = manage.fetchone()
            print(report)
            # ***********************************************
            # benef_acct = input("Enter Benef account Number>>>:")
            data = "SELECT total_balance FROM accessbank WHERE Account_Number=%s"
            val = (benef_acct,)
            manage.execute(data, val)
            report = manage.fetchone()
            balance = report[-1]
            print(balance)
            
            self.inflow = amount
            amount = input("Confirm amount to be transferred")
            self.Account_Number = input("Confirm Benef account Number>>>:")
            balance = report[-1]
            self.total_balance = (self.inflow + balance)
            data4 = "UPDATE accessbank SET inflow=%s WHERE Account_Number=%s"
            data3 = "UPDATE accessbank SET total_balance=%s WHERE Account_Number=%s"
            val4 = (self.inflow, self.Account_Number)
            val3 = (self.total_balance, self.Account_Number)
            manage.execute(data4, val4)
            manage.execute(data3, val3)
            connect.commit()
            print(f'Your Transfer is Successful!')
           
        elif choice == '2':
            amount = int(input("Enter amount to be transferred>>>>:"))
            charges = 60
            outflow = int(amount + charges)
            print(outflow)
            self.Pin = input("Enter Pin>>>>:")
            data = "UPDATE accessbank SET outflow=%s WHERE Pin=%s"
            val = (outflow, self.Pin)
            manage.execute(data, val)
            connect.commit()
            self.total_balance = (report[-1])
            self.total_balance = self.total_balance - outflow
            data1 = "UPDATE accessbank SET total_balance=%s WHERE Pin=%s"
            val1 = (self.total_balance, self.Pin,)
            manage.execute(data1, val1)
            connect.commit()

            benef_acct = input("Enter Benef account Number>>>:")
            data = "SELECT Firstname, Surname FROM gtbank WHERE Account_Number=%s"
            val = (benef_acct,)
            manage.execute(data, val)
            report = manage.fetchone()
            print(report)
            # ***********************************************
            # benef_acct = input("Confirm Benef account Number>>>:")
            data = "SELECT total_balance FROM gtbank WHERE Account_Number=%s"
            val = (benef_acct,)
            manage.execute(data, val)
            report = manage.fetchone()
            balance = report[-1]
            print(balance)
            
            self.inflow = amount
            amount = input("Confirm amount to be transferred")
            self.Account_Number = input("Confirm Benef account Number>>>:")
            balance = report[-1]
            self.total_balance = (self.inflow + balance)
            data4 = "UPDATE gtbank SET inflow=%s WHERE Account_Number=%s"
            data3 = "UPDATE gtbank SET total_balance=%s WHERE Account_Number=%s"
            val4 = (self.inflow, self.Account_Number)
            val3 = (self.total_balance, self.Account_Number)
            manage.execute(data4, val4)
            manage.execute(data3, val3)
            connect.commit()
            print(f'Your Transfer is Successful!')

        elif choice == '3':
            amount = int(input("Enter amount to be transferred>>>>:"))
            charges = 60
            outflow = int(amount + charges)
            print(outflow)
            self.Pin = input("Enter Pin>>>>:")
            data = "UPDATE accessbank SET outflow=%s WHERE Pin=%s"
            val = (outflow, self.Pin)
            manage.execute(data, val)
            connect.commit()
            self.total_balance = (report[-1])
            self.total_balance = self.total_balance - outflow
            data1 = "UPDATE accessbank SET total_balance=%s WHERE Pin=%s"
            val1 = (self.total_balance, self.Pin,)
            manage.execute(data1, val1)
            connect.commit()

            benef_acct = input("Enter Benef account Number>>>:")
            data = "SELECT Firstname, Surname FROM polarisbank WHERE Account_Number=%s"
            val = (benef_acct,)
            manage.execute(data, val)
            report = manage.fetchone()
            print(report)
            # ***********************************************
            # benef_acct = input("Confirm Benef account Number>>>:")
            data = "SELECT total_balance FROM polarisbank WHERE Account_Number=%s"
            val = (benef_acct,)
            manage.execute(data, val)
            report = manage.fetchone()
            balance = report[-1]
            print(balance)
            
            self.inflow = amount
            amount = input("Confirm amount to be transferred")
            self.Account_Number = input("Confirm Benef account Number>>>:")
            balance = report[-1]
            self.total_balance = (self.inflow + balance)
            data4 = "UPDATE polarisbank SET inflow=%s WHERE Account_Number=%s"
            data3 = "UPDATE polarisbank SET total_balance=%s WHERE Account_Number=%s"
            val4 = (self.inflow, self.Account_Number)
            val3 = (self.total_balance, self.Account_Number)
            manage.execute(data4, val4)
            manage.execute(data3, val3)
            connect.commit()
            print(f'Your Transfer is Successful!')
        else:
            print("Invalid Option!")
            quit()
        

            

bank = Banking()
bankme = Money()
bankus = Pool()


print(f'Welcome to MultiBanks Solutions System Inc')
print(f'Please Choose a Bank of your Interest and Sign Up to Start Enjoying our Services')
print(f'1.AccessBank\n2.GT Bank\n3.Polaris Bank') 
option = input("Please Enter an option to proceed>>>>:")
if option == '1':
    bank.menu()
    option = input("Enter an option to proceed>>>:")
    if option == '1':
        bank.customer_signup()
    elif option == "2":
        bank.login()
    elif option == "3":
        bank.Deposit()
    elif option == "4":
        bank.transfer()
    elif option == "5":
        bank.bundle()
    elif option == "6":
        bank.service()
    elif option == "7":
        bank.Balance()
    elif option == "8":
        quit()
elif option == '2':
    bankme.menu()
    option = input("Enter an option to proceed>>>:")
    if option == '1':
        bankme.customer()
    elif option == "2":
        bankme.login()
    elif option == "3":
        bankme.Deposit()
    elif option == "4":
        bankme.transfer()
    elif option == "5":
        bankme.bundle()
    elif option == "6":
        bankme.service()
    elif option == "7":
        bankme.Balance()
    elif option == "8":
        quit()
    
elif option == '3':
    bankus.menu()

else:
    print(f'Invalid Option')
    quit()





# else:
#     print(f'Invalid Option')
#     quit()

        




























            
            
            
            










 # data = "SELECT Firstname, Surname FROM accessbank WHERE Account_Number=%s"
            # val = (beneficiary,)
            # manage.execute(data, val)
            # report = manage.fetchone()
            # # print(report)
            # self.outflow = int(input("Enter amount to be transferred>>>>:"))
            # self.total_balance = (self.balance - self.outflow)
            # self.bal = (self.outflow + self.total_balance)
            # payment2 = "UPDATE accessbank SET balance=%s WHERE outflow=%s"
            # details2 = (self.balance, self.outflow)
            # payment = "UPDATE accessbank SET inflow=%s WHERE Account_Number=%s"
            # payment1 = "UPDATE accessbank SET total_balance=%s WHERE Account_Number=%s"
            # details = (self.inflow, self.Account_Number)
            # details1 = (self.total_balance, self.Account_Number)
            # manage.execute(payment, details)
            # manage.execute(payment1, details1)
            # manage.execute(payment2, details2)
            # connect.commit()
            # print(f'The Deposit of {self.inflow} is Successful')
            # print(f'Thank you for Banking with us!')
            # quit()
            # if self.inflow == amount:
            #     data2 = "UPDATE gtbank SET inflow=%s WHERE Pin=%s"
            #     val2 = (self.inflow, self.Pin)
            #     manage.execute(data2, val2)
            #     connect.commit()
                
                

            # benef = input("Enter Beneficiary Account Number>>>>:")
            # data = "SELECT Firstname, Surname FROM gtbank WHERE Account_Number=%s"
            # val = (benef,)
            # manage.execute(data, val)
            # report = manage.fetchone()
            # print(report)
            # self.outflow = int(input("Enter amount to be transferred>>>>:"))
            # self.balance = (self.balance - self.outflow)
            # payment = "UPDATE gtbank SET balance=%s WHERE Pin=%s"
            # details = (self.balance, self.outflow)
            # manage.execute(payment, details)


# benef_acct = input("Enter Benef account Number>>>:")
            # data = "SELECT total_balance FROM gtbank WHERE Account_Number=%s"
            # val = (benef_acct,)
            # manage.execute(data, val)
            # report = manage.fetchone()[-1]
            # print(report)



# WITHDRAWAL #SECOND MENU
#USE THIS MENU FOR WITHDRAWAL
    # def Withdrawal(self):
    #     print("2.Make a Withdrawal 3.Go back to the Main Menu")
    #     self.password= input("Enter Pin>>>>:")
    #     report = "SELECT * FROM accessbank WHERE Pin=%s"
    #     details = (self.pin,)
    #     manage.execute(report, details)
    #     report = manage.fetchone()
    #     print(report)
    #     self.total_balance = (report[-3])
    #     print(self.total_balance)
    #     choice = input("Please Enter 1 to Make a Withdrawal>>>>:")
    #     if choice == '1':
    #         self.Account_Number = input("Enter Account Number")
    #         self.flow = int(input("Enter the amount to Withdraw>>>:"))
    #         self.balance = self.total_balance - self.flow
    #         # self.balance = 
    #     # payment2 = "UPDATE accessbank SET balance=%s WHERE Account_Number=%s"
    #     payment1 = "UPDATE accessbank SET flow=%s WHERE Account_Number=%s"
    #     payment = "UPDATE accessbank SET balance=%s WHERE Pin=%s"
    #     details = (self.balance, self.pin)
    #     details1 = (self.flow, self.Account_Number)
    #     manage.execute(payment, details)
    #     manage.execute(payment1, details1)
    #     connect.commit()
    #     print(f'The Withdrawal of {self.flow} is Successful')
    #     print(f'Thank you for Banking with us!')
    #     quit()

#  FIRST MENU
        # print("2.Make a Withdrawal 3.Go back to the Main Menu")
        # self.pin = input("Enter Pin>>>>:")
        # report = "SELECT * FROM accessbank WHERE Pin=%s"
        # details = (self.pin,)
        # manage.execute(report, details)
        # report = manage.fetchone()
        # accessbalance = int(report[9])
        # print(accessbalance)
        # choice = input("Please Enter 2 to Make a Withdrawal>>>>:")
        # if choice == '2':
        #     self.Account_Number = input("Enter Account Number")
        #     amount = int(input("Enter the amount to Withdraw>>>:"))
        #     self.new_balance = accessbalance - amount
        # payment = "UPDATE accessbank SET new_balance=%s WHERE Pin=%s"
        # details = (self.new_balance, self.pin)
        # manage.execute(payment, details)
        # connect.commit()
        # print(f'Your Withdrawal is Successful')
        # print(f'Withdrawal Confirmation Receipt Printed')
        # quit()

    # SECOND MENU
    

     # # self.pin = input("Enter Pin>>>>:")
        # # report = "SELECT total_balance FROM accessbank WHERE Pin=%s"
        # # details = (self.Pin,)
        # # manage.execute(report, details)
        # # report = manage.fetchone()
        # # print(f'Your Available Balance is', report)
        # self.pin = input("Enter Pin>>>>:")
        # report = "SELECT total_balance FROM accessbank WHERE Pin=%s"
        # details = (self.pin,)
        # manage.execute(report, details)
        # report = manage.fetchone()
        # print(report)
        # print(f'Your account balance is', report)
        # self.Account_Number = input("Enter Account Number")
        # self.outflow = int(input("Enter the amount >>>:"))
        # self.balance = (self.total_balance - self.outflow)
        
        # details = (self.outflow, self.Account_Number)
        # details2 = (self.balance, self.outflow)
        # payment = "UPDATE accessbank SET outflow=%s WHERE Account_Number=%s"
        # payment2 = "UPDATE accessbank SET clsbalance=%s WHERE outflow=%s"
        # manage.execute(payment, details)
        # manage.execute(payment2, details2)
        # connect.commit()
        # print(f'Your Bundle has been successfully purchased!')
        # quit()







