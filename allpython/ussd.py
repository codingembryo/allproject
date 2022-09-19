print("Welcome to Coding Embryo Telecoms")
login = input('Enter the ussd code to begin>>>>:')
ussd_code = "*478#"
if login == ussd_code:
    print("1. Buy Data Plans")
    print("2. Buy Social Bundles")
    print("3.Roaming/Int")
    print("4.Transfer Airtime")
    print("5.Transfer Data")
    options = input('Choose from the options above>>:')
    if options == '1':
            print('Buy Data Plans')
            print('1.Daily')
            print('2.Weekly')
            print('3.Monthly')
            print('4.Quaterly')
            print('5.Yearly')
            options = input('Choose from the options above>>:')
            if options == '1':
                print('1.Daily Bundles')
                print('Buy 500MB for 300 Naira')
                card_details = input('Enter card details to buy Daily Bundle data>>>:')
                if len(card_details) == 16:
                    print('Payment Successful:Data Purchased Successfully!')
                else:
                    print('Invalid Card Number')
                    quit()
    elif options == '2':
        print('Buy Social Bundles')
        print('1.Facebook')
        print('2.Instagram')
        print('3.Twitter')
        print('4.Youtube')
        print('5.Others')
    elif options == '3':
        print("3.Roaming/Int")
        number = []
        if len(number) <= 10:
            number = input("Enter your phone number to roam>>>:")
            print("Roaming Successful")
        else:
            print("Phone Number must be 11 digits")
    elif options == '4':
        print("4.Transfer Airtime")
        number = []
        number = input("Enter phone number to transfer to>>>:")
        amount = int(input("Enter the amount>>>>:"))
        if len(number) >= 10:
            print("Transfer Successful")
        else:
            print("Phone Number must be 11 digits")

else:
    print('Incorrect Option')