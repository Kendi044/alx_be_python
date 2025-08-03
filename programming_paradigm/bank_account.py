# In bank_account.py
class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        _account_balance (float): The current balance of the account.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional starting balance.

        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.0.
        """
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        # The 'return' statement MUST be indented to be part of this method
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            # Here, we only return False without a print statement
         return False

    def display_balance(self):
        """
        Displays the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")