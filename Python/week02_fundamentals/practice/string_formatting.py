""" Day 8 Targeted Practice: Practice Set 2: String Formatting """

# Exercise 3:

# Fix
name = "Alice"
age = 25

# ❌ Wrong
message = f"My name is name and I am age years old"

# ✓ Correct
message = f"My name is {name} and I am {age} years old"

# Exercise 4:
student_id = "S001"
grades = [85, 90, 92]

# ❌ Wrong - will print the list with brackets
line = f"{student_id},{grades}\n"

# ✓ Correct - need to join the grades first
grades_str = ",".join(str(grade) for grade in grades)
line = f"{student_id},{grades_str}\n"