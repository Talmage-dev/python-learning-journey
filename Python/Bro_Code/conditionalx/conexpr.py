# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

# Example 1
num1 = 5
print("Positive" if num1 > 0 else "Negative")

# Example 2
num2 = 6
result = "EVEN" if num2 % 2 == 0 else "ODD"
print(result)

# Example 3
a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

# Example 4
age = 25
status = "Adult" if age >= 18 else "Child"
print(status)

# Example 5
temp = 30
weather = "HOT" if temp > 20 else "COLD"
print(temp)

# Example 6
user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)