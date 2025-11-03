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
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
def main(text):
    stack = Stack()
    matches = {')': '(', '}':'{', ']': '['}

    for char in text:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            if stack.pop() != matches[char]:
                return False

    return stack.is_empty()    

# Test
print(main("({[]})"))  # Should be True
print(main("({[}])"))  # Should be False
print(main("((()))"))  # Should be True
print(main("(()"))     # Should be False