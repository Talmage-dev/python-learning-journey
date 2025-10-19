# Day 12: Finance Tracker Enhancements Reference

## Date: October 24, 2025

---

## Enhancements Added

### 1. Delete Transaction

**Method:**
```python
def delete_transaction(self, index):
    """Delete transaction by index"""
    if 0 <= index < len(self.transactions):
        deleted = self.transactions.pop(index)
        return deleted
    return None

Usage Pattern:
# Show transactions with index numbers
for i, t in enumerate(transactions):
    print(f"{i}. {t.description}")

# Get user choice
index = int(input("Enter index: "))
deleted = tracker.delete_transaction(index)

Key Concept: enumerate() gives both index and item when looping

2. Edit Transaction:
def edit_transaction(self, index, date=None, type=None, amount=None, 
                     category=None, description=None):
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

Usage Pattern:
# Get new values (or None if skipped)
date = input("New date or Enter to skip: ")
date = date.strip() or None

# Update only provided fields
tracker.edit_transaction(index, date=date, amount=amount)

Key Concept: Optional parameters with default None all partial updates

3. Date Range Finder:
def get_transactions_by_date_range(self, start_date, end_date):
    """Get transactions between dates (inclusive)"""
    return [t for t in self.transactions 
            if start_date <= t.date <= end_date]

Usage Pattern:
start = input("Start date (YYYY-MM-DD): ")
end = input("End date (YYYY-MM-DD): ")

transactions = tracker.get_transactions_by_date_range(start, end)

# Calculate period totals
income = sum(t.amount for t in transactions if t.type == "income")
expenses = sum(t.amount for t in transactions if t.type == "expense")

Key Concept: String comparison works for ISO date format(YYYY-MM-DD)

4. Export to CSV:
def export_to_csv(self, filename):
    """Export all transactions to CSV file"""
    try:
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Type', 'Amount', 'Category', 'Description'])
            for t in self.transactions:
                writer.writerow([t.date, t.type, t.amount, t.category, t.description])
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

Key Concepts: 
- csv.writer() for writing to CSV files
- writerow() for header and each data row
- newline=='' prevents extra blank lines

5. Budget Tracking:

Data Structure:
def __init__(self):
    self.transactions = []
    self.budgets = {}  # {category: budget_amount}

Method:
def set_budget(self, category, amount):
    """Set budget for a category"""
    self.budgets[category] = amount
    return True

def remove_budget(self, category):
    """Remove budget for a category"""
    if category in self.budgets:
        del self.budgets[category]
        return True
    return False

def get_budget_status(self):
    """Get spending vs budget for all categories"""
    status = {}
    for category, budget in self.budgets.items():
        spent = sum(t.amount for t in self.transactions 
                   if t.type == "expense" and t.category == category)
        remaining = budget - spent
        percentage = (spent / budget * 100) if budget > 0 else 0
        status[category] = {
            "budget": budget,
            "spent": spent,
            "remaining": remaining,
            "percentage": percentage
        }
    return status

Key Concepts:
- Seperate dictionary budgets
- Calculate spending per category
- Show percentage and remaining amount
- Warn when over budget

6. Monthly Reports
def get_monthly_report(self):
    """Group transactions by month"""
    from collections import defaultdict
    
    monthly_data = defaultdict(lambda: {
        "income": 0, 
        "expenses": 0, 
        "transactions": []
    })
    
    for t in self.transactions:
        month = t.date[:7]  # Extract "YYYY-MM"
        monthly_data[month]["transactions"].append(t)
        
        if t.type == "income":
            monthly_data[month]["income"] += t.amount
        else:
            monthly_data[month]["expenses"] += t.amount
    
    return dict(monthly_data)

Key Concepts:
- defaultdict for automatic initialization
- String slicing to exact month: "2025-10-23"[:7] -> "2025-10"
- Group and aggregate by period

- - -

User Experience Improvements

1. Pause After Display:

Helper Function:
def pause():
    """Wait for user to press Enter"""
    input("\nPress Enter to continue...")

Usage:
# After displaying information
print("=== Summary ===")
print(f"Total: ${total}")
pause()  # Wait before returning to menu

- - -

2. Retry Loops for Invalid Input

Pattern:
while True:
    user_input = input("Enter choice (or 'b' to go back): ")
    
    if user_input.lower() == 'b':
        break  # Exit to main menu
    
    try:
        # Process input
        if valid:
            # Success - exit loop
            break
        else:
            print("Invalid! Try again.")
            continue  # Ask again
    except ValueError:
        print("Invalid input!")
        continue  # Ask again

Key Concepts:
- Loop until valid input or user cancels
- Allow 'b' to go back
- Clear error messages
- Better user experience

- - -

3. Persistent Data with Budgets

Updated Save Format:
def save_to_file(self, filename):
    data = {
        "transactions": [t.to_dict() for t in self.transactions],
        "budgets": self.budgets
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

Updated Load:
def load_from_file(self, filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        
        # Load transactions
        self.transactions = []
        for item in data.get("transactions", []):
            t = Transaction(...)
            self.transactions.append(t)
        
        # Load budgets
        self.budgets = data.get("budgets", {})

Key Concepts:
- Save multiple data types in one JSON file
- Use .get() with defaults for backward compatibility
- Structured data format

- - -

Common Patterns Used

enumerate() for Index + Item:

for index, item in enumerate(collection):
    print(f"{index}. {item}")

Similar to:
- Dictionary: for key, value in dict.items()
- Lists: for index, item in enumerate(list)

- - - 
Optional Parameters

def edit(index, field1=None, field2=None):
    if field1: obj.field1 = field1
    if field2: obj.field2 = field2

Allows partial updates

- - -

String Slicing for Dates

date = "2025-10-23"
year_month = date[:7]   # "2025-10"
year = date[:4]         # "2025"
month = date[5:7]       # "10"
day = date[8:10]        # "23"

- - -

Comprehension with Mulitple Conditions

# Filter by type AND category
expenses = [t for t in transactions if t.type == "expense" and t.category == "Food"]

# Sum with condition
total = sum(t.amount for t in transactions if t.type == "income")

- - -

defaultdict for Auto-initialization

from collections import defaultdict

# Instead of checking if key exists
data = defaultdict(list)
data["key"].append(item)  # Works even if "key" doesn't exist

# With lambda for complex defaults
data = defaultdict(lambda: {"count": 0, "total": 0})
data["key"]["count"] += 1

- - - 

Complete Feature List

Core Features:

1. ✅ Add income/expenses
2. ✅ View all transactions
3. ✅ Filter by category
4. ✅ Financial summary
5. ✅ Save/load (JSON)

Advanced Features:

6. ✅ Delete transactions
7. ✅ Edit transactions
8. ✅ Date range filter
9. ✅ Export to CSV
10. ✅ Set budgets
11. ✅ Remove budgets
12. ✅ View budget status
13. ✅ Monthly reports

UX Features:

14. ✅ Pause after displays
15. ✅ Retry loops
16. ✅ 'b' to go back
17. ✅ Input validation
18. ✅ Clear error messages

- - -

Testing Checklist

✅ Add transactions (income & expense)
✅ View all transactions
✅ Filter by category (valid & invalid)
✅ View summary
✅ Delete transaction (valid & invalid index)
✅ Edit transaction (partial & full edit)
✅ Date range filter
✅ Export to CSV
✅ Set budget
✅ View budget status (under & over budget)
✅ Remove budget
✅ Monthly report
✅ Save & exit
✅ Load on restart
✅ Handle invalid inputs gracefully

- - -

Key Learnings

1. enumerate() vs range(len())
# Harder to read
for i in range(len(items)):
    print(f"{i}. {items[i]}")

# Cleaner
for i, item in enumerate(items):
    print(f"{i}. {item}")

2. Optional Parameters for Flexibility
# Allows updating only specific fields
edit_transaction(index, amount=100)  # Only update amount
edit_transaction(index, category="Food", description="Lunch")  # Update multiple

3. Data Aggregation Patterns
# Group by category
by_category = {}
for t in transactions:
    if t.category not in by_category:
        by_category[t.category] = []
    by_category[t.category].append(t)

# Or with defaultdict
from collections import defaultdict
by_category = defaultdict(list)
for t in transactions:
    by_category[t.category].append(t)

4. User Experience Matters

- Clear error messages
- Allow going back
- Confirm actions
- Show progress
- Pause before clearing screen

- - -

End of Day 12 Reference

- - -