"""Practice Warm Up"""

# Stack Edition
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0

def reverse_string(text):
    """Reverse a string using a stack"""
    stack = Stack()

    # Push all characters
    for char in text:
        stack.push(char)

    # Pop all characters (reversed)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    
    return result

def balanced_parentheses(expr):
    """Check if parentheses are balanced"""
    stack = Stack()
    pairs = {'(': ')', '{': '}', '[': ']'}

    for char in expr:
        if char in pairs:               # Opening bracket
            stack.push(char)
        elif char in pairs.values():    # Closing bracket
            if stack.is_empty():
                return False
            opening = stack.pop()
            if pairs[opening] != char:
                return False
    return stack.is_empty()             # Should be empty if balanced

def undo_system():
    """Demonstrate undo functionality with stack"""
    actions = Stack()

    # Perform actions
    actions.push("Type 'Hello'")
    actions.push("Type 'World'")
    actions.push("Delete 'World'")

    print("Actions performed:")
    # Show all actions (we'll just print the stack)
    temp = []
    while not actions.is_empty():
        action = actions.pop()
        temp.append(action)
        print(f" {action}")

    # Restore (push back)
    for action in reversed(temp):
        actions.push(action)
    
    # Undo last action
    print("\nUndo last action:")
    last = actions.pop()
    print(f" Undid: {last}")

    print("\nRemaining actions:")
    while not actions.is_empty():
        print(f" {actions.pop()}")

# ===== TESTS =====

print("=" * 50)
print("TEST 1: Reverse String")
print("=" * 50)
print(f"reverse_string('hello'): {reverse_string('hello')}")
print(f"reverse_string('Python'): {reverse_string('Python')}")
print(f"reverse_string('12345'): {reverse_string('12345')}")

print("\n" + "=" * 50)
print("TEST 2: Balanced Parentheses")
print("=" * 50)
print(f"balanced_parentheses('(hello)'): {balanced_parentheses('(hello)')}")
print(f"balanced_parentheses('(hello]'): {balanced_parentheses('(hello]')}")
print(f"balanced_parentheses('{{[()]}}'): {balanced_parentheses('{[()]}')}")
print(f"balanced_parentheses('((hello)'): {balanced_parentheses('((hello)')}")
print(f"balanced_parentheses('hello)'): {balanced_parentheses('hello)')}")

print("\n" + "=" * 50)
print("TEST 3: Undo System")
print("=" * 50)
undo_system()