"""Practice with user input and type conversion."""

def calculator():
    """Simple calculator with error handling."""
    print("=== Simple Calculator ===")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator(+,-,*,/): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print(f"Error: Unkown operator '{operator}'")
            return
        
        print(f"\n{num1} {operator} {num2} = {result:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    calculator()