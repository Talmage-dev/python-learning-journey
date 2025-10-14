""" Day 7 Practice Exercise: Reading and processing CSV-like Files """

# 8

def display_products_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)