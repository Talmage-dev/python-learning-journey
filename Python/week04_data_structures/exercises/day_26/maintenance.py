"""Day 26: Maintenance - Queues"""

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import Stack

# Part 1:
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Part 2:
def rev_first_k_elements(ar, k):
    queue = Queue()
    stack = []
    # Build queue from array
    for num in ar:
        queue .enqueue(num)
    # Dequeue first k elements, push to stack
    for i in range(k):
        element = queue.dequeue()
        stack.append(element)
    # Pop from stack and enqueue to queue (reverse k elements)
    while len(stack) > 0:
        element = stack.pop()
        queue.enqueue(element)
    # Move the remining elements to back of queue
    remaining = queue.size() - k
    for i in range(remaining):
        element = queue.dequeue()
        queue.enqueue(element)
    # Convert back to an array and return it
    result = []
    while not queue.is_empty():
        result.append(queue.dequeue())
    return result

# # Part 2: (better way of doing it)
# def rev_first_k_elements(ar, k):
#     queue = Queue()
#     stack = Stack()

#     # add ar to queue
#     for num in ar:
#         queue.enqueue(num)

#     # Dequeue first k elements and push to stack    
#     for i in range(k):
#         stack.push(queue.dequeue())

#     # Pop from stack and enqueue back
#     while not stack.is_empty():
#         queue.enqueue(stack.pop())
    
#     # Move remaining elements to back of queue
#     remaining = queue.size() - k
#     for i in range(remaining):
#         queue.enqueue(queue.dequeue())
    
#     # remove from queue into an array and return it
#     result = []
#     while not queue.is_empty():
#         result.append(queue.dequeue())
    
#     return result

# Test: Queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Should print 1
print(q.peek())     # Should print 2
print(q.size())     # Should print 2

# Test 1
print(rev_first_k_elements([1, 2, 3, 4, 5], 3))
# Expected: [3, 2, 1, 4, 5]

# Test 2
print(rev_first_k_elements([1, 2, 3, 4, 5], 2))
# Expected: [2, 1, 3, 4, 5]

# Test 3
print(rev_first_k_elements([1, 2, 3], 3))
# Expected: [3, 2, 1]