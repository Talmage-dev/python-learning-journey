""" Tutorial 7 """

import math

# Objectives:
#       To introduce you to evaluating formulae that include variables in Python.
#       We will also look at what functions are available in Math library.

# Reading:
#       Before coming to this tutorial, you should have read Chapter 2 of Fangohr.
#       You may also want to read https://docspython.org/3/library/math/html.

# Summary:
# 1)    Data types in Python.
# 2)    Creating naming varables.
# 3)    Using Math Functions.

# Exercises:

""" # 1)    What numeric data types are available in Python? """
#       Integer, Floatin Point, Complex Numbers, decimal.Decimal, fractions.Fraction

type(42)            # <class 'int'>
type(3.14)          # <class 'float'>
type(2+3j)          # <class 'complex'>
isinstance(42, int) # True

""" # 2)    How do you create a variable in Python? """
#       Basic Syntax:
#       variable_name = value
# Examples

# Numbers
age = 25
price = 19.99
temp = -5

# Strings 
name = "Alice"
message = 'Hello, World!'

# Boolean
is_student = True
has_license = False

# Multiple assignments
x = y = z = 0 # All three get the same value

# Multiple variables at once
a, b, c = 1, 2, 3

# Key points:
# 1) No declaration needed - Python automatically determines the type based on the value
# 2) dynamic typing - Variables can change type:
x = 5       # x is an integer
x = "hi"    # now x is a string
# 3) Naming rules:  - Must start with a letter or underscore(_)
#                   - Can contain letters, numbers, and underscores
#                   - Case-sensitive (age and Age are different)
#                   - Cannot use Python keywords (if, for, while, etc.)
# 4) Naming conventions: 
#                   - Use lowercase with underscores: student_name, total_price
#                   - Descriptive names: age not a, count not c
# Good examples:
student_name = "Bob" 
total_count = 100
is_valid = True

# Valid but not recommended
x = 5
a = "test"

""" # 3)    An enginner needs to store info about screws required for a project.
            They need to store the type of screw, the price, the length and 
            whether the screw is a right-handed thread or not.
            Show how you would store the following information:

            The screw type is Phillips head, it is 25 mm long, 
            its current rental price is $0.50 and right-handed thread should be set to true.

"""

screw_type = "Phillips Head"
price = 0.5
length = 25
is_right_handed = True

""" # 4)    Write the result of evaluating each of the following expressions when the variable 'length' has the value '8'.
            After each result, write down the Python type of the result.
"""
length = 8

a = 3 + length * 2
print(a)
print(type(a))

b = 3.2 + length * 2
print(b)
print(type(b))

c = 2 + length / 3
print(c)
print(type(c))

d = 2 ** length
print(d)
print(type(d))

e = length // 3
print(e)
print(type(e))

f = math.pi * 2
print(f)
print(type(f))

g = math.radians(180)
print(g)
print(type(g))

h = math.sin(0)
print(h)
print(type(h))

""" # 5)    What is the value of x. """
x = 12 % 2
print(x)
print(type(x))

x = 9 % 2
print(x)
print(type(x))

x = 20 % 6
print(x)
print(type(x))

x = 8 % 10
print(x)
print(type(x))

x = 8
print(x)
print(type(x))

x = "eight"
print(x)
print(type(x))

""" # 7)    Can you create a constant in Python? """

# python doesn't have true constants like some other languages, but there's a convention for creating them:

# Convention: Use UPPERCASE names
# Constants (by convention)
PI = 3.14159
MAX_SIZE = 100
DEFAULT_COLOUR = "blue"
TAX_RATE = 0.15

# Important Notes:
# 1) Not enforced - Python won't stop you from changing these values:
PI = 3.14159
PI = 5  # This works, but you shouldn't do it!
# 2) It's a naming convention - Using UPPERCASE tells other programmers "don't change this value"
# 3) Where to define them:
# At the top of your file
MAX_ATTEMPTS = 3
TIMEOUT = 30

def myfunction():
    # Use the constant
    for i in range(MAX_ATTEMPTS):
        print(i)

# For True Immutability:
# If you need actual constant behavior, you can use:
# 1) Tuples (immutables):
COORDINATES = (10, 20)  # Can't change individual values
# 2) typing.Final (Python 3.8+) - provides type hints:
from typing import Final

MAX_SIZE: Final = 100
# 3) Module-level constant in seperate file:
# constants.py
# PI =3.14159
# MAX_SIZE = 100

# main.py
# import constants
# print(constants.PI)

# Bottom line: Use UPPERCASE naming for constants - it's the Pythonic way,
#              even though it's not technically enforced.

""" # 8)    Your marine engineer friend Nic is trying to calculate how much 
            marine paint they need to paint the boats in the engineer
            companies fleet. Nic has written a python program to calculate the
            litres of paint required to paint a boat, based on its surface area, and
            stores this information in th variable paintRequired which is a
            floating-point number. Marine paint is only availiable in tins
            containing 5 litres of paint, so Nic used the following Python code
            to work out the number of tins of paint required for the wall.
            numTins = int(paintRequired/5)
            Nic is almost always short of paint when they go to paint a boat.
            Why? What formula should they have used?
"""

paintRequired = 13
numTins = math.ceil(paintRequired / 5)

# Alternative Solutions
numTins = int(paintRequired / 5) + (1 if paintRequired % 5 > 0 else 0)
# Or more concisely:
numTins = -(-paintRequired // 5)  # Clever trick using floor division