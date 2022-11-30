import json
import random
import secrets
import string
from os.path import exists
import pickle


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
        if exists(file_name + ".txt"):
            sign_in = input("\nAccount already exists. Would you like to log in? ").lower()
            if sign_in == "y":
                # TODO: enter login function once created
                print("opening log in window.....")

        else:
            new_file = open(file_name + '.txt', 'x')
            new_file.write(f"\nUSER DETAILS:"
                           f"\n------------------"
                           f"{user_info} ")
            new_file.close()

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
        for num in range(8):
            random_account_number = secrets.choice(string.digits)
            new_account_number += random_account_number

        self.account_number = "".join(new_account_number) + "-" + business_initials.upper()
        return self.account_number

    def business_initials(self):
        """ Returns the first two letters of the business name"""
        initials_list = []
        for letter in range(2):
            initials_list.append(self.business_name[letter])

        return ''.join(initials_list)

    def create_pin(self):
        """creates a random 4-digit pin"""
        new_pin = ''
        for char in range(4):
            random_pin = secrets.choice(string.digits)
            new_pin += random_pin

        self.pin = new_pin
        return self.pin

    def create_username(self):
        """ Creates a username """
        name = self.name.split()
        first_name = name[0]
        last_name = name[1]
        username = first_name[0] + last_name[0:4]

        return "".join(username).lower()

    def create_password(self):
        """ Generates a secure 7 character password"""
        punctuation = ["!", "@", "#", "&", "*"]
        new_password = []
        for char in range(2):
            num = secrets.choice(string.digits) + secrets.choice(string.ascii_uppercase) + \
                  secrets.choice(string.ascii_lowercase)
            new_password.append(num)
        new_password += random.choice(punctuation)
        random.shuffle(new_password)

        self.password = "".join(new_password)
        return self.password

    def save_login_details(self):
        user_name = self.create_username()
        user_password = self.create_password()
        user_pin = self.create_pin()
        credentials = {"Name": f"{self.name}",
                       "Username": f"{user_name}",
                       "Password": f"{user_password}",
                       "Pin": f"{user_pin}"}

        if exists("Login_db.txt"):

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

        login_info = (f"\n"
                      f"\nLOG-IN INFORMATION:"
                      f" ** You will need this information to log in at a later time **"
                      f"\n-------------------"
                      f"\nUSERNAME: {user_name}"
                      f"\nPASSWORD: {user_password}"
                      f"\nPIN: {user_pin} ")
        print(login_info)
