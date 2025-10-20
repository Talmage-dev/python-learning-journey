# Day 13: Advanced OOP & Data Structures Reference

## Date: October 20, 2025

---

## Part 1: Advanced OOP

### Inheritance

**Concept:** A child class inherits attributes and methods from a parent class.

**Basic Pattern:**
```python
class Parent:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def method(self):
        return "Parent method"

class Child(Parent):  # Inherits from Parent
    def child_method(self):
        return "Child method"

# Child has both parent and child methods
obj = Child("value")
obj.method()        # From Parent
obj.child_method()  # From Child

Example:
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.eat())   # Inherited from Animal
print(dog.bark())  # Defined in Dog

- - -

Polymorphism

Concept: Same method name, different behavior in different classes.

Pattern:
class Parent:
    def method(self):
        return "Parent version"

class Child(Parent):
    def method(self):  # Override
        return "Child version"

Example:
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism in action
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Each calls their own version

- - -

Using super()
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent's __init__
        self.age = age
    
    def greet(self):
        parent_greeting = super().greet()  # Call parent's method
        return f"{parent_greeting} and I'm {self.age}"

When to use super():

- Call parent's init to initialize inherited attributes
- Extend (not replace) parent's methods
- Access parent functionality

- - -

Part 2: Data Structures - Stacks

What is a Stack?

LIFO

Last In, First Out (like a stack of plates)

Visual:
Push → [3][2][1] ← Pop
       Top

Stack Operations
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Look at top without removing"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get count"""
        return len(self.items)

Stack Applications

1. Reverse a String:
def reverse_string(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    
    reverse = ""
    while not stack.is_empty():
        reverse += stack.pop()
    return reverse

2. Browser History:
class Browser:
    def __init__(self):
        self.history = Stack()
    
    def visit(self, url):
        self.history.push(url)
    
    def back(self):
        return self.history.pop()
    
    def current_page(self):
        return self.history.peek()

3. Undo Functionality:
class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = Stack()
    
    def write(self, new_text):
        self.history.push(self.text)
        self.text += new_text
    
    def undo(self):
        if not self.history.is_empty():
            self.text = self.history.pop()

- - -

Part 3: Data Structures - Queues

What is a Queue?

FIFO - First In, First Out (like a line at a store)

Visual:
Enqueue → [1][2][3] → Dequeue
          Front    Rear

Queue Operations
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if not self.is_empty():
            return self.items.pop(0)  # Remove from front
        return None
    
    def front(self):
        """Look at front without removing"""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """Check if empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get count"""
        return len(self.items)

Queue Applications

1. Print Queue:
class PrintQueue:
    def __init__(self):
        self.queue = Queue()
    
    def add_document(self, doc_name):
        self.queue.enqueue(doc_name)
    
    def print_next(self):
        doc = self.queue.dequeue()
        if doc:
            print(f"Printing: {doc}")

2. Customer Service:
class CustomerService:
    def __init__(self):
        self.customers = Queue()
    
    def add_customer(self, name):
        self.customers.enqueue(name)
    
    def serve_next(self):
        customer = self.customers.dequeue()
        print(f"Serving {customer}")
    
    def current_customer(self):
        return self.customers.front()
    
    def customers_waiting(self):
        return self.customers.size()


- - -

Stack vs Queue Comparison

| Feature | Stack (LIFO) | Queue (FIFO) |

|---------|-------------|--------------|

| Add

| push()

to top | enqueue()

to rear |

| Remove

| pop()

from top | dequeue()

from front |

| Look

| peek()

at top | front()

at front |

| Order

| Last in, first out | First in, first out |

| Example

| Stack of plates | Line at store |

| Uses

| Undo, browser back | Print queue, customer service |

---

When to Use Each

Use Stack When:
- Need to reverse order
- Undo/redo functionality
- Backtracking (browser history)
- Expression evaluation
- Function call tracking

Use Queue When:
- Need to maintain order
- First-come, first-served
- Task scheduling
- Breadth-first search
- Message queues

- - -

Key Concepts

Inheritance

- IS-A relationship: Dog IS AN Animal
- Child inherits parent's attributes and methods
- Use when classes share common functionality

Composition

- HAS-A relationship: Browser HAS A Stack
- Object contains another object
- Use when you need functionality without inheritance

Polymorphism

- Same interface, different implementations
- Allows treating different objects uniformly
- Essential for flexible, extensible code

Data Structures

- Stack: LIFO - last in, first out
- Queue: FIFO - first in, first out
- Choose based on access pattern needed

- - -

Common Patterns

Inheritance with super()
class Child(Parent):
    def __init__(self, parent_attr, child_attr):
        super().__init__(parent_attr)
        self.child_attr = child_attr

Method Override
class Child(Parent):
    def method(self):
        # Completely new implementation
        return "Child version"

Method Extension
class Child(Parent):
    def method(self):
        parent_result = super().method()
        # Add to parent's result
        return f"{parent_result} + child addition"

Stack Pattern:
stack = Stack()
stack.push(item)      # Add
item = stack.pop()    # Remove
top = stack.peek()    # Look

Queue Pattern:
queue = Queue()
queue.enqueue(item)   # Add
item = queue.dequeue() # Remove
front = queue.front()  # Look

- - -

Practice Exercises Completed

1. ✅ Vehicle Inheritance (Car, Motorcycle)
2. ✅ Shape Area Calculator (Rectangle, Circle)
3. ✅ Bank Account Hierarchy (Savings, Checking)
4. ✅ Stack Implementation
5. ✅ Reverse String with Stack
6. ✅ Browser History with Stack
7. ✅ Queue Implementation
8. ✅ Customer Service Queue

- - -

End of Day 13 Reference

- - -
