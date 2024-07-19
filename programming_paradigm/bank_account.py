class BankAccount:
    
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0

    def deposit(self, amount):
        if amount >= 0:
            self.initial_balance += amount
            self.account_balance += self.initial_balance
        else:
            print("you can't deduct with this function")

    def withdraw(self, amount):
        if self.account_balance > 0:
            self.account_balance -= amount
        else:
            print ("Insufficient funds")

    def display_balance(self, amount):
        print (f"Current Balance: {amount}")