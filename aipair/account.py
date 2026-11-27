# Account class to store acno, customer, balance and deposit(), withdraw() and getbalance() methods 

class Account:
    """Represent a bank account with a customer and a balance."""

    def __init__(self, acno, customer, balance):
        """Initialize an account.

        Args:
            acno: The account number.
            customer: The account holder's name or details.
            balance: The opening balance.
        """
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        """Add a positive amount to the account balance.

        Args:
            amount: The amount to deposit.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtract an amount from the balance if sufficient funds exist.

        Args:
            amount: The positive amount to withdraw.

        Raises:
            ValueError: If the amount is not positive or exceeds the balance.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount.")

    def getbalance(self):
        """Return the current account balance.

        Returns:
            The current balance.
        """
        return self.balance


    # Test Account class 
if __name__ == "__main__":
    # Create an account
    acc = Account(acno=12345, customer="John Doe", balance=1000)

    # Test deposit
    acc.deposit(500)  # Expected: Deposited 500. New balance is 1500.
    acc.deposit(-100)  # Expected: Deposit amount must be positive.

    # Test withdraw
    acc.withdraw(200)  # Expected: Withdrew 200. New balance is 1300.
    acc.withdraw(2000)  # Expected: Insufficient funds or invalid withdrawal amount.

    # Test getbalance
    print(f"Current balance is {acc.getbalance()}.")  # Expected: Current balance is 1300.

    