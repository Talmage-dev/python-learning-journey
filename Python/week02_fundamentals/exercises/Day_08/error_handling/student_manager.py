""" Day 8 Error Handling """

# Final Challenge: Robust Student Manager

# Functions
def load_students_safe(filename):
    students = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                student_id = parts[0]
                name = parts[1]
                grades_str = parts[2:]
                grades = [int(score) for score in grades_str]
                student_info = {"name": name, "grades": grades}
                students[student_id] = student_info
        return students
    except FileNotFoundError:
        print("Error: File could not be found!")
        return students

def save_students_safe(students, filename):
    try:
        with open(filename, "w") as file:
            for student_id, student_info in students.items():
                name = student_info["name"]
                grades = student_info["grades"]
                grades_str = ",".join(str(score) for score in grades)
                line = f"{student_id},{name},{grades_str}\n"

                file.write(line)
    except PermissionError:
        print("Error: Cannot write to file!")
        return False
    else:
        return True


def get_student_grade_safe():
    while True:
        try:
            grade = int(input("Enter students grade: "))
            return grade
        except ValueError:
            print("Error: Invalid number")

# Main Program
print("=== Robust Student Manager ===\n")
# Try to load existing file (might not exist)
students = load_students_safe("students.txt")
print(f"Loaded {len(students)} students\n")
# If no students, create some
if not students:
    print("Creating sample students...")
    students = {
        "S001": {"name": "Alice", "grades": [85, 90, 92]},
        "S002": {"name": "Bob", "grades": [78, 82, 88]}
    }
# Save students
if save_students_safe(students, "students.txt"):
    print("Students saved successfully!\n")
else:
    print("Failed to save students\n")
# Get a grade from user (with error handling)
print("Let's add a grade:")
grade = get_student_grade_safe()
print(f"You entered: {grade}\n")
# Display all students
print("=== All Students ===")
for student_id, info in students.items():
    avg = sum(info["grades"]) / len(info["grades"])
    print(f"{student_id}: {info['name']} - Average: {avg:.2f}")