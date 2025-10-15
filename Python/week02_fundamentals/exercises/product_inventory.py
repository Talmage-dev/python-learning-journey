""" Day 8 Final Challenge: Product Inventory System """

def load_inventory_safe(filename):
    inventory = {}
    try:
        with open(filename, "r") as file:
            for line in file:               # P001,Laptop,999.99,15
                part = line.strip().split(",")
                product_id = part[0]
                name = part[1]
                price = float(part[2])
                quantity = int(part[3])
                item_info = {"name": name, "price": price, "quantity": quantity}
                inventory[product_id] = item_info
        return inventory
    except FileNotFoundError:
        return inventory

def save_inventory_safe(inventory, filename):
    try:
        with open(filename, "w") as file:
            for product_id, product_info in inventory.items():          # P001: {name: Laptop, price: 999.99, quantity, 15}
                name = product_info["name"]
                price = str(product_info["price"])
                quantity = str(product_info["quantity"])
                line = f"{product_id},{name},{price},{quantity}\n"
                file.write(line)
        return True
    except PermissionError:
        return False

def get_low_stock_products(inventory, threshold=20):
    low_stock = {product_id: info for product_id, info in inventory.items() if info["quantity"] < threshold}
    return low_stock

def get_total_value(inventory):
    total_value = sum(float(info["price"]) * float(info["quantity"]) for product_id, info in inventory.items())
    return total_value

def add_product_safe(inventory, product_id, name, price, quantity):
    if price <= 0:
        print("Error: Price must be greater than 0")
        return False
    
    if quantity < 0:
        print("Error: Quantity cannot be negative")
        return False
    
    inventory[product_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def update_quantity_safe(inventory, product_id, change):
    try:
        quantity = inventory[product_id]["quantity"] + change
        inventory[product_id]["quantity"] = quantity
        return quantity
    except KeyError:
        return None

# Main Program

# 1. If empty, create sample data
inventory = {
    "P001": {"name": "Laptop", "price": 999.99, "quantity": 15},
    "P002": {"name": "Mouse", "price": 25.50, "quantity": 50},
    "P003": {"name": "Keyboard", "price": 75.00, "quantity": 30}
}
save_inventory_safe(inventory, "inventory.txt")

# 2. Load inventory (handle if file doesn't exist)
inventory = load_inventory_safe("inventory.txt")
print(f"Loaded {len(inventory)} products\n")

# 3. Display all products with total value
print("=== Current Inventory ===")
for product_id, info in inventory.items():
    value = info["price"] * info["quantity"]
    print(f"{product_id}: {info['name']} - ${info['price']:.2f} x {int(info['quantity'])} = ${value:.2f}")

# 4. Show total inventory value (use comprehension)
total = get_total_value(inventory)
print(f"\nTotal Inventory Value: ${total:.2f}\n")

# 5. Show low stock products (use comprehension)
low_stock = get_low_stock_products(inventory, threshold=20)
if low_stock:
    print("=== Low Stock Alert ===")
    for product_id, info in low_stock.items():
        print(f"{product_id}: {info['name']} - Only {info['quantity']} left!")
    print()

# 6. Add new product
if add_product_safe(inventory, "P004", "Monitor", 350.00, 8):
    print("Added Monitor to inventory\n")

# 7. Update quantities
update_quantity_safe(inventory, "P002", -10)  # Sold 10 mice
update_quantity_safe(inventory, "P003", 20)   # Restocked 20 keyboards

# 8. Save inventory
if save_inventory_safe(inventory, "inventory.txt"):
    print("Inventory saved successfully!")