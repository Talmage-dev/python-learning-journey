""" Day 8 Comprehensions """

""" Pattern 4: Dictionary Comprehension """

# Pratice Exercise 6: Price Dictionary

products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 25.50, 75.00]

inventory = {product: price for product, price in zip(products, prices)}

# Practice Exercise 7: Student Grades Dictionary

students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]

student_grade = {name: grade for name, grade in zip(students, grades)}
