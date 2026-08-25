class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")


account = BankAccount("Jahirul", 1000)

account.display_balance()

account.deposit(500)

print("\nAfter deposit:")
account.display_balance()

account.withdraw(200)

print("\nAfter withdrawal:")
account.display_balance()