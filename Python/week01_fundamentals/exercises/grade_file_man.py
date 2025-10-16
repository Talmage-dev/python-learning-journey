""" Day 7 Practice Exercise: Student Grade File Manager """

# Setup:

# Functions:
def save_students_to_file(students, filename):
# Steps: 
    # 1. Open the file in write mode ("w")
    with open(filename, "w") as file:
        # 2. Loop through each student in the students dictionary
        for student_id, student_info in students.items():
            # b. Get student info (name, grades)
            name = student_info["name"]
            grades_str = student_info["grades"] 
            # c. Format the grades list into a string (join with commas)
            grades = ",".join(str(score) for score in grades_str)
            # d. Create the line: "student_id,name,grades_string\n"
            line = f"{student_id},{name},{grades}\n"
            # e. Write this line to the file
            file.write(line)
    # 4. File closes automatically (using 'with')
    
def load_students_from_file(filename):
    # 1. Create empty dictionary (students)
    students = {}
    # 2. Open file in read mode ("r")
    with open(filename, "r") as file:
        # 3. Loop through each line in file
        for line in file:
            # a. Remove whitespace/newline (strip)
            # b. Split line by comma into parts: ["S001", "Alice", "85", "90" "92"]
            parts = line.strip().split(",")
            # c. Extract student_id from parts[0]
            student_id = parts[0]
            # d. Extract name from parts[1]
            name = parts[1]
            # e. Create list from parts [2:]: grades = ["85", "90", "92"]
            grades_str = parts[2:]
            # f. grades = [int(score) for score in grades]
            grades = [int(score) for score in grades_str]
            # g. Create student_info dict: {"name": Alice, "grades": [85, 90, 92]}
            student_info = {"name": name, "grades": grades}
            # h. Add to dictionary: students[student_id] = student_info
            students[student_id] = student_info
        # 5. Return dictionary
    return students
    # 6. File closes automatically (using 'with')

def add_student_to_file(filename, student_id, name, grades): 
    # 1. Open file in append mode ("a")
    with open(filename, "a") as file:
        # 2. Convert grades to comma-seperated string: 
        grades_str = ",".join(str(score) for score in grades)
        # 3. format the line: 
        line = f"{student_id},{name},{grades_str}\n"
        # 4. Write line to file
        file.write(line)
    # 5. File closes automatically (using 'with')
    
def display_file_contents(filename):
# Output: string (print file contents)
    # 1. Open file in read mode ("r")
    with open(filename, "r") as file:
        # 2. Read entire file content
        content = file.read()
        # 3. Print the content
        print(content)
    # 4. File closes automatically (using 'with')
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

# Main logic:
# Create 3 students (reuse Day 6 structure)
students = {
    "S001": {"name": "Alice", "grades": [85, 90, 92]},
    "S002": {"name": "Bob", "grades": [78, 82, 88]},
    "S003": {"name": "Charlie", "grades": [92, 95, 89]},
}
# Save them to "students.txt"
save_students_to_file(students, "students.txt")
# Load them back from file
students = load_students_from_file("students.txt")
# Add a new student to the file
student_id = "S004"
name = "Donald"
grades = [99, 98, 94]
add_student_to_file("students.txt", student_id, name, grades)
students = load_students_from_file("students.txt")
# Display all students from file
display_file_contents("students.txt")
# Calculate and display averages
for student in students:
    average = get_average(students[student]["grades"])
    print(f"Student {student}: Grade average: {average:.2f}")
