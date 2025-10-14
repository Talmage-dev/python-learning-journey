""" Day 7 Final Challenge: Combine All I/O Patterns """

# Functions:

def load_inventory(filename):
    inventory = {}
    
    with open(filename, "r") as file:
        for line in file:
            part = line.strip().split(",")
            product_id = part[0]
            name = part[1]
            price = float(part[2])
            inventory[product_id] = {"name": name, "price": price}
    return inventory

def save_inventory(inventory, filename):
    with open(filename, "w") as file:
        for product_id, product_info in inventory.items():
            name = product_info["name"]
            price = product_info["price"]

            line = f"{product_id},{name},{price}\n"

            file.write(line)

def add_product(filename, product_id, name, price):
    with open(filename, "a") as file:
        line = f"{product_id},{name},{price}\n"
        file.write(line)

def display_inventory(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)

# Create initial inventory
inventory = {
    "P001": {"name": "Laptop", "price": 999.99},
    "P002": {"name": "Mouse", "price": 25.50}
}

# Save it
save_inventory(inventory, "inventory.txt")

# Display it
display_inventory("inventory.txt")

# Add new product
add_product("inventory.txt", "P003", "Keyboard", 75.00)

# Load and display updated inventory
inventory = load_inventory("inventory.txt")
print(f"\nTotal products: {len(inventory)}")