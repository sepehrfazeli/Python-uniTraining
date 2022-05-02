class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self._limit = limit
        self._balance = 0

    def get_balance(self):
        return self._balance

    def get_limit(self):
        return self._limit

    def set_limit(self, limit):
        self._limit = limit

    def charge(self, price):
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount
