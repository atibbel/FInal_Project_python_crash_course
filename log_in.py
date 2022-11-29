import pickle
from account import Account


class LogIn(Account):
    """ User will be able to log in using their username, password, and PIN.
        Unauthorized users will be blocked.
         """

    def __init__(self):
        Account.__init__(self)
        self.count = 0

    # *** LOAD DATA into list****
    def load_login_details(self):
        """ will load saved user data from pickles back into a list for use"""
        file_name = "Login_DB.txt"
        # open a file, where you stored the pickled data
        file = open(file_name, 'rb')
        try:
            while True:
                # dump information to that file
                self.user_login_db.append(pickle.load(file))

        except EOFError:
            # close the file
            file.close()

        return self.user_login_db

    def get_index(self, username):
        """ find the index of the dictionary that the user detail are in. """

        self.load_login_details()
        user_cred = self.user_login_db
        for index in range(len(user_cred)):
            for key in user_cred[index]:
                if username in key["Username"]:
                    is_valid = True
                    break
                else:
                    self.count += 1
                    is_valid = False
            if is_valid:  # we found our username so, now we must break our of the second loop as well
                break
        # so we know the inputted username is at this index (count)
        return self.count

    def verify_username(self, username):
        user_cred = self.user_login_db
        index = self.count  # the index location found in get_index()
        for key in user_cred[index]:
            if username in key["Username"]:
                print("\nValid username")
                is_valid = True
                break
            else:
                print("Invalid username")

                is_valid = False

        return is_valid

    def verify_pin(self, pin):
        user_cred = self.user_login_db
        index = self.count
        for key in user_cred[index]:
            if pin in key["Pin"]:
                print("Valid pin")
                is_valid = True
                break
            else:
                print("Invalid pin")

                is_valid = False

        return is_valid

    def verify_password(self, password):
        user_cred = self.user_login_db
        index = self.count
        for key in user_cred[index]:
            if password in key["Password"]:
                print("Valid password")
                is_valid = True
                break
            else:
                print("Invalid password")

                is_valid = False
        return is_valid

    def verify_login(self, username, pin, password):
        """ verify that username, pin and password are all valid """
        self.load_login_details()
        if self.verify_username(username) and self.verify_pin(pin) and self.verify_password(password):
            valid_login = True
        else:
            valid_login = False

        return valid_login

    def welcome_user(self):
        """Displays a welcome message to the logged-in user"""
        user_cred = self.user_login_db
        index = self.count
        user_list = user_cred[index]
        welcome_name = [name["Name"] for name in user_list]
        split_name = "".join(welcome_name).split()
        first_name = split_name[0]
        print(f'\nWelcome {first_name}!')

