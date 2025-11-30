class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional starting balance.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add money to the account.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Remove money from the account if sufficient funds exist.
        Returns True if withdrawal succeeds, otherwise False.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current account balance.
        """
        print(f"Current balance: ${self.account_balance}")
