""" Day 6 Exercise: Student Management System """

# Variables (Setup)
students = {}

# Functions
def add_student(students, student_id, name, age, email):
    # Function: add_student
    # Input: students dict, student_id, name, age, email
    # Output: None (modifies student dict)
    # Steps:
    #   1. Create a new dictionary for this student with:
    #       - name
    #       - age
    #       - email
    #       - grades (empty list to start)
    grades = []
    student = {"name":name, "age":age, "email":email, "grades":grades}
    #   2. Add this student dictionary to students using student_id as key
    students[student_id] = student

def add_grade(students, student_id, grade):
    # Function: add_grade
    # Input: students dict, student_id, grade
    # Output: None (modifies students dict)
    # Steps:
    #   1. Add grade to student
    students[student_id]["grades"].append(grade)

def get_average(grades):
    # Function: get_average
    # Input: list of grades
    # Output: float (average)
    # Steps:
    #   1. Sum all grades in the list
    #   2. divide sum by number of grades (length of list)
    average = sum(grades) / len(grades)
    #   3. return average
    return average

def get_student_info(students, student_id):
    # Function: get_student_info
    # Input: students dict, student_id
    # Output: string (formatted info)
    # Steps:
    #    1. Access student using student_id
    #    2. Get student's name, age, email, grades
    #    3. Calculate average of grades (call get_average)
    #    4. Format into a readable string
    #    5. Return the formatted string
    print(f"Student: {students[student_id]["name"]}, age: {students[student_id]["age"]}, email: {students[student_id]["email"]} grades: {students[student_id]["grades"]}")

def get_all_averages(students):
    # Function: get_all_averages
    # Input: students dict
    # Output: dictionary {student_id: average}
    # Steps:
    #   1. Create empty dictionary for results
    result = {}
    #   2. Loop through each student in students dict
    for student_id, student_info in students.items(): # Student_id (key) Student_info (values)
        #   3. For each student, get their grades
        grades = student_info["grades"]
        #   4. Calculate average (call get_average)
        ave = get_average(grades)
        #   5. Add student_id and average to results dictionary
        result[student_id] = ave
    #   6. Return results dictionary
    return result

# Main Logic
# Create 3 students
add_student(students, 1, "Alice", 25, "alice@example.com")
add_student(students, 2, "Bob", 40, "bob@example.com")
add_student(students, 3, "Charlie", 32, "charlie@example.com")
# Add grades
add_grade(students, 1, 89)
add_grade(students, 1, 52)
add_grade(students, 1, 99)
add_grade(students, 1, 75)

add_grade(students, 2, 45)
add_grade(students, 2, 63)
add_grade(students, 2, 85)
add_grade(students, 2, 75)

add_grade(students, 3, 98)
add_grade(students, 3, 92)
add_grade(students, 3, 99)
add_grade(students, 3, 96)
#Display Info
print("=== Stundent Info ===")
for student in students:
    get_student_info(students, student)
    average = get_average(students[student]["grades"])
    print(f"Grade average: {average}")
    print()
#Calculate and display class averages
print("\n=== Class Averages ===\n")
all_ave = get_all_averages(students)
for key, value in all_ave.items():
    print(f" Student {key}: {value}")
# Calculate overall class average
all_averages = list(all_ave.values())
class_average = sum(all_averages) / len(all_averages)
print(f"\nOverall Class Average: {class_average:.2f}")
