""" Day 11: Comprehensive Practice Project - Finance Tracker """

import json

class Transaction:
    def __init__(self, date, type, amount, category, description):
        self.date = date
        self.type = type  # 'income' or 'expense'
        self.amount = amount
        self.category = category
        self.description = description

    def get_info(self):
        return f"Transaction(amount={self.amount}, category='{self.category}', description='{self.description}')"
    
    def to_dict(self):
        return {"date": self.date, "type": self.type, "amount": self.amount, "category": self.category, "description": self.description}

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
                json.dump(data, f, indent=2)    # indent=2 makes the JSON file more readable
        except PermissionError:
            print(f"Error: No permission to write to {filename}.")
            return False
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.transactions = []  # Clear existing transactions
                for item in data:
                    t = Transaction(item["date"], item["type"], item["amount"], item["category"], item["description"])
                    self.transactions.append(t)
            return True
        except FileNotFoundError:
            print(f"No existing file found. Starting fresh.")
            return False
        except json.JSONDecodeError:
            print(f"Error: File is corrupted")
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
    
    def edit_transaction(self, index, date=None, type=None, amount=None, category=None, description=None):
        """Edit transaction by index. Only updates provided fields."""
        if 0 <= index < len(self.transactions):
            t = self.transactions[index]
            if date: t.date = date
            if type: t.type = type
            if amount: t.amount = amount
            if category: t.category = category
            if description: t.description = description
            return True
        return False
        
def display_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View by Category")
    print("5. View Summary")
    print("6. Delete Transaction")
    print("7. Edit Transaction")
    print("8. Save & Exit")
    print("================================")

def get_date():
    """Get current date in YYYY-MM-DD format"""
    from datetime import date
    return str(date.today())

def get_valid_amount():
    """Get valid amount from user"""
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("Amount must be positive!")
                continue
            return amount
        except ValueError:
            print("Invalid amount! Please enter a number.")

def main():
    tracker = FinanceTracker()
    filename = "finances.json"
    
    # Try to load existing data
    print("Loading existing data...")
    tracker.load_from_file(filename)
    
    while True:
        display_menu()
        choice = input("\nEnter choice (1-8): ").strip()
        
        if choice == "1":  # Add Income
            category = input("Category (e.g., Salary, Freelance): ")
            amount = get_valid_amount()
            description = input("Description: ")
            date = get_date()
            tracker.add_transaction(date, "income", amount, category, description)
            print(f"✓ Income of ${amount:.2f} added!")
        
        elif choice == "2":  # Add Expense
            category = input("Category (e.g., Food, Transport, Bills): ")
            amount = get_valid_amount()
            description = input("Description: ")
            date = get_date()
            tracker.add_transaction(date, "expense", amount, category, description)
            print(f"✓ Expense of ${amount:.2f} added!")
        
        elif choice == "3":  # View All Transactions
            if not tracker.transactions:
                print("No transactions yet!")
            else:
                print("\n=== All Transactions ===")
                for t in tracker.transactions:
                    type_symbol = "+" if t.type == "income" else "-"
                    print(f"{t.date} | {type_symbol}${t.amount:.2f} | {t.category} | {t.description}")
        
        elif choice == "4":  # View by Category
            category = input("Enter category: ")
            transactions = tracker.get_transactions_by_category(category)
            if not transactions:
                print(f"No transactions in category '{category}'")
            else:
                print(f"\n=== {category} Transactions ===")
                for t in transactions:
                    type_symbol = "+" if t.type == "income" else "-"
                    print(f"{t.date} | {type_symbol}${t.amount:.2f} | {t.description}")
        
        elif choice == "5":  # View Summary
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
            else:
                print("You're breaking even.")
        
        elif choice == "6":  # Delete Transaction
            if not tracker.transactions:
                print("No transactions to delete!")
                continue
            print("\n=== All Transactions ===")
            for index, t in enumerate(tracker.transactions):
                type_symbol = "+" if t.type == "income" else "-"
                print(f"{index}. {t.date} | {type_symbol}${t.amount:.2f} | {t.category} | {t.description}")
            try:
                index = int(input("Enter the index of the transaction to delete: "))
                deleted = tracker.delete_transaction(index)
                if deleted:
                    print(f"✓ Deleted transaction: {deleted.get_info()}")
                else:
                    print("Invalid index!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "7":  # Edit Transaction
            if not tracker.transactions:
                print("No transactions to edit!")
                continue
            print("\n=== All Transactions ===")
            for index, t in enumerate(tracker.transactions):
                type_symbol = "+" if t.type == "income" else "-"
                print(f"{index}. {t.date} | {type_symbol}${t.amount:.2f} | {t.category} | {t.description}")
            try:
                index = int(input("Enter the index of the transaction to edit: "))
                date = input("New date (YYYY-MM-DD) or press Enter to skip: ")
                type = input("New type (income/expense) or press Enter to skip: ")
                amount_input = input("New amount or press Enter to skip: ")
                amount = float(amount_input) if amount_input else None
                category = input("New category or press Enter to skip: ")
                description = input("New description or press Enter to skip: ")
                
                if tracker.edit_transaction(index, date or None, type or None, amount, category or None, description or None):
                    print("✓ Transaction updated successfully!")
                else:
                    print("Invalid index!")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "8":  # Save & Exit
            print("Saving data...")
            if tracker.save_to_file(filename):
                print("✓ Data saved successfully!")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1-6.")

# Run the program
if __name__ == "__main__":
    main()