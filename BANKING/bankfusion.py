from gtbbank import Money
from polaris import Pool
from testing import Banking
import mysql.connector
connect = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Multibanks')
manage = connect.cursor()
import random
import re
press = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'



class Banking:
    
    def __init__(self):
        self.bk = 'bk'


print(f'Welcome to MultiBanks Solutions System Inc')
print(f'Please Choose a Bank of your Interest and Sign Up to Start Enjoying our Services')
print(f'1.AccessBank\n2.GT Bank\n3.Polaris Bank') 
# option = input("Please Enter an option to proceed>>>>:")




bank = Banking()

bankme = Money()
bankus = Pool()




    
    






