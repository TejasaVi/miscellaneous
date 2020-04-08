class CreditCard(object):

    def __init__(self):
        self.__bank = ""
        self.__limit = ""
        self._bill_date = ""  # between 1 to 28
        self._bill_due_date = ""
        self.bill_amount = ""

    def get_bill(self):
        return self.bill_amount

    def bill_due_date(self):
        return self._bill_due_date

    def get_billing_date(self):
        return self.billdate

    def get_days_for_bill(self):
        """Get the current date and subtract it from the month to get remainder days for bill """
        return

    def available_credit(self):
        return (self.get_limit() - self.get_bill())

    def get_limit(self):
        return self.__limit
