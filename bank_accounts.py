"""
Bank Account Management System

This program defines a simple banking system with different types of accounts. It allows users to:
- Create bank accounts.
- Deposit and withdraw money.
- Transfer money between accounts.
- Handle insufficient balance cases using custom exceptions.
- Implement interest rewards for deposits.
- Introduce savings accounts with withdrawal fees.

Classes:
1. `BalanceException`: Custom exception for handling insufficient balance.
2. `BankAccount`: Base class for a general bank account.
3. `InterestRewardsAccount`: Inherits from `BankAccount` and adds a 5% interest on deposits.
4. `SavingsAccount`: Inherits from `InterestRewardsAccount` and introduces a withdrawal fee.

"""

# Custom exception for handling insufficient balance cases
class BalanceException(Exception):
    pass

# Base class for a general bank account
class BankAccount:
    """
    Represents a bank account with basic operations: deposit, withdraw, and transfer.
    """
    def __init__(self, initial_amount, account_name):
        """
        Initializes the bank account with an initial balance and name.

        :param initial_amount: The starting balance for the account.
        :param account_name: The name of the account holder.
        """
        self.balance = initial_amount  # Store initial balance
        self.name = account_name  # Store account name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        """
        Prints the current balance of the account.
        """
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        :param amount: The amount to deposit.
        """
        self.balance += amount  # Increase balance
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        """
        Checks if there are sufficient funds to complete a transaction.

        :param amount: The amount to be withdrawn or transferred.
        :raises BalanceException: If the balance is insufficient.
        """
        if self.balance >= amount:
            return  # Transaction is allowed
        else:
            # Raise an exception if the balance is too low
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account, if possible.

        :param amount: The amount to withdraw.
        """
        try:
            self.viable_transaction(amount)  # Check if withdrawal is possible
            self.balance -= amount  # Deduct amount
            print("\nWithdrawal complete!")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: {error}")  # Handle insufficient balance

    def transfer(self, amount, account):
        """
        Transfers a specified amount from this account to another account.

        :param amount: The amount to transfer.
        :param account: The destination account.
        """
        try:
            print("\n**********\n\nBeginning Transfer...🚀")
            self.viable_transaction(amount)  # Check if transfer is possible
            self.withdraw(amount)  # Withdraw from sender account
            account.deposit(amount)  # Deposit into receiver account
            print("\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")  # Handle insufficient balance


# Subclass that rewards deposits with interest
class InterestRewardsAccount(BankAccount):
    """
    A bank account that rewards deposits with a 5% bonus.
    """
    def deposit(self, amount):
        """
        Deposits an amount with an added 5% interest.

        :param amount: The amount to deposit.
        """
        self.balance += amount * 1.05  # Add 5% interest
        print("\nDeposit complete (with interest bonus).")
        self.get_balance()


# Subclass that adds a withdrawal fee
class SavingsAccount(InterestRewardsAccount):
    """
    A bank account with deposit rewards and a withdrawal fee.
    """
    def __init__(self, initial_amount, account_name):
        """
        Initializes a savings account with a withdrawal fee.

        :param initial_amount: The starting balance.
        :param account_name: The account holder's name.
        """
        super().__init__(initial_amount, account_name)  # Call parent constructor
        self.fee = 5  # Set withdrawal fee

    def withdraw(self, amount):
        """
        Withdraws an amount with an additional fixed fee.

        :param amount: The amount to withdraw.
        """
        try:
            total_deduction = amount + self.fee  # Calculate total amount with fee
            self.viable_transaction(total_deduction)  # Check if withdrawal is possible
            self.balance -= total_deduction  # Deduct amount including fee
            print("\nWithdrawal complete (including fee).")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: {error}")  # Handle insufficient balance