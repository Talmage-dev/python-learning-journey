""" Day 7 Practice Exercise: Reading and processing CSV-like Files """

# 7

def add_product_to_file(filename, product_id, name, price):
    with open(filename, "a") as file:
        line = f"{product_id},{name},{price}\n"
        file.write(line)
    