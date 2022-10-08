
import mysql.connector
import re
press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='newstep')
manage = connect.cursor()
# CREATE DATABASE
# manage.execute("CREATE DATABASE newstep")
# manage.execute("SHOW DATABASES")
# for db in manage:
#     print(db)

# CREATE TABLE
# manage.execute("CREATE TABLE balance (Firstname VARCHAR(20), Surname VARCHAR(20), Email VARCHAR(50), Password VARCHAR(30), Score INT(10))")
# manage.execute("SHOW TABLES")
# for table in manage:
#     print(table)
# press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class Examination:
    def __init__(self):
        self.nu = 'nu'
# Candidate Registration

    def registration(self):
        
        print(f'Welcome! Enter your details to register below')
        self.fname = input('Firstname>>:')
        self.sname = input('Surname>>:')
        # press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.email = input('Email>>:')
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
        cand_details = 'INSERT into balance (Firstname, Surname, Email, Password, Score) VALUES(%s, %s, %s, %s,%s)'
        val = (self.fname, self.sname, self.email, self.password, 0)
        manage.execute(cand_details, val)
        connect.commit()
        print(manage.rowcount, 'record(s) inserted successfully')

# Candidate Login
    def login(self):
        print(f'Welcome,Please Login below')
        self.email =  input('Enter your email>>:')
        self.password = (input('Password>>:'))
        cand_details = 'SELECT * FROM balance WHERE email=%s AND Password=%s'
        val = (self.email, self.password)
        manage.execute(cand_details, val)
        report = manage.fetchone()
        print(report)
        count = 1

        while count <= 3:
            self.email = input('Email>>:')
            self.password = (input('Password>>:'))
            cand_details = 'SELECT * FROM balance WHERE email=%s AND Password=%s'
            val = (self.email, self.password)
            manage.execute(cand_details, val)
            report = manage.fetchone()
            if self.email == report[-3] and self.password == report [-2]:
                print(f'Welcome back {self.email}!\nTake test below')
                x.questions()
            break
        else:
            count += 1
            print('Invalid input.\nlogged out!')

    def questions(self):
        p = 0
        # QUESTION NUMBER ONE
        exer = ("The number of states in Nigeria is_____________")
        print(exer)
        print("""
                (a) 45 States
                (b) 90 States
                (c) 36 States
        """)
        exer = input("Choose an Answer from the Options above>>:")
        if exer == 'c':
            print("Valid")
            p += 5
            # print(p)
            print("You have 5 Marks")
        else:
            p==0
            # return p
            print("Invalid")
            print(p)
        # QUESTION NUMBER TWO
        exer = ("The capital of United States is_____________")
        print(exer)
        print("""
                (a) Abuja
                (b) Washington
                (c) New York
        """)
        exer = input("Choose an Answer from the Options above>>>>>")
        if exer == 'b':
            print("Valid")
            p += 5
            # print(p)
            print("You have 5 Marks")
        else:
            p==0
        # return p
            print("Invalid")
            print(p)
        # QUESTION NUMBER THREE
        exer = ("Which of the following is a fruit?_____________")
        print(exer)
        print("""
                (a) Lagos
                (b) Books
                (c) Orange
        """)
        exer = input("Choose an Answer from the Options above>>>>>")
        if exer == 'c':
            print("Valid")
            p += 5
            # print(p)
            print("You have 5 Marks")
        else:
            print("Invalid")
            p==0
            print(p)
        # QUESTION NUMBER FOUR
        exer = ("What color represent Agriculture?_____________")
        print(exer)
        print("""
                (a) Green
                (b) Red
                (c) Black
        """)
        exer = input("Choose an Answer from the Options above>>>>>")
        if exer == 'a':
            print("Valid")
            p += 5
            # print(p)
            print("You have 5 Marks")
        else:
            print("Invalid")
            p==0
            print(p)

        # QUESTION NUMBER FIVE
        exer = ("Which of the following animal has wings?_____________")
        print(exer)
        print("""
                (a) A Bird
                (b) A Goat
                (c) A Rat
        """)
        exer = input("Choose an Answer from the Options above>>>>>")
        if exer == 'a':
            print("Valid")
            p += 5
            # print(p)
            print("You have 5 Marks")
        else:
            print("Invalid")
            p == 0

        # TOTAL MARKS
            print(f'Your Objective Examination is Over,Congratulations!')
            print('You have', p ,'points')
        print(f'Thank you for writing this test. \nYour Total Score is {p/25*100}%')
        self.email = self.email
        score = "UPDATE balance SET Score=%s WHERE Email=%s"
        val = (p, self.email)
        manage.execute(score, val)
        connect.commit()
        print(manage.rowcount, 'record(s) updated successfully')

x = Examination()
print('Enter 1 to Register or 2 to Login')
choice = input('Response>>>:')
if choice == '1':
    x.registration()
    x.login()
elif choice == '2':
    x.login()

else:
    count = 1
    while count <= 2:
        print(f'Invalid input. \nChoose 1 to Register or 2 to Login')
        choice = input('Response>>>:')
        if choice == '1':
            x.registration()
        elif choice == '2':
            Examination().login()
        count += 1
    else:
        print(f'Page suspended! Try again tomorrow!!!')

# press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# email = input('Enter your email')
# password = input('Enter your password')
# def check():
#     if(re.fullmatch(press, email)):
#         print("Valid Email")
#     else:
#         print("Please Enter a valid Email")
#         email = input('Enter your email')
#         password = input('Enter your password')
# check()

