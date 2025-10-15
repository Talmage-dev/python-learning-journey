""" Day 8 Comprehensions """

""" Pattern 5: Dictionary Comprehension with Condition """

# Pratice Exercise 8: Passing students

students = {"Alice": 85, "Bob": 55, "Charlie": 92, "Diana": 48, "Eve": 78}

passing_students = {name: grade for name, grade in students.items() if grade >= 60}