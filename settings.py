import json
import os
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
        self.file_name = ''  # this will be needed for account deactivation
        self.name = ''
        self.login_details = []

    def get_login_list(self):
        """ calling the list with all the login information"""
        self.login_details = self.load_login_details()
        return self.login_details

    def view_profile(self, name):
        name2 = name.replace(" ", "_")
        file_name = name2 + ".txt"
        self.file_name = file_name
        try:
            read_file = open(self.file_name, 'r')
            print(read_file.read())
            read_file.close
            input("\n\nPress enter to continue....")
        except FileNotFoundError:
            print("Oops! File could not be found!")

    def change_username(self, index_pos):
        index = index_pos
        user_data = self.login_details
        new_username = input("Enter your new username: ")
        user_data[index]['Username'] = new_username

        print(f"Username has been changed to {new_username}")
        print(user_data[index])
        self.save_updated_login_details()
        return self.login_details

    def change_password(self, index_pos):
        index = index_pos
        user_data = self.login_details
        new_password = input("Enter your new password: ")
        user_data[index]['Password'] = new_password

        print(f"Password has been changed to {new_password}")
        print(user_data[index])
        self.save_updated_login_details()
        return self.login_details

    def change_pin(self, index_pos):
        index = index_pos
        user_data = self.login_details
        new_pin = input("Enter your new PIN: ")
        user_data[index]['Pin'] = new_pin

        print(f"Username has been changed to {new_pin}")
        print(user_data[index])
        self.save_updated_login_details()
        return self.login_details

    def save_updated_login_details(self):
        updated_credentials = self.login_details
        os.remove('Login_db.txt')

        with open("Login_db.txt", 'w') as file:
            for dic in updated_credentials:
                file.write(json.dumps(dic))
                file.write("\n")

        file.close()

        print("Account login details have been saved")

