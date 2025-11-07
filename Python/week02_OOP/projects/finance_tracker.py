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
        self.budgets = {}
    
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
            data = {"transactions": [t.to_dict() for t in self.transactions], "budgets": self.budgets}
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)    # indent=2 makes the JSON file more readable
            return True
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
                for item in data.get("transactions", []):
                    t = Transaction(item["date"], item["type"], item["amount"], item["category"], item["description"])
                    self.transactions.append(t)
                self.budgets = data.get("budgets", {})
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
    
    def set_budget(self, category, amount):
        """Set budget for a category"""
        self.budgets[category] = amount
        return True

    def get_budget_status(self):
        """Get spending vs budget for all categories with budgets"""
        status = {}
        for category, budget in self.budgets.items():
            spent = sum(t.amount for t in self.transactions if t.type == "expense" and t.category == category)
            remaining = budget - spent
            percentage = (spent / budget * 100) if budget > 0 else 0
            status[category] = {
                "budget": budget,
                "spent": spent,
                "remaining": remaining,
                "percentage": percentage
            }
        return status
    
    def remove_budget(self, category):
        """Remove budget for a category"""
        if category in self.budgets:
            del self.budgets[category]
            return True
        return False
    
    def get_transactions_by_date_range(self, start_date, end_date):
        """Get transactions between start_date and end_date (inclusive)"""
        return [t for t in self.transactions if start_date <= t.date <= end_date]
    
    def export_to_csv(self, filename):
        """Export all transactions to CSV file"""
        try:
            import csv
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                # Write header
                writer.writerow(['Date', 'Type', 'Amount', 'Category', 'Description'])
                # Write transactions
                for t in self.transactions:
                    writer.writerow([t.date, t.type, t.amount, t.category, t.description])
            return True
        except Exception as e:
            print(f"Error exporting: {e}")
            return False
        
    def get_monthly_report(self):
        """Group transactions by month and calculate totals"""
        from collections import defaultdict
    
        monthly_data = defaultdict(lambda: {"income": 0, "expenses": 0, "transactions": []})
    
        for t in self.transactions:
            # Extract year-month (e.g., "2025-10" from "2025-10-23")
            month = t.date[:7]  # Gets "YYYY-MM"
            monthly_data[month]["transactions"].append(t)
        
            if t.type == "income":
                monthly_data[month]["income"] += t.amount
            else:
                monthly_data[month]["expenses"] += t.amount
    
        return dict(monthly_data)
        
def display_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View by Category")
    print("5. View Summary")
    print("6. Delete Transaction")
    print("7. Edit Transaction")
    print("8. Date Range Filter")
    print("9. Export to CSV")
    print("10. Set Budget")
    print("11. Remove Budget")
    print("12. View Budget Status")
    print("13. View Monthly Report")
    print("14. Save & Exit")
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

def pause():
    """Pause and wait for user to press Enter"""
    input("\nPress Enter to continue...")

