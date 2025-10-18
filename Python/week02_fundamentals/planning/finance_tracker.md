""" Day 11: Comprehensive Practice Project - Finance Tracker """

# Features:
    1) Add transactions (income/expense)
    2) View all transactions
    3) View by category (food, transport, salary, etc.)
    4) Monthly summary (total income, expense, balance)
    5) Save to file (persistent storage)
    6) Load from file (reume previous session)
    7) Generate reports (spending by ctegory)

# Step 1: Plan the Transaction Class
    1) create class
    2) init method with (date, type, category, amount, descripton)
            self.date = date
            ....
            ....
    3) get_info(self) method
            return f"{date} ......
    4) to_dict(self)
            return tran_dic = {"date": self.date, ......}
    
# Step 2: Plan the FinanceTracker Class
    1) create an empty transactions list
    2) init method
            Initialize empty list       # self.transactions = []
    3) add_transaction(date, type, amount, category, description)
            transaction = Transaction()
            self.transactions.append(transaction)      # Add object
    4) get_all_transactions(self)
            return transactions list
    5) get_transactions_by_category(self, category)
            return [t for t in self.transactions if t.category == category]
    6) get_total_income(self)
            return sum(t.amount for t in self.transactions if t.type == "income")
    7) get_total_expenses(self)
            return sum(t.amount for t in self.transactions if t.type == "expense")
    8) get_balance(self)
            return get_total_income() - get_total_expenses()
    9) save_to_file(self, filename)
            data = [t.to_dict90 for t in selftransactions]  # list of dicts
            with open(...., "w") as f:
                json.dump(data, f)      # Save entire list at once
    10) load_from_file(self, filename):
            with open(filename, "r") as f:
                data = json.load(f)  # Load entire list
                for item in data:
                    # Create Transaction object from dict
                    t = Transaction(item["date"], item["type"], item["amount"], item["category"], item["description"])
                    self.transactions.append(t)