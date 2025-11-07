""" Day 13: Advanced OOP - Inheritance & Polymorphism """

# Practice Exercise 3: Bank Account Hierarchy

class BankAccount:      # Mum
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):          # Daughter
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def deposit(self, amount):
        return super().deposit(amount)
    
    def get_balance(self):
        return super().get_balance()
    
class CheckingAccount(BankAccount):     # Son
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        print(f"Deposited ${amount}")
        return super().deposit(amount)
    
    def get_balance(self):
        return super().get_balance()
    
save = SavingsAccount("Claude", 1000000, 0.7)
check = CheckingAccount("Me", 30000, 1000)

save.deposit(500)
save.add_interest()
print(save.get_balance())

check.deposit(500)
print(check.get_balance())