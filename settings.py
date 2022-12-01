import json
import os
from log_in import LogIn


class Settings(LogIn):

    # TODO: Deactivate account - Current users should be able
    #  to deactivate their account and their information deleted.

    def __init__(self):
        LogIn.__init__(self)
        self.file_name = ''  # this will be needed for account deactivation
        self.name = ''
        self.login_details = []

    def get_login_list(self):
        """ loading an empty list with the login information"""
        self.login_details = self.load_login_details()
        return self.login_details

    def view_profile(self, name):
        """ create filename from account name then read file for user to view"""

        # replace the blank space between the first and last name with an undescore
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

        return self.file_name

    def change_username(self, index_pos):
        """ finds users current username and replaces it with new username"""
        index = index_pos
        user_data = self.login_details
        new_username = input("Enter your new username: ")
        user_data[index]['Username'] = new_username

        print(f"Username has been changed to {new_username}")
        print(user_data[index])
        # saves changed username info into login_db file
        self.save_updated_login_details()
        return self.login_details

    def change_password(self, index_pos):
        """ finds users current password and replaces it with new password. Then saves the new info"""
        index = index_pos
        user_data = self.login_details
        new_password = input("Enter your new password: ")
        user_data[index]['Password'] = new_password

        print(f"Password has been changed to {new_password}")
        print(user_data[index])
        self.save_updated_login_details()
        return self.login_details

    def change_pin(self, index_pos):
        """ finds users current pin and replaces it with new password. Then saves the new info"""
        index = index_pos
        user_data = self.login_details
        new_pin = input("Enter your new PIN: ")
        user_data[index]['Pin'] = new_pin

        print(f"Username has been changed to {new_pin}")
        print(user_data[index])
        self.save_updated_login_details()
        return self.login_details

    def save_updated_login_details(self):
        """ replaces old file with updated user login information"""
        updated_credentials = self.login_details
        # delete old file
        os.remove('Login_db.txt')

        # Write updated info to newly created file.
        with open("Login_db.txt", 'w') as file:
            # loop through the current login_details list to load each entry on a new line
            for dic in updated_credentials:
                file.write(json.dumps(dic))
                file.write("\n")

        file.close()

        print("Account login details have been saved")

