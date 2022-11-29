import random
import time
import secrets
import string


class Account:

    def __init__(self):
        self.name = ''
        self.address = ''
        self.date_of_birth = ''
        self.business_name = ''
        self.incorporation_date = ''
        self.stakeholders_equities_list = ''
        self.pin = ''
        self.account_type = ''
        self.account_number = ''

    def create_account(self, user_name, user_address, d_o_b, name_of_business,
                       date_incorporated, stakeholders_equities):
        self.name = user_name
        self.address = user_address
        self.date_of_birth = d_o_b
        self.business_name = name_of_business
        self.incorporation_date = date_incorporated
        self.stakeholders_equities_list = stakeholders_equities

        print(f"\nName: {user_name.title()}"
              f"\nAddress: {user_address}"
              f"\nDate of Birth: {d_o_b}"
              f"\nBusiness: {name_of_business.title()}"
              f"\nIncorporation Date: {date_incorporated}"
              f"\nStakeholders/Equities: ${stakeholders_equities}"
              f"\nAccount Type: {self.set_account_type()}"  # calling the set account function
              f"\nAccount Number: {self.create_account_number(self.business_initials())}")  # calling the create account number function

    def set_account_type(self):
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
        """Create a random 8-digit account number ending in the business's initals"""
        new_account_number = ''
        for num in range(9):
            random_account_number = secrets.choice(string.digits)
            new_account_number += random_account_number

        self.account_number = "".join(new_account_number) + "-" + business_initials.upper()
        return self.account_number

    def business_initials(self):
        initials_list = []
        for letter in range(2):
            initials_list.append(self.business_name[letter])

        return ''.join(initials_list)

    def create_pin(self):
        new_pin = ''
        for char in range(4):
            random_pin = secrets.choice(string.digits)
            new_pin += random_pin

        self.pin = "".join(new_pin)
        return self.pin

    def print_all_statements(self, monthly_statement_list):
        pass

    def print_statement(self, monthlyStatement):
        pass


class monthlyStatement():
    # TODO: create a file to write statements to that the user may access.
    # month
    # year
    # transaction_list
    pass


# Execution
print('\n\n')
print("GEO Investments Customer Portal")
print("===============================")
print("1 - Log in\n2 - Create an account")
menu_choice = int(input("\nEnter an option: "))


# Log In
if menu_choice == 1:
    # TODO: Login logic followed by account actions
    print("\nIn Login")

# Create Account
elif menu_choice == 2:
    name = input("\nEnter your full name: ")
    address = input("Enter your address: ")
    date_of_birth = input("Enter your date of birth: yyy/mm/dd")
    business_name = input("Enter the name of your business: ")
    incorporation_date = input("Enter your business's date of incorporation: ")
    stakeholders_equities = input("Enter your business's stakeholder and equities: ")

    # Instantiate Account
    new_account = Account()
    new_account.create_account(name, address, date_of_birth, business_name, incorporation_date, stakeholders_equities)


# Quit Program
elif menu_choice == 3:
    # TODO: Quit program logic
    print("\nIn Quit")

# If not valid option
else:
    print("\nChoice not valid")
    # TODO: Implement looping menu until Quit (3) option chosen
