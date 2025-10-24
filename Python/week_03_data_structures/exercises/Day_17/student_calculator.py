""" Student Grade Calculator """

students = []

# Inputs:
def homework():
    while True:
        try:
            homework_ave = float(input("Enter students homework average: "))
            if 0 <= homework_ave <= 100:
                return homework_ave
            else:
                print("Invalid input, must be a number between 0-100")
                continue
        except ValueError:
            print("Invalid input: value must be a number between 0-100")
            continue

def quiz():
    while True:
        try:
            quiz_ave = float(input("Enter students quiz average: "))
            if 0 <= quiz_ave <= 100:
                return quiz_ave
            else:
                print("Invalid input, must be a number between 0-100")
                continue
        except ValueError:
            print("Invalid input: value must be a number between 0-100")
            continue

def mid_term():
    while True:
        try:
            mid = float(input("Enter students Mid-term Exam score: "))
            if 0 <= mid <= 100:
                return mid
            else:
                print("Invalid input, must be a number between 0-100")
                continue
        except ValueError:
            print("Invalid input: value must be a number between 0-100")
            continue

def final_score():
    while True:
        try:
            final = float(input("Enter students Final Exam score: "))
            if 0 <= final <= 100:
                return final
            else:
                print("Invalid input, must be a number between 0-100")
                continue
        except ValueError:
            print("Invalid input: value must be a number between 0-100")
            continue

def enter_student_info():
    student = {}
    stud_name = input("Enter students name: ")
    homework_ave = homework()
    quiz_ave = quiz()
    midterm = mid_term()
    final = final_score()

    grade = (homework_ave*0.2)+(quiz_ave*0.2)+(midterm*0.3)+(final*0.3)
    if grade >= 90:
        letter = 'A'
    elif grade >= 80:
        letter = 'B'
    elif grade >= 70:
        letter = 'C'
    elif grade >= 60:
        letter = 'D'
    else:
        letter = 'F'

    info = {"grade": grade, "letter": letter, "scores": [homework_ave, quiz_ave, midterm, final]}
    student[stud_name] = info
    students.append(student)
    print(f"Thank you, {stud_name}'s information has been updated.")
            

                
def display_student_information(stud_name):
    for student in students:
        if stud_name in student:    # ✓ Check if key EXISTS first
            print(f"{stud_name}'s Final Grade: {student[stud_name]['grade']:.2f} {student[stud_name]['letter']}")
            return
    print("Student not found")

def main():
    while True:
        choice = input("Enter 's' to enter students score or enter 'f' to view a students grade or 'q' to quit: ")
        if choice.lower() == 's':
            enter_student_info()
        elif choice.lower() == 'f':
            if len(students) == 0:
                print("No students have been entered yet")
                continue
            else:
                stud_name = input("Enter students name: ")
                display_student_information(stud_name)
                continue
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid input, try again")
            continue

main()