
import pickle


# **** SAVE DATA ***
from os.path import exists


# user_login_db.append({"Name": "Nacho Darby",
#                       "Username": "Ndarb",
#                       "Password": "8675309",
#                       "Pin": "0987"})


# **** SAVE DATA ***
def save_login_details():
    user_login_db = [{"Name": "Amber Wonnenberg",
                      "Username": "Awonn",
                      "Password": "11009309",
                      "Pin": "3456"}]
    # take input of the data
    # open a file, where you want to store the data.
    file_name = "Login_DB.txt"
    if exists(file_name):
        with open("Login_DB.txt", 'ab+') as file:
            # dump information to that file
            pickle.dump(user_login_db, file)

    else:
        with open("Login_DB.txt", "wb") as file:
            # dump information to that file
            pickle.dump(user_login_db, file)

    # close file
    file.close()


#save_login_details()

# *** LOAD DATA ****
def load_login_details():
    details = []
    file_name = "Login_DB.txt"
    # open a file, where you stored the pickled data
    file = open(file_name, 'rb')
    try:
        while True:
            # dump information to that file
            details.append(pickle.load(file))

    except EOFError:
        # close the file
        file.close()
    print(details)


load_login_details()