# function = A block of reusable code
#            place () after th function name to invoke it

# Example 1
def happy_birthday(name, age):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print(f"Happy birthday dear {name}!")
    print("Happy birthday to you!")
    print(f"You are {age} years old")

happy_birthday("Bro Code", 20)
happy_birthday("Bro Code", 21)
happy_birthday("Bro Code", 22)

# Example 2
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("JoeSchmo", 42.50, "01/02/2026")

# return = statement used to end a function
#          and send a result back to the caller

# Example 1
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

# Example 2
def create_name(first, last):
    first = first.capitalize()
    last = last.capitialize()
    return first + " " + last

full_name = create_name("bro", "code")
print(full_name)