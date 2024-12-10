# Base Class
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")


# Derived Class for Savings Account
class SavingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest on account balance: ${interest}")
        return interest


# Example Usage
def main():
    # Create a SavingAccount
    savings = SavingAccount("SA123", "John Doe", 1000, 0.05)

    # Display balance
    savings.display_balance()

    # Deposit money
    savings.deposit(500)

    # Withdraw money
    savings.withdraw(200)

    # Calculate interest
    interest = savings.calculate_interest()

    # Display final balance
    savings.display_balance()


if __name__ == "__main__":
    main()

