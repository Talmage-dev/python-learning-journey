""" Day 8 Error Handling """

# Practice Exercise 3: Safe File Reader

def load_products_safe(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
