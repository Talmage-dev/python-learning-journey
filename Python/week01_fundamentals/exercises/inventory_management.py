""" Day 6 Final Challenge: Inventory Management System """

# Inventory system for a small store.

# Setup
inventory = {}

# Functions
def add_product(inventory, product_id, name, price, quantity, category): # dict, key(str), value(flt), value(str), value(flt), value(str)
    #   1. Create a new dictionary for this student with:
    #       - name
    #       - price
    #       - quantity
    #       - category
    product = {"name":name, "price":price, "quantity":quantity, "category":category}
    #   2. Add this product dictionary to inventory using product_id as key
    inventory[product_id] = product

def update_stock(inventory, product_id, quantity_change): # dict, key(str), value(flt)
    #   1. Add quantity value - Increase or decrease stock (positive = add, negative = remove)
    inventory[product_id]["quantity"] += quantity_change

def get_product_value(inventory, product_id): # dict, key(str)
    #   1. Get price and quantity values
    price = inventory[product_id]["price"]
    quantity = inventory[product_id]["quantity"]
    #   2. Calculate value
    value = price * quantity
    #   3. Return value
    return value

def get_total_inventory_value(inventory): # dict   
#   1. Initialize total_value to 0
    total_value = 0
#   2. Loop through each product in inventory
    for product in inventory:
#       3. For each product, calculate its value (call get_product_value)
        value = get_product_value(inventory, product)
#       4. Add product value to total_value
        total_value += value
#   5. Return total_value
    return total_value

def get_low_stock_products(inventory, threshold=5): # dict, const(int)
    #   1. Create empty list for results
    results = []
    #   2. Loop through each product in inventory
    for product_id, product_info in inventory.items():
        #   3. If product's quantity < threshold:
        if product_info["quantity"] < threshold:
            #   4.     Add product_id to results list
            results.append(product_id)
    #   5. Return results list
    return results

def get_products_by_category(inventory, category): # dict, value(str)
    #   1. Create empty dictionary for results
    results = {}
    #   2. Loop through each product in inventory
    for product_key, product_values in inventory.items():
        #   3. If product's category matches the input category:
        if product_values["category"] == category:
            #   4.     Add product to results dictionary (same product_id as key)
            results[product_key] = product_values
    #   5. Return results dictionary
    return results

def display_product(inventory, product_id): # dict, key(str)
# Output: None (prints formatted info)
    #   1. Access product using product_id
    #   2. Get product's name, price, quantity, category
    product = inventory[product_id]
    #   3. Calculate product value (call get_product_value)
    value = get_product_value(inventory,product_id)
    #   4. Format and print all information
    print(f"ID: {product_id} - {product['name']} ({product['category']})")
    print(f"Price: ${product['price']:.2f}, Stock: {product['quantity']}, Value: ${value:.2f}")

# Main Program

#- Create 5 products in different categories
add_product(inventory, "P001", "Laptop", 999.99, 15, "Electronics")
add_product(inventory, "P002", "Gaming PC", 4999.99, 4, "Electronics")
add_product(inventory, "P003", "Coke", 2.99, 40, "Food")
add_product(inventory, "P004", "T-Shirt", 19.99, 50, "Clothing")
add_product(inventory, "P005", "Hat", 29.99, 20, "Clothing")
#- Display all products - loop through dictionary, call display_product
print("=== All Products ===")
for product in inventory:
    display_product(inventory, product)
    print()
#- Update stock for 2 products (one increase, one decrease) - call update_stock
print(". . .")
print()
print("=== After Stock Updates ===")
update_stock(inventory, "P004", 10)
update_stock(inventory, "P005", -5)
print(f"Updated P004: New stock = {inventory["P004"]['quantity']}")
print(f"Updated P005: New stock = {inventory["P005"]['quantity']}")
#- Display low stock products (threshold = 10) - call get_low_stock_products
print()
print("=== Low Stock alert (threshold: 5) ===")
low = get_low_stock_products(inventory)
for product in low:
    print(f"{product} - {inventory[product]["name"]}: {inventory[product]["quantity"]} units remaining")
#- Display all products in one category - find products of category, put in dictionary, loop & call display_product
print()
print("=== Electronics Category ===")
category = get_products_by_category(inventory, "Electronics")
for product_id, product_info in category.items():
    print(f"{product_id} - {product_info["name"]}: ${product_info["price"]} ({product_info["quantity"]} in stock)")
#- Display total inventory value - call get_total_inventory_value
print()
print("=== Total Inventory Value ===")
print(f"${get_total_inventory_value(inventory):.2f}")