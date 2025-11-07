""" Day 8 Targeted Practice: Practice Set 1: Variable Naming """

# Exercise 1:

# fix mistake
def process_data(data):
    result = []
    for data in data:
        result.append(data * 2)
    return result

def process_data(data):
    result = []
    for info in data:
        result.append(info * 2)
    return result

# Exercise 2:

# fix mistake
def save_products(products, filename):
    with open(filename, "w") as file:
        for products, info in products.items():  # ❌ Problem here!
            name = info["name"]
            price = info["price"]
            file.write(f"{products},{name},{price}\n")

def save_products(products, filename):
    with open(filename, "w") as file:
        for product, info in products.items():
            name = info["name"]
            price = info["price"]
            file.write(f"{product},{name},{price}\n")