def main():
    tracker = FinanceTracker()
    filename = "finances.json"
    
    # Try to load existing data
    print("Loading existing data...")
    tracker.load_from_file(filename)
    
    while True:
        display_menu()
        choice = input("\nEnter choice (1-14): ").strip()
        
        if choice == "1":  # Add Income
            category = input("Category (e.g., Salary, Freelance): ")
            amount = get_valid_amount()
            description = input("Description: ")
            date = get_date()
            tracker.add_transaction(date, "income", amount, category, description)
            print(f"✓ Income of ${amount:.2f} added!")
            pause()
        
        elif choice == "2":  # Add Expense
            category = input("Category (e.g., Food, Transport, Bills): ")
            amount = get_valid_amount()
            description = input("Description: ")
            date = get_date()
            tracker.add_transaction(date, "expense", amount, category, description)
            print(f"✓ Expense of ${amount:.2f} added!")
            pause()
        
        elif choice == "3":  # View All Transactions
            if not tracker.transactions:
                print("No transactions yet!")
            else:
                print("\n=== All Transactions ===")
                for t in tracker.transactions:
                    type_symbol = "+" if t.type == "income" else "-"
                    print(f"{t.date} | {type_symbol}${t.amount:.2f} | {t.category} | {t.description}")
            pause()
        
        elif choice == "4":  # View by Category
            while True:
                category = input("Enter category(or 'b' to go back to main meanu): ")
                if category.lower() == 'b':
                    break
                transactions = tracker.get_transactions_by_category(category)
                if not transactions:
                    print(f"No transactions in category '{category}'. Try again.")
                    continue
                else:
                    print(f"\n=== {category} Transactions ===")
                    for t in transactions:
                        type_symbol = "+" if t.type == "income" else "-"
                        print(f"{t.date} | {type_symbol}${t.amount:.2f} | {t.description}")
                    pause()
                    break
        
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
            pause()
        
        elif choice == "6":  # Delete Transaction
            if not tracker.transactions:
                print("No transactions to delete!")
                pause()
                continue
            while True:
                print("\n=== All Transactions ===")
                for index, t in enumerate(tracker.transactions):
                    type_symbol = "+" if t.type == "income" else "-"
                    print(f"{index}. {t.date} | {type_symbol}${t.amount:.2f} | {t.category} | {t.description}")
                user_input = input("\nEnter index to delete (or 'b' to go back)")
                if user_input.lower() == 'b':
                    break
                try:
                    index = int(user_input)
                    deleted = tracker.delete_transaction(index)
                    if deleted:
                        print(f"✓ Deleted transaction: {deleted.get_info()}")
                        pause()
                        break
                    else:
                        print("Invalid index! Try again.")
                        continue
                except ValueError:
                    print("Please enter a valid number or 'b' to go back.")
                    continue

        elif choice == "7":  # Edit Transaction
            if not tracker.transactions:
                print("No transactions to edit!")
                pause()
                continue
    
            while True:
                print("\n=== All Transactions ===")
                for i, t in enumerate(tracker.transactions):
                    type_symbol = "+" if t.type == "income" else "-"
                    print(f"{i}. {t.date} | {type_symbol}${t.amount:.2f} | {t.category} | {t.description}")
        
                user_input = input("\nEnter index to edit (or 'b' to go back): ")
        
                if user_input.lower() == 'b':
                    break
        
                try:
                    index = int(user_input)
            
                    # Check if valid index
                    if index < 0 or index >= len(tracker.transactions):
                        print("Invalid index! Try again.")
                        continue
            
                    # Get new values
                    date = input("New date (YYYY-MM-DD) or press Enter to skip: ")
                    date = date.strip() or None
                    type = input("New type (income/expense) or press Enter to skip: ")
                    type = type.strip() or None
                    amount_input = input("New amount or press Enter to skip: ")
                    amount = float(amount_input) if amount_input else None
                    category = input("New category or press Enter to skip: ")
                    category = category.strip() or None
                    description = input("New description or press Enter to skip: ")
                    description = description.strip() or None
            
                    if tracker.edit_transaction(index, date, type, amount, category, description):
                        print("✓ Transaction updated successfully!")
                        pause()
                        break
                    else:
                        print("Update failed! Try again.")
                        continue
                
                except ValueError:
                    print("Please enter a valid number or 'b' to go back.")
                    continue

        elif choice == "8":  # Date Range Filter
            if not tracker.transactions:
                print("No transactions yet!")
                continue
    
            print("\nEnter date range (YYYY-MM-DD format)")
            start_date = input("Start date: ")
            end_date = input("End date: ")
    
            transactions = tracker.get_transactions_by_date_range(start_date, end_date)
    
            if not transactions:
                print(f"No transactions between {start_date} and {end_date}")
            else:
                print(f"\n=== Transactions from {start_date} to {end_date} ===")
                for t in transactions:
                    type_symbol = "+" if t.type == "income" else "-"
                    print(f"{t.date} | {type_symbol}${t.amount:.2f} | {t.category} | {t.description}")
        
            # Show totals for this period
            income = sum(t.amount for t in transactions if t.type == "income")
            expenses = sum(t.amount for t in transactions if t.type == "expense")
            print(f"\nPeriod Income: ${income:.2f}")
            print(f"Period Expenses: ${expenses:.2f}")
            print(f"Period Balance: ${income - expenses:.2f}")
            pause()

        elif choice == "9":  # Export to CSV
            if not tracker.transactions:
                print("No transactions to export!")
                continue
    
            filename = input("Enter filename (e.g., transactions.csv): ")
            if not filename.endswith('.csv'):
                filename += '.csv'
    
            if tracker.export_to_csv(filename):
                print(f"✓ Exported to {filename}")
            else:
                print("Export failed!")
            pause()

        elif choice == "10":  # Set Budget
            category = input("Enter category: ")
            try:
                amount = float(input("Enter budget amount: $"))
                if amount <= 0:
                    print("Budget must be positive!")
                    continue
                tracker.set_budget(category, amount)
                print(f"✓ Budget of ${amount:.2f} set for {category}")
            except ValueError:
                print("Invalid amount!")
            pause()

        elif choice == "11":  # Remove Budget
            if not tracker.budgets:
                print("No budgets set!")
                pause()
                continue
    
            print("\n=== Current Budgets ===")
            for category, amount in tracker.budgets.items():
                print(f"{category}: ${amount:.2f}")
    
            category = input("\nEnter category to remove budget (or 'b' to go back): ")
    
            if category.lower() == 'b':
                continue
    
            if tracker.remove_budget(category):
                print(f"✓ Budget removed for {category}")
            else:
                print(f"No budget found for {category}")
    
            pause()

        elif choice == "12":  # View Budget Status
            status = tracker.get_budget_status()
            if not status:
                print("No budgets set!")
            else:
                print("\n=== Budget Status ===")
                for category, info in status.items():
                    print(f"\n{category}:")
                    print(f"  Budget:    ${info['budget']:.2f}")
                    print(f"  Spent:     ${info['spent']:.2f}")
                    print(f"  Remaining: ${info['remaining']:.2f}")
                    print(f"  Used:      {info['percentage']:.1f}%")
            
                    if info['remaining'] < 0:
                        print(f"  ⚠ OVER BUDGET by ${abs(info['remaining']):.2f}!")
                    elif info['percentage'] > 80:
                        print(f"  ⚠ Warning: {info['percentage']:.1f}% of budget used")
            pause()

        elif choice == "13":  # Monthly Report
            report = tracker.get_monthly_report()
    
            if not report:
                print("No transactions yet!")
            else:
                print("\n=== Monthly Report ===")
        
                # Sort by month
                for month in sorted(report.keys()):
                    data = report[month]
                    balance = data["income"] - data["expenses"]
            
                    print(f"\n{month}:")
                    print(f"  Income:   ${data['income']:.2f}")
                    print(f"  Expenses: ${data['expenses']:.2f}")
                    print(f"  Balance:  ${balance:.2f}")
                    print(f"  Transactions: {len(data['transactions'])}")
            
                    if balance > 0:
                        print(f"  ✓ Positive month")
                    elif balance < 0:
                        print(f"  ⚠ Negative month")
            pause()

        elif choice == "14":  # Save & Exit
            print("Saving data...")
            if tracker.save_to_file(filename):
                print("✓ Data saved successfully!")
            print("Goodbye!")
            pause()
            break
        
        else:
            print("Invalid choice! Please enter 1-14.")

# Run the program
if __name__ == "__main__":
    main()