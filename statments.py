
class Statement:
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

    def print_all_statements(self, monthly_statement_list):
        pass

    def print_statement(self, monthlyStatement):
        pass