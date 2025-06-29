class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def account_summary(self):
        print("Account Summary:")
        print(f"Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        self.check_balance()

# Example usage
if __name__ == "__main__":
    acc1 = BankAccount("1234567890", "Vadivelan")

    acc1.account_summary()
    acc1.deposit(5000)
    acc1.withdraw(1200)
    acc1.check_balance()