""" Day 8 Comprehensions """

# Final Challenge: Combine Everthing.

# Student Report System

students = {
    "S001": {"name": "Alice", "grades": [85, 90, 92]},
    "S002": {"name": "Bob", "grades": [55, 60, 58]},
    "S003": {"name": "Charlie", "grades": [92, 95, 89]},
    "S004": {"name": "Diana", "grades": [78, 82, 80]}
}

# List of all students names (uppercase)
uppercase_names = [name["name"].upper() for student_id, name in students.items()]

# Dictionary of student averages
averages = {student_id: sum(info["grades"])/len(info["grades"]) for student_id, info in students.items()}

# List of passing students (average >= 70)
passing_students =[info["name"] for student_id, info in students.items() if (sum(info["grades"])/len(info["grades"])) >= 70]

# Dictionary of High achievers
high_achievers ={student_id: info for student_id, info in students.items() if (sum(info["grades"])/len(info["grades"])) >= 85}