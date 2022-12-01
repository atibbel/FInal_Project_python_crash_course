from account import Account
from log_in import LogIn
import menu_options as menu
from settings import Settings
from statments import Statements

# loop flag.
run_program = True

while run_program:
    login = LogIn()
    new_account = Account()
    settings = Settings()
    statements = Statements()

    # loop exit flags
    in_settings_menu = True
    logged_in = True
    in_statements_menu = True

    # Execution
    print(menu.start_up)
    menu_choice = input("\nEnter an option from the menu above: ")

    # Log In
    if menu_choice == "1":
        name = input("\nPlease enter your username: ")
        password = input("Please enter your password: ")
        pin = input("Please enter your pin: ")
        login.get_index(name)

        # if login information is correct
        if login.verify_login(name, pin, password):
            print("\nLogging in ...\n")
            login.welcome_user()

            while logged_in:
                print(menu.account_options)
                option = input("\nPlease choose an option from the Account Option menu above: \n")

                # for dev purposes only. to help with testing
                if option == '0':  # TESTING
                    pass

                #  Account Settings menu
                elif option == '1':
                    in_settings_menu = True
                    while in_settings_menu:
                        print(menu.settings)
                        option = input("\nPlease choose an option form the Settings menu above: \n")
                        settings.get_login_list()
                        #  View profile
                        if option == '1':
                            settings.view_profile(login.get_name())

                        #  Change Username
                        elif option == '2':
                            settings.change_username(login.get_index(name))

                        # Change password
                        elif option == '3':
                            settings.change_password(login.get_index(name))

                        # Change pin
                        elif option == '4':
                            settings.change_pin(login.get_index(name))

                        # Deactivate account
                        elif option == '5':
                            settings.deactivate_account(login.get_index(name), login.get_name())
                            in_settings_menu = False
                            logged_in = False

                        #  Return to Account Options menu
                        elif option == '6':
                            # exit settings menu
                            in_settings_menu = False

                # Statements menu
                elif option == '2':
                    while in_statements_menu:
                        print(menu.statements)
                        option = input(
                            "\nPlease choose an option from the Statements menu above: \n")
                        # View all statements for the account
                        if option == '1':
                            statements.print_all_statements()
                        # View statement for a specific month
                        elif option == '2':
                            statements.print_statement()
                        # Add transaction to statement
                        elif option == '3':
                            statements.add_transaction()
                        # Monthly comparison insight
                        elif option == '4':
                            statements.statement_comparison()
                        # Quarterly insight
                        elif option == '5':
                            statements.quarterly_report()
                        # Exit statements menu
                        elif option == '6':
                            in_statements_menu = False

                # log out/ return to main menu
                else:
                    logged_in = False

        # if login credentials are invalid
        else:

            print("Invalid credentials.")
            print("\nYou have been BLOCKED."
                  "\nProgram shutting down...")
            break

    # Create Account
    elif menu_choice == "2":
        new_account.create_account()
        print("\nAccount created...")
        run_program = False

    # Quit Program
    elif menu_choice == "3":
        print("\nShutting Down...")
        break

    # dev option to view the log_in details, for testing purposes
    elif menu_choice == "4":
        print(login.load_login_details())

    # If not valid option
    else:
        print("\nChoice not valid")
