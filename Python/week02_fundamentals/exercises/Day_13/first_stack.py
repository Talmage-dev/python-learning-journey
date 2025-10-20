""" Day 13(continued): Intro to Data Structures - Stacks """

# Practice Exercise 1: Build your own stack

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Return top item without removing"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Checks if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items"""
        return len(self.items)
    
    def display(self):
        """Show all items"""
        print("Stack", self.items)

# Test 1
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.display()
# print(stack.pop())
# print(stack.peek())

# Practice Exercise 2: Reverse a String Using Stack

def reverse_string(text):
    stack = Stack() 
    
    for char in text:
        stack.push(char)
    
    reverse = ""
    while not stack.is_empty():
        reverse += stack.pop()
    
    return reverse

# Test 2
# print(reverse_string("hello"))  # "olleh"
# print(reverse_string("Python"))  # "nohtyP"

# Practice Exercise 3: Browser History

class Browser:
    def __init__(self):
        self.history = Stack()
    
    def visit(self, url):
        self.history.push(url)

    def back(self):
        self.history.pop()

    def current_page(self):
        return self.history.peek()

# Test 3
browser = Browser()
browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")
print(browser.current_page())  # "github.com"
browser.back()
print(browser.current_page())  # "youtube.com"