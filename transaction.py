class Transaction:

    def __init__(self):
        self.date = ''
        self.amount = 0

    # Apply passed-in date and amount to Transaction object
    def create_transaction(self, date, amount):
        if (date > 0 and date <= 31):
            self.date = int(date)
            self.amount = int(amount)
        else:
            print("Date not acceptable. Please enter a date between 1 and 31.")
        return self

    def print_transaction(self):
        print(f"Day: {self.date} Amount: ${self.amount}")
