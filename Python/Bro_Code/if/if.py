# if = Do some code only IF some condition is True
#      Else do something else

# Example 1
age = int(input("Enter your age: "))

if age >= 100:
    print("You are to old to get a credit card.")
elif age >= 18:
    print("You are eligible for a credit card.")
elif age <0:
    print("You havent been born yet!")
else:
    print("You must be 18 years old to be eligible to get a credit card.")

# Example 2
response = input("Would you like some food? (Y/N): ")

if response == "Y":
    print("Have some food.")
else:
    print("No food for you!")

# Example 3
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")

# BOOLEAN if statements

# Example 1
for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is NOT for sale.")

# Example 2
online = False

if online:
    print("The user is online.")
else:
    print("The user is offline.")