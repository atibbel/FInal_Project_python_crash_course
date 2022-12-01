from transaction import Transaction


class MonthlyStatement:
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
        self.month = ''
        self.year = ''
        self.transaction_list = []
        self.transaction_count = 0

    # Add monthly fee on statement creation
    def create_statement(self, month, year):
        self.month = month
        self.year = year
        new_transaction = Transaction()
        monthly_fee = new_transaction.create_transaction(1, -10)
        self.transaction_list.append(monthly_fee)
        self.transaction_count += 1

    # Create new transaction object and add it to transaction_list
    def add_transaction(self, date, amount):
        new_transaction = Transaction()
        complete_transaction = new_transaction.create_transaction(date, amount)
        self.transaction_list.append(complete_transaction)
        self.transaction_count += 1

    # Print each transaction in this MonthlyStatement
    def print_statement(self):
        print(f"\nStatement for {self.month}/{self.year}\n-----------------------")
        for transaction_item in self.transaction_list:
            transaction_item.print_transaction()

    # Sum amount of all transactions in this MonthlyStatement
    def monthly_change(self):
        total = 0
        for transaction in self.transaction_list:
            total += transaction.amount
        return total
