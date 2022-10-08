import mysql.connector
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='extraexam')
manage = connect.cursor()


# import mysql.connector
# mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='')
# mycursor = mycon.cursor()

# CREATE DATABASE
# mycursor.execute("CREATE DATABASE mainexam")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# CREATE DATABASE
# manage.execute("CREATE DATABASE extraexam")
# manage.execute("SHOW DATABASES")
# for db in manage:
#     print(db)

# CREATE TABLE
# manage.execute("CREATE TABLE extraexam (Firstname VARCHAR(20), Surname VARCHAR(20), Username VARCHAR(40), Pin INT(4), score INT(4))")
# manage.execute("SHOW TABLES")
# for table in manage: 
#     print(table)




class Examination:
    def __init__(self):
        self.nu = 'nu'
# Candidate Registration

    def registration(self):
        
        print(f'Welcome! Enter your details to register below')
        self.fname = input('Firstname>>:')
        self.sname = input('Surname>>:')
        self.uname = input('Username>>:')
        self.pin = int(input('Pin>>:'))
        cand_details = 'INSERT into extraexam (Firstname, Surname, Username, Pin, Score) VALUES(%s, %s, %s, %s,%s)'
        val = (self.fname, self.sname, self.uname, self.pin, 0)
        manage.execute(cand_details, val)
        connect.commit()
        print(manage.rowcount, 'record(s) inserted successfully')

# Candidate Login
    def login(self):
        print(f'Welcome,Please Login below')
        self.uname =  input('Username>>:')
        self.pin = int(input('Pin>>:'))
        cand_details = 'SELECT * FROM extraexam WHERE Username=%s AND Pin=%s'
        val = (self.uname, self.pin)
        manage.execute(cand_details, val)
        report = manage.fetchone()
        print(report)
        count = 1

        while count <= 3:
            self.uname = input('Username>>:')
            self.pin = int(input('Pin>>:'))
            cand_details = 'SELECT * FROM extraexam WHERE Username=%s AND Pin=%s'
            val = (self.uname, self.pin)
            manage.execute(cand_details, val)
            report = manage.fetchone()
            if self.uname == report[-3] and self.pin == report [-2]:
                print(f'Welcome back {self.uname}!\nTake test below')
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
        self.uname = self.uname
        score = "UPDATE extraexam SET Score=%s WHERE Username=%s"
        val = (p, self.uname)
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


