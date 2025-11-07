# Queue using list
queue = []

# Enqueue (add to rear)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # [1, 2, 3]

# Dequeue (remove from front)
front = queue.pop(0)  # Remove first item
print(front)   # 1
print(queue)   # [2, 3]

# Front (look at first)
front = queue[0]
print(front)   # 2