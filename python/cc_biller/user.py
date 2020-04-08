import CreditCard as CreditCard


class User(object):

    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.uid = ""
        self.pan = ""
        self.cards = []

    def addCard(self, card):
        self.cards.append()

    @property
    def credit_limit(self):
        limit = 0
        for card in self.cards:
            limit = limit + card.get_limit()
        return limit

    @property
    def available_credit(self):
        credit = 0
        for card in self.cards:
            credit = credit + card.available_credit()
        return credit
