# TEMPERATE CONVERTER WITH USER LOGIN
print('Welcome to Temperature Converter Portal')
print('Please Enter your Username and Password to Continue')
username = input('Enter your Username >>>>:')
custom_username = ['green','red','yellow']
if username in custom_username:
    print('Username is Valid')
else:
    print('Incorrect Username')
password = int(input('Enter your password>>>>:'))
custom_password = [2010,2011,2012]
if password in custom_password:
    print('Temperature Converter Menu')
else:
    print('Incorrect Password')
temp = input('Enter the unit you want to convert from :')
if temp.upper() == 'C':
    temps = input('Enter the unit you want to convert to :')
    if temps.upper() == 'F' :
        c = int(input('Enter the value for temp(c):'))
        result = (9/5 * c) + 32
        print(result, 'F')
    else:
        print('Error')
elif temp.upper() == 'F':
    temps = input('Enter the unit you want to convert to :')
    if temps.upper() == 'C':
        f = int(input('Enter the value for temp(f):'))
        result = (f-32) * 5/9
        print(result, 'C')
    else:
        print('Error')
elif temp.upper() == 'K':
    t = input('Enter the unit you want to convert to: ')
    if t.upper() == 'C':
        k = int(input('Enter the value for temp(k): '))
        result = (k - 273.15)
        print(result, 'C')
    elif t.upper() == 'F':
        k = int(input('Enter the value for temp(k):'))
        result = (k - 273.15) * 9/5 + 32
        print(result, 'F')
else:
    print('Unknown Input')
    quit()
