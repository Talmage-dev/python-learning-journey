""" Day 4 Final Challenge: Student Grade Calculator """

# Requirements
# Create a student grade management system that:

# 1) Stores student data - Use a list of student scores: [85, 92, 78, 90, 65, 88, 73, 95, 82, 70]

# 2) Create these functions:
#   - calculate_letter_grade(score)                             - Returns letter grade (A,B,C,D,F)
#       - A: 90 - 100
#       - B: 80 - 89
#       - C: 70 - 79
#       - D: 60 - 69
#       - F: Below 60
#   - calculate_class_average(scores)                           - Returns the average score
#   - calculate_percentage_letter_grade(scores)                    - Returns the average letter grade
#   - count_passing_student(scores, passing_grade=60)           - Returns how many students passed
#   - is_at_risk(scores, risk=70)                               - Returns True of False
#   - find_highest_score(scores)                                - Returns the highest score
#   - find_lowest_score(scores)                                 - Returns the lowest score
#   - print_student_report(student_number, score, letter_grade) - Prints inidividual student info

# 3) Main program logic: 
#   - Loop through all students
#   - For each student, print their number, score, and letter grade
#   - after the loop, print a summary with:
#           - Class average
#           - Number of passing students
#           - Highest score
#           - Lowest score
#           - A message: If average >= 80, print "Excellent class performance!", otherwise print "Class needs improvement."

# Variables
score = [85, 92, 78, 90, 65, 88, 73, 95, 82, 70]
student_count = 1

# Functions
def calculate_letter_grade(score):
    """ 
    Calculate a students grade from their score. 
    
    Args:
        score (int):
    
    Return:
        grade (string):
    """
    if score >= 90: 
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_class_average(score):
    """
    Calculate the average class score
    
    Args:
        score(int): 
    
    Return:
        average(float)
    """
    total = sum(score)
    average = total / len(score)
    return average

def percentage_calculator(num):
    percent = (num / 10) * 100
    return percent

def calculate_percentage_letter_grade(score):
    a, b, c, d, f = 0
    for scores in score:
        if score >= 90:
            a += 1 
        elif score >= 80:
            b += 1
        elif score >= 70:
            c += 1
        elif score >= 60:
            d += 1
        else:
            f += 1
    result = print(f"A: {percentage_calculator(a)}%%\nB: {percentage_calculator(b)}%%\nC: {percentage_calculator(c)}%%\nD: {percentage_calculator(d)}%%\nF:{percentage_calculator(f)}%%")
    return result

def count_passing_student(score, passing_grade=60):
    pass_total = 0
    for scores in score:
        if scores >= passing_grade:
            pass_total += 1
    return pass_total

def is_at_risk(score, risk=70):

    return

def find_highest_score(scores):
    return max(scores)

def find_lowest_score(scores):
    return min(scores)

def print_student_report(student_number, score, letter_grade):
    print(f"Student {student_number}: Score: {score}, Grade: {letter_grade}")

# Loop
for scores in score:
    grade = calculate_letter_grade(scores)
    print_student_report(student_count, scores, grade)
    student_count += 1

# Class Summary
print("=== Class Summary ===")
average = calculate_class_average(score)
print(f"Class Average: {average:.2f}")
print(f"Passing Students: {count_passing_student(score)} out of {len(score)}")
print(f"Highest Score: {find_highest_score(score)}")
print(f"Lowest Score: {find_lowest_score(score)}")
if average >= 80:
    print("Excellent class performance!")
else:
    print("Class needs improvement.")