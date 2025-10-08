# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Bro Code"
age = 25
gpa = 3.5
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

print(name)
print(age)
print(gpa)
print(is_student)

name = bool(name)
age = float(age)
gpa = int(gpa)
is_student = str(is_student)

print(name)
print(age)
print(gpa)
print(is_student)

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

is_student += "1"

print(is_student)