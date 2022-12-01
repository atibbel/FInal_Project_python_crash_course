import ast
from account import Account


class LogIn(Account):
    """ User will be able to log in using their username, password, and PIN. """

    def __init__(self):
        Account.__init__(self)
        self.index = 0
        self.account_name = ''
        self.user_login_db = []

    # *** LOAD DATA into list****
    def load_login_details(self):
        """ will load saved user data back into a list for use"""
        file_name = "Login_db.txt"
        credentials = []
        try:
            with open(file_name) as file:
                data_list = file.readlines()
            # reads each line from the file into the list. Creating a list of dictionaries
            for line in data_list:
                credentials.append(ast.literal_eval(line))
            file.close()

        except FileNotFoundError:
            print("File not found. No accounts created yet.")

        self.user_login_db = credentials
        return self.user_login_db

    def get_index(self, username):
        """ find the index of the dictionary that the user detail are in. """
        index = 0
        user_data = self.load_login_details()
        for dic in user_data[index]:
            # if inputted username matches username at this index, then we found the correct index location
            if user_data[index]['Username'] == username:
                break
            else:
                index += 1
        # index is saved
        self.index = index
        return self.index

    def verify_username(self, username):
        """ verifies username entered matches the username in the list at the index of a specific user """
        user_data = self.user_login_db
        # retrieve the found index
        index = self.index
        # if username in dictionary equals inputted username
        if user_data[index]['Username'] == username:
            print("\nValid username")
            is_valid = True
        else:
            print("Invalid username")

            is_valid = False

        return is_valid

    def verify_pin(self, pin):
        """ verifies pin entered matches the pin in the list at the index of a specific user """
        user_data = self.user_login_db
        index = self.index
        if user_data[index]['Pin'] == pin:
            print("Valid pin")
            is_valid = True
        else:
            print("Invalid pin")

            is_valid = False

        return is_valid

    def verify_password(self, password):
        """ verifies password entered matches the password in the list at the index of a specific user """
        user_data = self.user_login_db
        index = self.index
        # for dic in user_data[index]:
        if user_data[index]['Password'] == password:
            print("Valid password")
            is_valid = True
        else:
            print("Invalid password")

            is_valid = False
        return is_valid

    def verify_login(self, username, pin, password):
        """ verify that username, pin and password are all valid and return True """

        if self.verify_username(username) and self.verify_pin(pin) and self.verify_password(password):
            valid_login = True
        else:
            valid_login = False

        return valid_login

    def welcome_user(self):
        """Displays a welcome message to the logged-in user"""
        user_data = self.user_login_db
        index = self.index
        welcome_name = user_data[index]['Name']
        split_name = "".join(welcome_name).split()
        first_name = split_name[0]
        print(f'\nWelcome {first_name}!')

    def get_name(self):
        """return the account name of the user"""
        index = self.index
        user_data = self.user_login_db
        account_name = user_data[index]['Name']
        self.account_name = "".join(account_name)

        return self.account_name
