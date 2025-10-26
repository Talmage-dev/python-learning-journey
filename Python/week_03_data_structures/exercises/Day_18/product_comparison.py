""" Day 18: Application Project - Product Price Comparison Tool """

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import BinarySearchTree


class Product:
    def __init__(self, name, price, store):
        self.name = name
        self.price = price
        self.store = store
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} at {self.store}"

class ProductComparison:
    def __init__(self):
        self.price_tree = BinarySearchTree()            # BST for prices
        self.products = {}                              # Dictionary: price -> list of products
    
    # 1. add_product(name, price, store)
    def add_product(self, name, price, store):
        """Add a product to Tree and Dictionary"""
        product = Product(name, price, store)

        self.price_tree.insert(price)                   # Add product to BST

        if price in self.products:                      # Add product to dictionary
            self.products[price].append(product)
        else:
            self.products[price] = [product]

    # 2. find_by_price(price)
    def find_by_price(self, price):
        """Find all products at a specific price"""
        if price in self.products:                      # If price is in dictionary
            return self.products[price]                 # Return the list
        return []                                       # If not in dictionary return an empty list
    
    # 3. show_all_sorted()
    def show_all_sorted(self):
        """Display all products sorted by price"""
        sorted_prices = sorted(self.products.keys())
        for price in sorted_prices:
            for product in self.products[price]:
                print(f" {product}")

    # 4. find_cheapest()
    def find_cheapest(self):
        """Find the cheapest products"""
        if not self.products:
            return []
        min_price = min(self.products.keys())
        return self.products[min_price]
        
    # 5. find_most_expensive()
    def find_most_expensive(self):
        """Find the most expensive products"""
        if not self.products:
            return []
        max_price = max(self.products.keys())
        return self.products[max_price]
    
# Test
pc = ProductComparison()

# Add products
pc.add_product("iPhone 15", 999.99, "Apple Store")
pc.add_product("iPhone 15", 949.99, "Best Buy")
pc.add_product("iPhone 15", 949.99, "Amazon")
pc.add_product("Samsung Galaxy", 899.99, "Samsung Store")
pc.add_product("Google Pixel", 699.99, "Google Store")
pc.add_product("OnePlus 12", 799.99, "OnePlus Store")

print("=== All Products (Sorted by Price) ===")
pc.show_all_sorted()

print("\n=== Products at $949.99 ===")
products = pc.find_by_price(949.99)
for p in products:
    print(f"  {p}")

print("\n=== Cheapest Product(s) ===")
cheapest = pc.find_cheapest()
for p in cheapest:
    print(f"  {p}")

print("\n=== Most Expensive Product(s) ===")
expensive = pc.find_most_expensive()
for p in expensive:
    print(f"  {p}")