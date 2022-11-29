
from account import Account
from log_in import LogIn
import menu_options as menu
from settings import Settings


while True:
    login = LogIn()
    new_account = Account()
    settings = Settings()

    # loop exit flags
    in_settings_menu = True
    logged_in = True

    # Execution
    print(menu.start_up)
    menu_choice = input("\nEnter an option from the menu above: ")

    # Log In
    if menu_choice == "1":
        name = input("\nPlease enter your username: ")
        pin = input("Please enter your pin: ")
        password = input("Please enter your password: ")
        login.get_index(name)

        if login.verify_login(name, pin, password):
            print("\nLogging in ...\n")
            login.welcome_user()

            while logged_in:
                print(menu.account_options)
                option = input("\nPlease choose an option from the Account Option menu above: \n")

                #  Account Settings menu
                if option == '1': # ********** THIS IS WHERE YOU ARE TESTING *********
                    while in_settings_menu:
                        #settings.get_index(name)
                        print(menu.settings)
                        option = input("\nPLease choose an option form the Settings menu above: \n")

                        #  View profile
                        if option == '1':
                            settings.view_profile()

                        #  Change Username
                        elif option == '2':
                            settings.change_username()

                        #  Change password
                        # elif option == '3':
                        #     settings.change_password()

                        #  Change pin
                        # elif option == '4':
                        #     settings.change_pin()

                        #  Deactivate account
                        # elif option == '5':
                        #     settings.deactivate_account()

                        #  Return to Account Options menu
                        elif option == '6':
                            # exit settings menu
                            in_settings_menu = False

                elif option == '2':
                    print(menu.statements)
                    option = input("\nPlease choose an option from the Statements menu above: \n")

                    # TODO: Statements class logic
                    #       1- View All Statements'
                    #       2- Monthly Statements'
                    #       3- Insights
                else:
                    logged_in = False
        else:

            print("\nInvalid credentials.")
            print("\nYou have been BLOCKED."
                  "\nProgram shutting down...")
            break

    # Create Account
    elif menu_choice == "2":
        new_account.create_account()

    # Quit Program
    elif menu_choice == "3":
        print("\nShutting Down...")
        break

    elif menu_choice == "4":
        # dev option to view the log_in details, for testing purposes
        print(login.load_login_details())

    elif menu_choice == "5":  # for testing purposes
        pass
    # If not valid option
    else:
        print("\nChoice not valid")

