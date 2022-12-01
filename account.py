import json
import random
import secrets
import string
from os.path import exists


class Account:
    """ Creates user account, including username, password and pin.
    """

    def __init__(self):
        self.name = ''
        self.address = ''
        self.date_of_birth = ''
        self.business_name = ''
        self.incorporation_date = ''
        self.stakeholders_equities = ''
        self.pin = ''
        self.account_type = ''
        self.account_number = ''
        self.password = ''

    def enter_account_info(self):
        """Accepts user info required to create account"""

        self.name = input("\nEnter your full name: ").title()
        self.address = input("Enter your address: ")
        self.date_of_birth = input("Enter your date of birth: yyyy/mm/dd ")
        self.business_name = input("Enter the name of your business: ").title()
        self.incorporation_date = input("Enter your business's date of incorporation: ")
        self.stakeholders_equities = input("Enter your business's stakeholder and equities: ")

    def create_account(self):
        """ Saves and displays account information. Log in information is displayed, so they may later log in"""
        # call function to gather user input for account creation 
        self.enter_account_info()

        user_info = (f"\nName: {self.name}"
                     f"\nAddress: {self.address}"
                     f"\nDate of Birth: {self.date_of_birth}"
                     f"\nBusiness: {self.business_name}"
                     f"\nIncorporation Date: {self.incorporation_date}"
                     f"\nStakeholders/Equities: ${self.stakeholders_equities}"
                     f"\nAccount Type: {self.set_account_type()}"  # calling the set account function
                     f"\nAccount Number: {self.create_account_number(self.business_initials())}")

        file_name = f"{self.name.replace(' ', '_')}"
        # if the file exists, user will be informed account exists & will be prompted to login
        if exists(file_name + ".txt"):
            sign_in = input("\nAccount already exists. Would you like to log in? ").lower()
            if sign_in == "y":
                # TODO: enter login function once created
                print("opening log in window.....")

        else:
            # if the file does not exist, create file specific to the user and write data.
            new_file = open(file_name + '.txt', 'x')
            new_file.write(f"\nUSER DETAILS:"
                           f"\n------------------"
                           f"{user_info} ")
            new_file.close()

        # displays the users account information
        print(f"\nAccount created..."
              f"\n{user_info}")

        self.save_login_details()

    def set_account_type(self):
        """ Returns business account type"""
        print("\n1 - Small Business Class"
              "\n2 - Medium Business Class"
              "\n3 - Large Business Class"
              "\n4 - Enterprise Business Class")

        business_type_choice = int(input("Enter an account type: "))

        if business_type_choice == 1:
            self.account_type = "Small Business Class"
        elif business_type_choice == 2:
            self.account_type = "Medium Business Class"
        elif business_type_choice == 3:
            self.account_type = "Large Business Class"
        elif business_type_choice == 4:
            self.account_type = "Enterprise Business Class"
        else:
            print("\nChoice not valid")

        return self.account_type

    def create_account_number(self, business_initials):
        """Create a random 8-digit account number ending in the first two letters of the business name"""
        new_account_number = ''
        # loops 8 times to generate 8 random digits
        for num in range(8):
            random_account_number = secrets.choice(string.digits)
            # adds the random digit to new_account_number string
            new_account_number += random_account_number

        # joins the business initials to the end of the account number
        self.account_number = "".join(new_account_number) + "-" + business_initials.upper()
        return self.account_number

    def business_initials(self):
        """ Returns the first two letters of the business name"""
        initials_list = []
        for letter in range(2):
            initials_list.append(self.business_name[letter])

        # join the two letters from the list, into a string
        return ''.join(initials_list)

    def create_pin(self):
        """creates a random 4-digit pin"""
        new_pin = ''
        # loop 4 times to generate 4 random digits
        for char in range(4):
            random_pin = secrets.choice(string.digits)
            # add the random digit to a string each loop
            new_pin += random_pin

        self.pin = new_pin
        return self.pin

    def create_username(self):
        """ Creates a username """
        # split the username into a list.
        name = self.name.split()
        first_name = name[0]
        last_name = name[1]
        # take the first character from the first name and the first 4 from the last name to create a username
        username = first_name[0] + last_name[0:4]

        return "".join(username).lower()

    def create_password(self):
        """ Generates a secure 7 character password"""
        punctuation = ["!", "@", "#", "&", "*"]
        # instantiate a new list to save our random characters
        new_password = []
        # loops 2 times to get 2 random digit, 2 uppercase letters and 2 lowercase letters
        for char in range(2):
            num = secrets.choice(string.digits) + secrets.choice(string.ascii_uppercase) + \
                  secrets.choice(string.ascii_lowercase)
            new_password.append(num)
        # adds a random symbol to the list
        new_password += random.choice(punctuation)
        # the 7 characters are randomly shuffled for a unique password
        random.shuffle(new_password)

        self.password = "".join(new_password)
        return self.password

    def save_login_details(self):
        """ When a new account is created the login information is saved to a separate list of dictionaries """
        user_name = self.create_username()
        user_password = self.create_password()
        user_pin = self.create_pin()
        credentials = {"Name": f"{self.name}",
                       "Username": f"{user_name}",
                       "Password": f"{user_password}",
                       "Pin": f"{user_pin}"}

        if exists("Login_db.txt"):
            # if the file already exists, the new data will be appended to the file
            with open("Login_db.txt", 'a') as file:
                # write dictionary into file using json.dumps()
                file.write(json.dumps(credentials))
                file.write("\n")

        else:
            with open("Login_db.txt", "w") as file:
                # write dictionary into file using json.dumps()
                file.write(json.dumps(credentials))
                file.write("\n")

        # close file
        file.close()
        # message displayed with login information for the new user
        login_info = (f"\n"
                      f"\nLOG-IN INFORMATION:"
                      f"\n ** You will need this information to log in at a later time **"
                      f"\n-------------------"
                      f"\nUSERNAME: {user_name}"
                      f"\nPASSWORD: {user_password}"
                      f"\nPIN: {user_pin} ")
        print(login_info)
