from monthly_statement import MonthlyStatement


class Statements:
    # TODO: create a file to write statements to that the user may access.
    """View Statements – All statements Current users should be able to view a
  list of all transactions made in their account. Users should also be able to
  view the total number of transactions made, and the total gain or loss in their
  account.
  View Statements – Monthly statements Current users should be able to view a
  list of all transactions made in their account. Users should also be able to
  view the total number of transactions made, and the total gain or loss in their
  account for any given month. View Statements – Insights Current users should be able to view
  insights in the following areas:
  - Compare monthly spending against other months
  -  Get a quarterly income report detailing money gain/loss per quarter.
  Fees – Charging businesses Every month all accounts are charged $10 to
  be with GEO Investments. This charge should also be included in
  monthly statements."""

    def __init__(self):
        self.statements_list = []

    # Create a new statement object and add it to statement_list
    def create_statement(self):
        month = input("For month (1 to 12): ")
        year = input("For year: ")
        new_statement = MonthlyStatement()
        new_statement.create_statement(month, year)
        self.statements_list.append(new_statement)

    # Print each statement by and totals looping through statements_list
    def print_all_statements(self):
        transaction_count = 0
        net_earnings = 0
        for statement in self.statements_list:
            statement.print_statement()
            transaction_count += statement.transaction_count
            net_earnings += statement.monthly_change()
        print(
            f"\nTotal transactions: {transaction_count}\nTotal gain/loss: ${net_earnings}"
        )

    # Print a single statement by month and year
    def print_statement(self):
        input_month = input("For month (1 to 12): ")
        input_year = input("For year: ")
        for statement in self.statements_list:
            if (statement.month == input_month and statement.year == input_year):
                statement.print_statement()
            else:
                print("No statement for that month found.")

    # Add  a transaction to a MonthlyStatement
    def add_transaction(self):
        input_month = input("For month (1 to 12): ")
        input_year = input("For year: ")
        input_date = int(input("For date (1 to 31): "))
        input_amount = input("Amount: ")
        for statement in self.statements_list:
            if (statement.month == input_month and statement.year == input_year):
                statement.add_transaction(input_date, input_amount)
                print("\nTransaction added.")
                return
        # If no statement existing, create a new one
        new_statement = MonthlyStatement()
        new_statement.create_statement(input_month, input_year)
        new_statement.add_transaction(input_date, input_amount)
        self.statements_list.append(new_statement)
        print("\nStatement created and transaction added.")

    # Total gain/loss per quarter
    def quarterly_report(self):
        q1_total = 0
        q2_total = 0
        q3_total = 0
        q4_total = 0
        input_year = input("For year: ")
        for statement in self.statements_list:
            if (statement.year == input_year):
                statement_month = int(statement.month)
                if (0 < statement_month <= 3):
                    q1_total += statement.monthly_change()
                elif (4 <= statement_month <= 6):
                    q2_total += statement.monthly_change()
                elif (7 <= statement_month <= 9):
                    q3_total += statement.monthly_change()
                elif (10 <= statement_month <= 12):
                    q4_total += statement.monthly_change()
        print(f"\nQ1 Total: ${q1_total}\nQ2 Total: ${q2_total}" +
              f"\nQ3 Total: ${q3_total}\nQ4 Total: ${q4_total}")

    # Compare two statements
    def statement_comparison(self):
        first_statement = 0
        second_statement = 0
        first_month = input("First statement month: ")
        first_year = input("First statement year: ")
        second_month = input("Second statement month: ")
        second_year = input("Second statement year: ")
        for statement in self.statements_list:
            if statement.month == first_month and statement.year == first_year:
                first_statement = statement.monthly_change()
            elif statement.month == second_month and statement.year == second_year:
                second_statement = statement.monthly_change()
        difference = first_statement - second_statement
        print(
            f"\nGain/loss for {first_month}/{first_year} is ${first_statement}\n" +
            f"Gain/loss for {second_month}/{second_year} is ${second_statement}\n" +
            f"The difference between the two statements is ${difference}")

    # Reset statements_list
    def erase_statements(self):
        self.statements_list = []
