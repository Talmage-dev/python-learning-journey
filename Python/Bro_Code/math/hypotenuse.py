import math

# Excercise 3
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = round(math.sqrt(pow(a, 2) + pow(b, 2)))

print(f"The length of the hypotenuse (side C) is: {c}")