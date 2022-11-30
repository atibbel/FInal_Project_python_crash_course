import ast
from account import Account


class LogIn(Account):
    """ User will be able to log in using their username, password, and PIN.
        Unauthorized users will be blocked.
         """

    def __init__(self):
        Account.__init__(self)
        self.index = 0
        self.account_name = ''
        self.user_login_db = []

    # *** LOAD DATA into list****
    def load_login_details(self):
        """ will load saved user data from pickles back into a list for use"""
        file_name = "Login_db.txt"
        credentials = []
        try:
            with open(file_name) as file:
                data_list = file.readlines()

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
            if user_data[index]['Username'] == username:
                is_valid = True
                break
            else:
                is_valid = False
                index += 1
        self.index = index
        return self.index

    def verify_username(self, username):
        user_data = self.user_login_db
        index = self.index  # the index location found in get_index()
        for dic in user_data[index]:
            if user_data[index]['Username'] == username:
                print("\nValid username")
                is_valid = True
                break
            else:
                print("Invalid username")

                is_valid = False

        return is_valid

    def verify_pin(self, pin):
        user_data = self.user_login_db
        index = self.index
        for dic in user_data[index]:
            if user_data[index]['Pin'] == pin:
                print("Valid pin")
                is_valid = True
                break
            else:
                print("Invalid pin")

                is_valid = False

        return is_valid

    def verify_password(self, password):
        user_data = self.user_login_db
        index = self.index
        for dic in user_data[index]:
            if user_data[index]['Password'] == password:
                print("Valid password")
                is_valid = True
                break
            else:
                print("Invalid password")

                is_valid = False
        return is_valid

    def verify_login(self, username, pin, password):
        """ verify that username, pin and password are all valid """

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
        """Displays a welcome message to the logged-in user"""
        index = self.index
        user_data = self.user_login_db
        account_name = user_data[index]['Name']
        self.account_name = "".join(account_name)

        return self.account_name
