# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it wass the value it contains

#Strings
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

#Integer
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You can buy {quantity} items")
print(f"Your class has {num_of_students} students")

#Floats
price = 10.99
gpa = 3.2
distance = 5.5

print(f"thie price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km's")

#Boolean
is_student = False

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

for_sale = True

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

is_online = True


if is_online:
    print("You are online")
else:
    print("You are offline")