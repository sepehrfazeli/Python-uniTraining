from sheet6.task2.credit_cards import CreditCard


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr  # annual percentage rate

    def process_month(self):
        """Monthly interest on outstanding balance"""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor

    def charge(self, price):
        """ charge a given price to the card """
        success = super().charge(price)
        if not success:
            self._balance += 5  # assess a penalty
        return success
