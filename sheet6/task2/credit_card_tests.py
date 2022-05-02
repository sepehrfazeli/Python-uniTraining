from sheet6.task2.credit_cards import CreditCard
from colorama import Fore

wallet = [CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500),
          CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500),
          CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000)]

for val in range(1, 59):
    if not wallet[0].charge(val):
        print(Fore.RED + 'exceed limit' + Fore.RESET)
        break
    if not wallet[1].charge(2 * val):
        print(Fore.RED + 'exceed limit' + Fore.RESET)
        break
    if not wallet[2].charge(3 * val):
        print(Fore.RED + 'exceed limit' + Fore.RESET)
        break

for c in range(3):
    print("Customer = ", wallet[c].customer)
    print("Bank = ", wallet[c].bank)
    print("Account = ", wallet[c].account)
    print("Limit = ", wallet[c].get_limit())
    print("Balance = ", wallet[c].get_balance())

    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print("New balance = ", wallet[c].get_balance())
    print()
