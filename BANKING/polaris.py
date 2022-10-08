import mysql.connector
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Multibanks')
manage = connect.cursor()
import random
import re
press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# CREATE TABLE
# manage.execute("CREATE TABLE polarisbank (Account_Number VARCHAR(10), Firstname VARCHAR(30), Surname VARCHAR(30), Email VARCHAR(50), Password VARCHAR(30), Phone VARCHAR(11), Username VARCHAR(8),Pin INT(4), inflow INT(20), outflow INT(20), balance INT(20), total_balance INT(20))")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)


class Pool:
    
    def __init__(self):
        self.bk = 'bk'



    def menu(self):
        print("Welcome to Polaris Bank!.What will you like to do today?")
        print(f'1.Open an Account')
        print(f'2.Login to your Account')
        print(f'3.Make a Deposit')
        print(f'4.Make a Transfer')
        print(f'5. Buy Bundles')
        print(f'6.Call Customer Service')
        print(f'7.Check Account Balance')
        print(f'8.Exit')
        option = input("Enter an option to proceed>>>:")
        if option == '1':
            bankus.customer_info()
        elif option == "2":
            bankus.login()
        elif option == "3":
            bankus.Deposit()
        elif option == "4":
            bankus.transfer()
        elif option == "5":
            bankus.bundle()
        elif option == "6":
            bankus.service()
        elif option == "7":
            bankus.Balance()
        elif option == "8":
            quit()




    def customer_info(self):
        
        print(f'Welcome to Polaris Bank,Please sign up to enjoy our services')
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
        self.account_number = random.randrange(11111111111, 55555555555)
        bank_customer = 'INSERT into polarisbank (Account_number, Firstname, Surname, Email, Password, Phone, Username, Pin, inflow, outflow, total_balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        details = (self.account_number, self.firstname, self.surname, self.email, self.password, self.phone, self.username, self.pin, self.inflow, self.outflow, self.total_balance)
        manage.execute(bank_customer, details)
        connect.commit()
        print(manage.rowcount, 'record(s) inserted successfully')
        print(f'Welcome {self.firstname}!')
        print(f'Your Account Number is {self.account_number}!\n Enjoy Banking with us!')
        # quit()
        print(f'Login into your Account to make your First Deposit!')
        bankus.login()
        # choice = input("Enter an option>>>>:")
        # # if choice == '1':

    def login(self):

        print(f'Enter your Username and Password as Login Details')
        self.username = input("Enter your username>>>:")
        self.password = input("Enter your password>>>:")
        bank_customer = 'SELECT * FROM polarisbank WHERE Username=%s AND Password=%s'
        details = (self.username, self.password)
        manage.execute(bank_customer, details)
        report = manage.fetchone()
        # print(report)
        print(f'Welcome {self.username},What will you like to do today?')
        print("1.Deposit 2.Make a Transfer 3.Make a Withdrawal 4.Check Balance 5.Exit")
        choice = input("Enter an option to proceed")
        if choice == '1':
            bankus.Deposit()
        elif choice == '2':
            bankus.transfer()
        elif choice == '3':
            bankus.Withdrawal()
        elif choice == '4':
            bankus.Balance()
        elif choice == '5':
            quit()
        else:
            print("Invalid Option")
            quit()


    def Deposit(self):
        
        print("Make a Deposit")
        choice = input("Please Enter 1 to Make a Deposit>>>>:")
        if choice == '1':
            self.Account_Number = input("Enter Account Number>>>:")
            self.pin = input("Enter Pin>>>>:")
            data6 = "SELECT total_balance FROM polarisbank WHERE Account_Number=%s AND Pin=%s"
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
            payment = "UPDATE polarisbank SET inflow=%s WHERE Account_Number=%s"
            payment1 = "UPDATE polarisbank SET total_balance=%s WHERE Account_Number=%s"
            # payment2 = "UPDATE gtbank SET total_balance=%s WHERE inflow=%s"
            details = (self.inflow, self.Account_Number)
            details1 = (self.total_balance, self.Account_Number)
            manage.execute(payment, details)
            manage.execute(payment1, details1)
            connect.commit()
            print(f'Your Deposit of {self.inflow} is Successful')
            print(f'Thank you for Banking with us!')
            quit()

    def transfer(self):
        
        print("To Access Your Account,Please Enter your Password")
        self.password= input("Enter Password>>>>:")
        report = "SELECT total_balance FROM polarisbank WHERE Password=%s"
        details = (self.password,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        self.balance = (report[-1])
        print(self.balance)
        print(f'1.Transfer to Polaris Bank Account\n2. Transfer GT Bank\n3. Transfer to Access Bank')

        choice = input("Enter an option>>>>:")
        if choice == '1':
            amount = int(input("Enter amount to be transferred>>>>:"))
            charges = 30
            outflow = int(amount + charges)
            print(outflow)
            self.Pin = input("Enter Pin>>>>:")
            data = "UPDATE polarisbank SET outflow=%s WHERE Pin=%s"
            val = (outflow, self.Pin)
            manage.execute(data, val)
            connect.commit()
            self.total_balance = (report[-1])
            self.total_balance = self.total_balance - outflow
            data1 = "UPDATE polarisbank SET total_balance=%s WHERE Pin=%s"
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
            # benef_acct = input("Enter Benef account Number>>>:")
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
        elif choice == '2':
                    amount = int(input("Enter amount to be transferred>>>>:"))
                    charges = 60
                    outflow = int(amount + charges)
                    print(outflow)
                    self.Pin = input("Enter Pin>>>>:")
                    data = "UPDATE polarisbank SET outflow=%s WHERE Pin=%s"
                    val = (outflow, self.Pin)
                    manage.execute(data, val)
                    connect.commit()
                    self.total_balance = (report[-1])
                    self.total_balance = self.total_balance - outflow
                    data1 = "UPDATE polarisbank SET total_balance=%s WHERE Pin=%s"
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
                    balance = (report[-1])
                    print(balance)
                        
                    self.inflow = amount
                    amount = input("Confirm amount to be transferred")
                    self.Account_Number = input("Confirm Benef account Number>>>:")
                    balance = (report[-1])
                    self.total_balance = (self.inflow + balance)
                    data4 = "UPDATE gtbank SET inflow=%s WHERE Account_Number=%s"
                    data3 = "UPDATE gtbank SET total_balance=%s WHERE Account_Number=%s"
                    val4 = (self.inflow, self.Account_Number)
                    val3 = (self.total_balance, self.Account_Number)
                    manage.execute(data4, val4)
                    manage.execute(data3, val3)
                    connect.commit()
                    print(f'Your Transfer of {self.inflow} is Successful')

        elif choice == '3':
            amount = int(input("Enter amount to be transferred>>>>:"))
            charges = 60
            outflow = int(amount + charges)
            print(outflow)
            self.Pin = input("Enter Pin>>>>:")
            data = "UPDATE polarisbank SET outflow=%s WHERE Pin=%s"
            val = (outflow, self.Pin)
            manage.execute(data, val)
            connect.commit()
            self.total_balance = (report[-1])
            self.total_balance = self.total_balance - outflow
            data1 = "UPDATE polarisbank SET total_balance=%s WHERE Pin=%s"
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
                # benef_acct = input("Confirm Benef account Number>>>:")
            data = "SELECT total_balance FROM accessbank WHERE Account_Number=%s"
            val = (benef_acct,)
            manage.execute(data, val)
            report = manage.fetchone()
            balance = (report[-1])
            print(balance)
                
            self.inflow = amount
            amount = input("Confirm amount to be transferred")
            self.Account_Number = input("Confirm Benef account Number>>>:")
            balance = (report[-1])
            self.total_balance = (self.inflow + balance)
            data4 = "UPDATE accessbank SET inflow=%s WHERE Account_Number=%s"
            data3 = "UPDATE accessbank SET total_balance=%s WHERE Account_Number=%s"
            val4 = (self.inflow, self.Account_Number)
            val3 = (self.total_balance, self.Account_Number)
            manage.execute(data4, val4)
            manage.execute(data3, val3)
            connect.commit()
            print(f'Your Transfer of {self.inflow} is Successful')


    def Withdrawal(self):
        self.password= input("Enter Password>>>>:")
        report = "SELECT total_balance FROM polarisbank WHERE Password=%s"
        details = (self.password,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        self.balance = (report[-1])
        print(self.balance)
        print("1.Make a Withdrawal 2.Go back to the Main Menu")
        option = input("Enter an option to proceed>>>>:")
        if option == '1':
            amount = int(input("Enter amount to Withdraw>>>>:"))
            charges = 30
            outflow = int(amount + charges)
            print(outflow)
            self.Pin = input("Enter Pin>>>>:")
            data = "UPDATE polarisbank SET outflow=%s WHERE Pin=%s"
            val = (outflow, self.Pin)
            manage.execute(data, val)
            connect.commit()
            self.total_balance = (report[-1])
            self.total_balance = self.total_balance - outflow
            data1 = "UPDATE polarisbank SET total_balance=%s WHERE Pin=%s"
            val1 = (self.total_balance, self.Pin,)
            manage.execute(data1, val1)
            connect.commit()
            benef_acct = input("Enter Account Number>>>:")
            data = "SELECT Firstname, Surname FROM polarisbank WHERE Account_Number=%s"
            val = (benef_acct,)
            manage.execute(data, val)
            report = manage.fetchone()
            print(report)
            print(f'Your Withdrawal has been processed successful')
            print(f'Thank you for Banking with us!')
            quit()

    def Balance(self):
        self.pin = input("Enter Pin>>>>:")
        report = "SELECT total_balance FROM polarisbank WHERE Pin=%s"
        details = (self.pin,)
        manage.execute(report, details)
        report = manage.fetchone()
        print(report)
        print(f'Your account balance is', report)

    def debit(self):
        self.password= input("Enter Password>>>>:")
        report = "SELECT total_balance FROM polarisbank WHERE Password=%s"
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
        data = "UPDATE polarisbank SET outflow=%s WHERE Pin=%s"
        val = (outflow, self.Pin)
        manage.execute(data, val)
        connect.commit()
        self.total_balance = (report[-1])
        self.total_balance = self.total_balance - outflow
        data1 = "UPDATE polarisbank SET total_balance=%s WHERE Pin=%s"
        val1 = (self.total_balance, self.Pin,)
        manage.execute(data1, val1)
        connect.commit()
        print(f'Your Purchase is Successful!')

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
                bankus.debit()
            elif option == '2':
                bankus.debit()
            elif option == '3':
                bankus.debit()
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
                bankus.debit()
            elif option == '2':
                bankus.debit()
            elif option == '3':
                bankus.debit()
            elif option == '4':
                bankus.debit()
            else:
                print("Invalid option")
                print("Thank you for Banking with Us!","Go back to the Main Menu")
                quit()



bankus = Pool()
# bankus.customer_info()
# bankus.Deposit()
# bankus.transfer()
# bankus.Withdrawal()
# bankus.Balance()
# bankus.debit()