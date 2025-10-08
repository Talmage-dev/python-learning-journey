# Phython calculator

num1 = float(input("Enter 1st number: "))
operator = input("Enter an operator (+ _ * ?): ")
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {round(result, 2)}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} {operator} {num2} = {round(result, 2)}")
else:
    print(f"{operator} is not valid a valid operator")