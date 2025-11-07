""" Day 8 Targeted Practice: Practice Set 4: Return Statement Placement """

# Exercise 8:

# fix
def load_students(filename):
    students = {}
    with open(filename, "r") as file:
        for line in file:
            # ... process line ...
            students[student_id] = student_info
        return students  # ❌ Wrong placement!
    
def load_students(filename):
    students = {}
    with open(filename, "r") as file:
        for line in file:
            # ... process line ...
            students[student_id] = student_info
    return students

# Exercise 9:

# Fix
def find_student(students, name):
    for student_id, info in students.items():
        if info["name"] == name:
            return student_id  # ✓ This is correct!
    return None