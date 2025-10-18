class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

account = BankAccount(100)    
print(account.get_balance())
