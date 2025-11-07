""" Day 10: Object-Oriented Programming (OOP) - Part 1 """

# Pattern 5: Class Variables vs Instance Variables

# The Pattern:
# class ClassName:
#     class_variable = value                  # Shared by ALL objects

#     def __init__(self,param):
#         self.instance_variable = param      # Unique to each object

# Example: Bank Account with Account Counter
class BankAccount:
    total_accounts = 0  # CLASS VARIABLE - shared by all accounts
    
    def __init__(self, owner, balance):
        self.owner = owner      # INSTANCE VARIABLE - unique to each account
        self.balance = balance  # INSTANCE VARIABLE - unique to each account
        BankAccount.total_accounts += 1  # Increment class variable
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

# Create accounts
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)
acc3 = BankAccount("Charlie", 1500)

# Instance variables are different
print(acc1.owner)    # "Alice"
print(acc2.owner)    # "Bob"

# Class variable is shared
print(BankAccount.total_accounts)  # 3
print(acc1.total_accounts)         # 3 (same!)
print(acc2.total_accounts)         # 3 (same!)

# Practice Exercise 5: Student with ID Counter

class Student:
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1

    def get_info(self):
        return f"{self.name}: Grade {self.grade}"
    
    @classmethod
    def get_total_students(cls):
        return cls.total_students
    
s1 = Student("Alice", 85)
s2 = Student("Bob", 92)
s3 = Student("Charlie", 78)

print(s1.get_info())
print(f"Total students: {Student.get_total_students()}")