""" Day 17: Project - Resturant Order System """

# Imports
import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import Stack, Queue, BinarySearchTree

# Menu Class
class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.category})"
    
# Order Class
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.total = sum(item.price for item in items)
    
    # Missing this:
    def __str__(self):
        items_str = ", ".join(item.name for item in self.items)
        return f"Order #{self.order_id}: {items_str} - Total: ${self.total:.2f}"

# ResturantSystem Class
class ResturantSystem:
    def __init__(self):
        self.menu_tree = BinarySearchTree()
        self.pending_orders = Queue()
        self.completed_orders = Stack()
        self.order_counter = 1
        self.menu_items = {}

    def add_menu_item(self, name, price, category):
        self.menu_items[name] = MenuItem(name, price, category)
        self.menu_tree.insert(price)
    
    def place_order(self, item_names):
        items = []
        for name in item_names:
            if name in self.menu_items:
                items.append(self.menu_items[name])
        order = Order(self.order_counter, items)
        self.pending_orders.enqueue(order)
        self.order_counter += 1
        return order
    
    def complete_next_order(self):
        order = self.pending_orders.dequeue()
        if order:
            self.completed_orders.push(order)
            return order
        return None
    
    def view_pending_orders(self):
        if self.pending_orders.is_empty():
            print("No pending orders")
        else:
            print("Pending Orders:")
            for order in self.pending_orders.items:
                print(f" {order}")
    
    def view_recent_orders(self):
        if self.completed_orders.is_empty():
            print("No completed orders")
        else:
            print("Completed Orders:")
            for order in self.completed_orders.items:
                print(f" {order}")
    
    def view_menu_sorted(self):
        print("Menu (sorted by price):")
        self.menu_tree.inorder(self.menu_tree.root)

# Test
restaurant = ResturantSystem()

# Add menu items
restaurant.add_menu_item("Burger", 8.99, "Main")
restaurant.add_menu_item("Fries", 3.99, "Side")
restaurant.add_menu_item("Soda", 1.99, "Drink")
restaurant.add_menu_item("Pizza", 12.99, "Main")
restaurant.add_menu_item("Salad", 6.99, "Side")

print("=== Menu (sorted by price) ===")
restaurant.view_menu_sorted()

print("\n=== Placing Orders ===")
order1 = restaurant.place_order(["Burger", "Fries", "Soda"])
print(f"Placed: {order1}")

order2 = restaurant.place_order(["Pizza", "Salad"])
print(f"Placed: {order2}")

order3 = restaurant.place_order(["Burger", "Soda"])
print(f"Placed: {order3}")

print("\n=== Pending Orders ===")
restaurant.view_pending_orders()

print("\n=== Completing Orders ===")
completed = restaurant.complete_next_order()
print(f"Completed: {completed}")

completed = restaurant.complete_next_order()
print(f"Completed: {completed}")

print("\n=== Pending Orders (after completing 2) ===")
restaurant.view_pending_orders()

print("\n=== Recent Completed Orders ===")
restaurant.view_recent_orders()