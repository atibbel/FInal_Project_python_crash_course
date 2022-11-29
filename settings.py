import pickle
from os.path import exists
from log_in import LogIn


class Settings(LogIn):

    """Settings – View profile User should be able to view their profile
        with all the information given during profile creation.

        Settings - Change username Current users should be able to change
        their usernames in the settings section.

        Settings - Change password Current users should be able to change
        their password in the settings section.

        Settings - Change PIN Current users should be able to change
        their PIN in the settings section.

        Settings – Deactivate account Current users should be able to
        deactivate their account and their
        information deleted."""

    def __init__(self):
        LogIn.__init__(self)
        self.account_name = ''
        self.login_db = []

    def get_account_name(self):
        self.login_db = self.load_login_details()
        index = self.count
        user_list = self.login_db[index]
        account_name = [name["Name"] for name in user_list]
        self.account_name = "".join(account_name)

        return self.account_name

    def view_profile(self):
        get_name = self.get_account_name()
        name = get_name.replace(" ", "_")
        file_name = name + ".txt"
        try:
            read_file = open(file_name, 'r')
            print(read_file.read())
            read_file.close
            input("\n\nPress enter to continue....")
        except FileNotFoundError:
            print("Oops! File could not be found!")

    # def change_username(self):
    #     self.login_db = self.load_login_details()
    #     index = self.count
    #     print(self.login_db)  # *** TESTING
    #     new_username = input("Enter your new username: ")
    #     self.login_db[index][0]['Username'] = new_username  # dict in a list in a list
    #     print(self.login_db[index])  # *** TESTING
    #
    #     try:
    #         # appending to file
    #         with open("Login_DB.txt", 'wb') as file:
    #             # dump information to that file
    #             pickle.dump(self.login_db, file)
    #             file.close()
    #         print(f"Your username has been changed to {new_username}")
    #
    #     except FileNotFoundError:
    #         print(f"New username could not be saved. ")
    #
    #     # close file
    #     file.close()