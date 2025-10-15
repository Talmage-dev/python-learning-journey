""" Day 8 Error Handling """

# Practice Exercise 4: Safe Calculator

def safe_multiply(a, b):
    try:
        result = a * b
        return result
    except TypeError:
        print("Error: Both values must be numbers!")
        return None
