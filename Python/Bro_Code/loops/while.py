# while loop = execute some code WHILE some condition remains true

# example 1
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")

# example 2
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"Yoou are {age} years old")

# example 3
food = input("Enter a food you like (press q to quit): ")

while not food == "q":
    print("f:You like {food}")
    food = input("Enter a food you like (press q to quit): ")

print("bye")

# example 4
num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")