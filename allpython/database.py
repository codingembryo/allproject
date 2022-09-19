import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='tradingapp')
mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE TradingApp")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)


# mycursor.execute("CREATE TABLE polarisbank (ctm_id INT(4), Ful_Name VARCHAR(20), Address VARCHAR(60), Phone VARCHAR(11), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)

# myquery = "INSERT INTO polarisbank (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = ('Mike Adesola', 'USA', '07068996534', '99885532009')
# mycursor.execute(myquery, val)
# mycon.commit()

# sql = "DROP DATABASE bankapp"
# mycursor.execute(sql)
# print('successful')

# MONEYAPP
# mycursor.execute("CREATE DATABASE CowryPay")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE polarisbank (ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT, Ful_name VARCHAR(30), Address VARCHAR(40), Phone VARCHAR(12), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)

# myquery = "INSERT INTO polarisbank (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = ('Mike Adesola', 'USA', '080994471623', '33667712')
# mycursor.execute(myquery, val)
# mycon.commit()

# full_name = input('Enter your full name>>>')
# address = input('Enter your full address>>>')
# phone = input('Enter your phone number>>>>')
# password = input('Enter your Password>>>>')
# myquery = "INSERT INTO polarisbank (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = (full_name,address,phone,password)
# mycursor.execute(myquery, val)
# mycon.commit()
# print(mycursor.rowcount, "records inserted successfully")

# query = "SELECT * FROM polarisbank"
# mycursor.execute(query)
# output = mycursor.fetchall()
# # print(output)
# for inf in output:
#     print(inf)

# mmm = "SELECT * FROM polarisbank WHERE Ful_Name = %s"
# val = ("Adebola Olayole", )
# mycursor.execute(mmm,val)
# nm = mycursor.fetchall()
# print(nm)
# query = "SELECT * FROM customers WHERE Ful_Name LIKE '%bo%'"
# query = "SELECT Ful_Name, Phone FROM customers"
# query = "SELECT * FROM customers ORDER BY ful_Name DESC"
# val = ('09013140700', val)


# ASSIGNMENT
# TRADINGAPP
# CREATE DATABASE
# mycursor.execute("CREATE DATABASE TradingApp")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)



# mycursor.execute("CREATE TABLE freshbank (ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT NOT NULL, First_name VARCHAR(30) NOT NULL, Last_Name VARCHAR(20) NOT NULL, Phone VARCHAR(12) UNIQUE NOT NULL, Amount INT(20) NOT NULL, Pin INT(4) NOT NULL, confirm_pin INT(4) NOT NULL)")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)

# for i in range(5):
#     fname = input('Enter your first name>>>')
#     lname = input('Enter your Last Name>>>')
#     phone = input('Enter your phone number>>>>')
#     amount = input('Enter Amount>>>')
#     pin = input('Enter your Pin>>>>')
#     confirm_pin = input('Confirm your Pin>>>')
#     if confirm_pin != pin:
#         quit()
#     else:
#         myquery = "INSERT INTO freshbank (First_name, Last_Name, Phone, Amount, Pin, confirm_pin) VALUES(%s, %s, %s, %s, %s, %s)"
# val = (fname,lname,phone,amount,pin,confirm_pin)
#         mycursor.execute(myquery, val)
#         mycon.commit()
#         print(mycursor.rowcount, "records inserted successfully")

# TO FETCH DATA FROM THE DATABASE THROUGH USER INPUT VERIFICATION

# query = "SELECT * FROM freshbank ORDER BY First_name"
# first_name = input("Enter your First Name")
# amount = input("Enter your amount")
# query = "SELECT ctm_id, pin FROM freshbank WHERE First_name=%s AND Amount=%s "
# val = (first_name, amount)
# mycursor.execute(query, val)
# nm = mycursor.fetchall()
# print(nm)
# # # for i in nm:
# #     print(i)

# TO CHANGE ANY DATA INSIDE THE TABLE
# sql = "UPDATE freshbank SET Amount = '12000000' WHERE Pin=%s"
# val =('3300',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record updated successfuly')

sql = "DELETE from freshbank WHERE pin=%s"
val =('4466',)
mycursor.execute(sql, val)
mycon.commit()
print(mycursor.rowcount, 'record deleted successfuly')





# mycursor.execute("CREATE TABLE tradebank (ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT NOT NULL, First_name VARCHAR(30) NOT NULL, Last_name VARCHAR(30) NOT NULL, Phone VARCHAR(11) UNIQUE NOT NULL, Amount VARCHAR(20) NOT NULL, Password VARCHAR(20) NOT NULL, Pin INT(4) NOT NULL, Confirm Pin INT(4) NOT NULL)")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)