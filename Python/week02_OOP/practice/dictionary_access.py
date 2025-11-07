""" Day 8 Targeted Practice: Practice Set 3: Dictionary Access """

# Exercise 5:

student = {"name": "Alice", "age": 25, "grades": [85, 90, 92]}

# ❌ Wrong - treating dict like a list
name = student[0]
age = student[1]

# ✓ Correct
name = student["name"]
age = student["age"]

# Exercise 6:
students = {
    "S001": {"name": "Alice", "grades": [85, 90, 92]},
    "S002": {"name": "Bob", "grades": [78, 82, 88]}
}

# Get Alice's first grade
# ❌ Wrong
first_grade = students["S001"][0]

# ✓ Correct
first_grade = students["S001"]["grades"][0]

# Exercise 7:
inventory = {
    "P001": {"name": "Laptop", "price": 999.99},
    "P002": {"name": "Mouse", "price": 25.50}
}

# Get the Mouse's price
# Write it in one line
price = inventory["P002"]["price"]