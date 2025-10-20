# Stack using list
stack = []

# Push (add to top)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# Pop (remove from top)
top = stack.pop()
print(top)    # 3
print(stack)  # [1, 2]

# Peek (look at top)
top = stack[-1]
print(top)    # 2

# Check if empty
is_empty = len(stack) == 0
print(is_empty)  # False