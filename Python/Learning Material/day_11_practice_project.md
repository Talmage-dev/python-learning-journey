# Day 11: Comprehensive Practice Project Reference

## Date: October 23, 2025

---

## Project: Personal Finance Tracker

A complete finance management system combining all concepts from Days 1-10.

---

## Project Structure

### Classes

#### Transaction Class
```python
class Transaction:
    def __init__(self, date, type, amount, category, description):
        self.date = date
        self.type = type  # "income" or "expense"
        self.amount = amount
        self.category = category
        self.description = description
    
    def get_info(self):
        return f"Transaction(amount={self.amount}, category='{self.category}', description='{self.description}')"
    
    def to_dict(self):
        return {
            "date": self.date,
            "type": self.type,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

Purpose: Represents a single financial transaction

Key Methods:

get_info() - Returns formatted string
to_dict() - Converts to dictionary for JSON storage

- - -

# FinanceTracker Class
class FinanceTracker:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, date, type, amount, category, description):
        transaction = Transaction(date, type, amount, category, description)
        self.transactions.append(transaction)
    
    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.type == "income")
    
    def get_total_expenses(self):
        return sum(t.amount for t in self.transactions if t.type == "expense")
    
    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()
    
    def get_transactions_by_category(self, category):
        return [t for t in self.transactions if t.category == category]
    
    def save_to_file(self, filename):
        try:
            data = [t.to_dict() for t in self.transactions]
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except PermissionError:
            print(f"Error: No permission to write to {filename}")
            return False
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.transactions = []
                for item in data:
                    t = Transaction(item["date"], item["type"], item["amount"],
                                  item["category"], item["description"])
                    self.transactions.append(t)
            return True
        except FileNotFoundError:
            print("No existing file found. Starting fresh.")
            return False
        except json.JSONDecodeError:
            print("Error: File is corrupted")
            return False
        except Exception as e:
            print(f"Error loading file: {e}")
            return False
    
    def delete_transaction(self, index):
        """Delete transaction by index"""
        if 0 <= index < len(self.transactions):
            deleted = self.transactions.pop(index)
            return deleted
        return None

Purpose: Manages all transactions

Key Methods:
    add_transaction() - Create and adds new transaction
    get_total_income() - Sums all income
    get_total_expenses() - Sums all expenses
    get_balance() - Calculates net balance
    get_transactions_by_category() - Filters by category
    save_to_file() - Persists to JSON with error handling
    load_from_file() - Loads from JSON with error handling
    delete_transaction() - Removes transaction by index

- - -

Helper Functions

# Display Menu:
def display_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View by Category")
    print("5. View Summary")
    print("6. Save & Exit")
    print("7. Delete Transaction")
    print("================================")

# Get Current Date:
def get_date():
    """Get current date in YYYY-MM-DD format"""
    from datetime import date
    return str(date.today())

# Validate Amount Input:
def get_valid_amount():
    """Get valid amount from user with error handling"""
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("Amount must be positive!")
                continue
            return amount
        except ValueError:
            print("Invalid amount! Please enter a number.")

Key Pattern: Input validation with loop + try/except

# Main Program Loop:
def main():
    tracker = FinanceTracker()
    filename = "finances.json"
    
    # Load existing data
    print("Loading existing data...")
    tracker.load_from_file(filename)
    
    while True:
        display_menu()
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == "1":  # Add Income
            category = input("Category (e.g., Salary, Freelance): ")
            amount = get_valid_amount()
            description = input("Description: ")
            date = get_date()
            tracker.add_transaction(date, "income", amount, category, description)
            print(f"✓ Income of ${amount:.2f} added!")
        
        elif choice == "2":  # Add Expense
            category = input("Category (e.g., Food, Transport): ")
            amount = get_valid_amount()
            description = input("Description: ")
            date = get_date()
            tracker.add_transaction(date, "expense", amount, category, description)
            print(f"✓ Expense of ${amount:.2f} added!")
        
        elif choice == "3":  # View All
            if not tracker.transactions:
                print("No transactions yet!")
            else:
                print("\n=== All Transactions ===")
                for i, t in enumerate(tracker.transactions):
                    type_symbol = "+" if t.type == "income" else "-"
                    print(f"{i}. {t.date} | {type_symbol}${t.amount:.2f} | {t.category} | {t.description}")
        
        elif choice == "4":  # View by Category
            category = input("Enter category: ")
            transactions = tracker.get_transactions_by_category(category)
            if not transactions:
                print(f"No transactions in '{category}'")
            else:
                print(f"\n=== {category} Transactions ===")
                for t in transactions:
                    type_symbol = "+" if t.type == "income" else "-"
                    print(f"{t.date} | {type_symbol}${t.amount:.2f} | {t.description}")
        
        elif choice == "5":  # Summary
            income = tracker.get_total_income()
            expenses = tracker.get_total_expenses()
            balance = tracker.get_balance()
            
            print("\n=== Financial Summary ===")
            print(f"Total Income:   ${income:.2f}")
            print(f"Total Expenses: ${expenses:.2f}")
            print(f"Balance:        ${balance:.2f}")
            
            if balance > 0:
                print("✓ You're in the positive!")
            elif balance < 0:
                print("⚠ You're spending more than earning!")
        
        elif choice == "6":  # Save & Exit
            print("Saving data...")
            if tracker.save_to_file(filename):
                print("✓ Data saved successfully!")
            print("Goodbye!")
            break
        
        elif choice == "7":  # Delete Transaction
            if not tracker.transactions:
                print("No transactions to delete!")
            else:
                print("\n=== All Transactions ===")
                for i, t in enumerate(tracker.transactions):
                    print(f"{i}. {t.date} | ${t.amount:.2f} | {t.category}")
                try:
                    index = int(input("\nEnter number to delete: "))
                    deleted = tracker.delete_transaction(index)
                    if deleted:
                        print(f"✓ Deleted: {deleted.get_info()}")
                    else:
                        print("Invalid transaction number!")
                except ValueError:
                    print("Please enter a valid number!")
        
        else:
            print("Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main()

Concepts Applied

OOP (Day 10)

Two classes working together
Instance variables and methods
Object composition (Transaction objects in FinanceTracker)

File I/O (Day 7)
JSON file format
Reading and writing files
Persistent data storage

Error Handling (Day 8)
try/except blocks
Multiple exception types (FileNotFoundError, PermissionError, ValueError)
Graceful error messages

Comprehensions (Day 8)
List comprehensions for filtering
Sum with generator expression

Modules (Day 9)
json module for data serialization
datetime module for timestamps

Dictionaries (Day 6)
to_dict() method for JSON conversion
Dictionary unpacking

Lists (Day 5)
Managing collections of objects
List operations (append, pop)

Functions (Day 4)
Helper functions for organization
Input validation functions

Loops & Conditionals (Day 4)
Main program loop
Menu-driven interface
Input validation loops

- - -

Key Patterns

# Object to Dictionary Conversion:
def to_dict(self):
    return {
        "key1": self.attribute1,
        "key2": self.attribute2
    }

# Dictionary to Object Conversion:
obj = ClassName(dict["key1"], dict["key2"])

Safe File Operations:
try:
    with open(filename, mode) as f:
        # file operations
    return True
except SpecificError:
    print("Error message")
    return False

# Input Validation Loop:
while True:
    try:
        value = type_conversion(input("Prompt: "))
        if validation_check:
            return value
        print("Validation failed message")
    except ValueError:
        print("Invalid input message")

# Filtering with Comprehensions:
filtered = [item for item in collection if condition]

# Summing with Generator Expression:
total = sum(item.value for item in collection if condition)

- - -

Common Mistakes to Avoid

❌ Forgetting to save date in init
❌ Not converting Transaction objects to dicts before JSON
❌ Not converting dicts back to Transaction objects when loading
❌ Modifying list while looping (use pop with index or comprehension)
❌ Not handling empty collections before calculations
❌ Forgetting error handling on file operations
❌ Not validating user input

- - -

Enhancement Ideas

1. Edit Transaction - Modify existing transactions

2. Date Range Filter - View transactions between dates

3. Export to CSV - Generate spreadsheet

4. Budget Tracking - Set and monitor budgets per category

5. Monthly Reports - Group transactions by month

6. Search - Find transactions by description

7. Categories Management - Predefined category list

8. Recurring Transactions - Auto-add monthly bills

- - -

Testing Checklist

✅ Add income transaction
✅ Add expense transaction
✅ View all transactions
✅ View by category
✅ View summary (income, expenses, balance)
✅ Save to file
✅ Load from file (restart program)
✅ Delete transaction
✅ Handle invalid input (letters for amount)
✅ Handle missing file (first run)
✅ Handle corrupted JSON file

- - -

End of Day 11 Reference

- - -
