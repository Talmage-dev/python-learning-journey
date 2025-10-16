students = {"S001": {"name": "Kardia", "age": 42, "grades": [52, 58, 53]}, "S002": {"name": "Talmage", "age": 40, "grades": [98, 95, 99]}}

def save_students(students, filename):
    with open(filename, "w") as file:
        for student_id, info in students.items():
            name = info["name"]
            age = (info["age"])
            grades_str = info["grades"]
            grades = ",".join(str(score) for score in grades_str)
            line = f"{student_id},{name},{age},{grades}\n"
            file.write(line)

def load_students(filename):
    students = {}
    with open(filename, "r") as file:
        for line in file:
            student = line.strip().split(",")
            student_id = student[0]
            name = student[1]
            age = student[1]
            grades = student[3:]
            info = {"name": name, "age": age, "grades": grades}
            students[student_id] = info
    return students

save_students(students, "stud.txt")
print(students)