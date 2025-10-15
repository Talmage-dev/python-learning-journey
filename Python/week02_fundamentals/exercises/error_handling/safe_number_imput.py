""" Day 8 Error Handling """

# Practice Exercise 1: Safe Number Input

def get_age(prompt):
    try:
        age = int(input(prompt))
        return age
    except ValueError:
        print("Error: Please enter a valid number!")
        return None
    
# Practice Exercise 2: Safe price Input

def get_price(prompt):
    try:
        price = float(input(prompt))
        return price
    except ValueError:
        print("Error: Enter a valid number!")
        return None
    
