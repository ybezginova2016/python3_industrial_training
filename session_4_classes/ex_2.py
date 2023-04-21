"""
2. Create a BankAccount class with the following attributes:
balance and account_number.

The class should also have the following methods:
deposit(amount),
withdraw(amount), and info().

account1 = BankAccount(1000.0, 123456789)
account1.deposit(500.0)
account1.withdraw(200.0)
account1.info()  # Output: Account Number: 123456789, Balance: 1300.0

"""
class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

        else:
            print('Insufficient funds')

    def info(self):
        print(f"Account Number: {self.account_number}, "
              f"Balance: {self.balance:.2f}")


 # Example usage
account1 = BankAccount(1000.0, 123456789)
account1.deposit(500.0)
account1.withdraw(200.0)
account1.info()  # Output: Account Number: 123456789, Balance: 1300.00