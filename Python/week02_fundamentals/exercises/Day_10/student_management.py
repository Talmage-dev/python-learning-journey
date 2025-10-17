""" Day 10: Object-Oriented Programming (OOP) - Part 1 """

# Final Challenge: Complete Student Management System

class Student:
    total_students = 0

    def __init__(self, name, student_id,):
        self.name = name
        self.student_id = student_id
        self.grades = []
        Student.total_students += 1
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_info(self):
        return f"Name: {self.name}, Student ID: {self.student_id}, Grades: {self.grades}\n"
    
    def is_passing(self):
        return self.get_average() >= 60
    
class Classroom:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_class_average(self):
        if not self.students:
            return 0
        total = sum(student.get_average() for student in self.students)
        return total / len(self.students)

    def get_passing_students(self):
        passing_students = []
        for student in self.students:
            if Student.is_passing(student):
                passing_students.append(student)
        return passing_students
    
    def display_all_students(self):
        print("Students in Class")
        for student in self.students:
            info = Student.get_info(student)
            print(info)

# Create classroom
math_class = Classroom()

# Create and add students
s1 = Student("Alice", "S001")
s1.add_grade(85)
s1.add_grade(90)
s1.add_grade(92)

s2 = Student("Bob", "S002")
s2.add_grade(55)
s2.add_grade(60)
s2.add_grade(58)

math_class.add_student(s1)
math_class.add_student(s2)

# Display results
math_class.display_all_students()
print(f"Class average: {math_class.get_class_average():.2f}")
print(f"Total students created: {Student.total_students}")