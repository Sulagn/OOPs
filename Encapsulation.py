class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        # Private attribute
        self.__balance = initial_balance
        self.account_holder = account_holder

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")
        else:
            print("Invalid or insufficient balance!")

    def get_balance(self):
        print(f"Current balance for {self.account_holder}: ₹{self.__balance}")
        return self.__balance
# Create an account
sulagna = BankAccount("Sulagna", 5000)

# Check balance
sulagna.get_balance()

# Deposit and withdraw
sulagna.deposit(2000)
sulagna.withdraw(1000)

# Try accessing private attribute
print(sulagna.__balance)  # ❌ This will give an error!
