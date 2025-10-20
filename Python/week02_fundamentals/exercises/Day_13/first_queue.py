""" Day 13 (continued): Intro to Data Structures - Queues """

# Practice Exercise 4: Build Your Own Queue

class Queue:
    def __init__(self):
        self.items = []
  
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)     # Add to rear
    
    def dequeue(self):
        """Remove and return front item"""
        if not self.is_empty():
            return self.items.pop(0)  # Remove from front
        return None
    
    def front(self):
        """Return front item without removing"""
        if not self.is_empty():
            return self.items[0]    # Show front
        return None
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0     # Is it empty
    
    def size(self):
        """Return number of items"""
        return len(self.items)      # How many items in queue
    
    def display(self):
        """Show all items"""
        print("Queue:", self.items)     # Show everything

# Test 1
# queue = Queue()
# queue.enqueue("Alice")
# queue.enqueue("Bob")
# queue.enqueue("Charlie")
# queue.display()
# print(queue.dequeue())  # Alice (first in line!)
# print(queue.front())    # Bob

# Practice Exercise 5: Customer Service Queue

class CustomerService:
    def __init__(self):
        self.customers = Queue()
    
    def add_customer(self, name):
        self.customers.enqueue(name)
    
    def serve_next(self):
        print(f"Serving {self.customers.dequeue()}")
    
    def current_customer(self):
        return self.customers.front()
    
    def customers_waiting(self):
        return self.customers.size()

# Test 2    
service = CustomerService()
service.add_customer("Alice")
service.add_customer("Bob")
service.add_customer("Charlie")
print(f"Waiting: {service.customers_waiting()}")  # 3
service.serve_next()  # "Serving Alice"
print(f"Current: {service.current_customer()}")   # "Bob"