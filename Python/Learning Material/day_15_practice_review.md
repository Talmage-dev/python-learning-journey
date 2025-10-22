# Day 15: Data Structures Practice & Review Reference

## Date: October 22, 2025

---

## Overview

Day 15 focused on **consolidating and mastering** the four data structures learned in Days 13-14 through:
1. Building a comprehensive Task Manager application
2. Targeted "Wax On Wax Off" practice sessions
3. Writing each method multiple times from memory

---

## Part 1: Task Manager Application

### Concept

Combined **three data structures** in one application:
- **Queue** - Pending tasks (FIFO)
- **Stack** - Completed tasks (LIFO - can undo)
- **LinkedList** - Permanent history

### Implementation

```python
class TaskManager:
    def __init__(self):
        self.pending = Queue()           # Tasks to do
        self.completed = Stack()         # Completed tasks
        self.history = LinkedList()      # All tasks ever added
    
    def add_task(self, task):
        """Add new task"""
        self.pending.enqueue(task)       # Add to pending queue
        self.history.append(task)        # Add to history
    
    def complete_next(self):
        """Complete the next pending task"""
        task = self.pending.dequeue()    # Remove from pending
        if task:
            self.completed.push(task)    # Add to completed
            return task
        return None
    
    def undo_completion(self):
        """Undo last completion"""
        task = self.completed.pop()      # Remove from completed
        if task:
            self.pending.enqueue(task)   # Add back to pending
            return task
        return None

Key Learning

Transfer data between structures:
# ❌ Wrong - loses the data
self.queue.dequeue()
self.stack.push()

# ✓ Right - saves and transfers
task = self.queue.dequeue()
self.stack.push(task)

- - - 

Part 2: "Wax On Wax Off" Method

The Process

For each data structure:
1. Random method selection
2. Write from memory
3. Must complete ALL methods TWICE correctly
4. Immediate feedback on mistakes
5. Move to next structure when mastered

Why This Works
1. Active Recall - Writing from memory, not copying
2. Spaced Repetition - Methods done twice with gaps
3. Pattern Recognition - See same patterns repeatedly
4. Immediate Feedback - Learn from mistakes instantly
5. Line-by-Line Understanding - Comments force comprehension

- - -

Stack Methods Mastered

push(item):
def push(self, item):
    self.items.append(item)    # Add to top (end of list)

pop():
def pop(self):
    if not self.is_empty():         # If stack not empty
        return self.items.pop()     # Remove and return top
    return None                     # Return None if empty

peek():
def peek(self):
    if not self.is_empty():         # If stack not empty
        return self.items[-1]       # Return top without removing
    return None                     # Return None if empty

is_empty():
def is_empty(self):
    return len(self.items) == 0    # True if empty, False otherwise

- - -

Queue Methods Mastered

enqueue(item):
def enqueue(self, item):
    self.items.append(item)    # Add to rear (end of list)

dequeue():
def dequeue(self):
    if not self.is_empty():         # If queue not empty
        return self.items.pop(0)    # Remove and return front
    return None                     # Return None if empty

front():
def front(self):
    if not self.is_empty():         # If queue not empty
        return self.items[0]        # Return front without removing
    return None                     # Return None if empty

is_empty():
def is_empty(self):
    return len(self.items) == 0    # True if empty, False otherwise

- - -

Singly Linked List Methods Mastered

append(data):
def append(self, data):
    new_node = Node(data)           # Create new node
    
    if self.head is None:           # If list empty
        self.head = new_node        # Make it head
        return
    
    current = self.head             # Start at beginning
    while current.next:             # Traverse to end
        current = current.next
    current.next = new_node         # Add to end

prepend(data):
def prepend(self, data):
    new_node = Node(data)           # Create new node
    new_node.next = self.head       # Point to current head
    self.head = new_node            # Make it new head

delete(data):

def delete(self, data):
    # Special case: Delete head
    if self.head and self.head.data == data:
        self.head = self.head.next  # Move head forward
        return True
    
    # General case: Find node before target
    current = self.head             # Start at beginning
    while current and current.next: # While there's a next
        if current.next.data == data:    # Found target
            current.next = current.next.next  # Skip over it
            return True
        current = current.next      # Keep looking
    return False                    # Not found

search(data):
def search(self, data):
    current = self.head             # Start at beginning
    while current:                  # While there's a node
        if current.data == data:    # Found it
            return True
        current = current.next      # Keep looking
    return False                    # Not found

display():
def display(self):
    current = self.head             # Start at beginning
    while current:                  # While there's a node
        print(current.data, end=" → ")
        current = current.next      # Move to next
    print("None")

- - -

Doubly Linked List Methods Mastered

append(data):
def append(self, data):
    new_node = DNode(data)          # Create new node
    
    if self.head is None:           # If list empty
        self.head = new_node        # Make it head
        self.tail = new_node        # And tail
        return
    
    new_node.prev = self.tail       # Point back to tail
    self.tail.next = new_node       # Tail points forward
    self.tail = new_node            # Update tail

prepend(data):
def prepend(self, data):
    new_node = DNode(data)          # Create new node
    
    if self.head is None:           # If list empty
        self.head = new_node        # Make it head
        self.tail = new_node        # And tail
        return
    
    new_node.next = self.head       # Point to head
    self.head.prev = new_node       # Head points back
    self.head = new_node            # Update head

delete(data):
def delete(self, data):
    current = self.head             # Start at beginning
    
    while current:                  # While there's a node
        if current.data == data:    # Found it
            
            # Update previous node (or head)
            if current.prev:
                current.prev.next = current.next
            else:  # Deleting head
                self.head = current.next
            
            # Update next node (or tail)
            if current.next:
                current.next.prev = current.prev
            else:  # Deleting tail
                self.tail = current.prev
            
            return True
        
        current = current.next      # Keep looking
    return False                    # Not found

display_forward():
def display_forward(self):
    current = self.head             # Start at head
    while current:                  # While there's a node
        print(current.data, end=" ⇄ ")
        current = current.next      # Move forward
    print("None")

- - -

Common Mistakes & Fixes

Mistake 1: Not Moving to Next Node
# ❌ Wrong - infinite loop
while current:
    if current.data == target:
        return True
    # Missing: current = current.next

# ✓ Right
while current:
    if current.data == target:
        return True
    current = current.next    # Move to next!

Mistake 2: Wrong Logic Check

python
# ❌ Wrong - backwards logic
if self.items:              # If has items
    return None             # Return None?

# ✓ Right
if self.items:              # If has items
    return self.items[-1]   # Return top
return None                 # Return None if empty

Mistake 3: Not Saving Returned Value
# ❌ Wrong - loses data
self.queue.dequeue()
self.stack.push()

# ✓ Right - save and transfer
item = self.queue.dequeue()
self.stack.push(item)

Mistake 4: Comparing List to Number
# ❌ Wrong
return self.items == 0      # List vs number

# ✓ Right
return len(self.items) == 0 # Length vs number

Mistake 5: Wrong Method Name
# ❌ Wrong
return self.items.remove[0]  # remove doesn't work like this

# ✓ Right
return self.items.pop(0)     # pop(0) removes and returns first

Mistake 6: Checking Wrong Node in Delete
# ❌ Wrong - can't update pointer
if current.data == data:
    current.next = current.next.next

# ✓ Right - check next, update current
if current.next.data == data:
    current.next = current.next.next

Mistake 7: Wrong Attribute Name
# ❌ Wrong
new_node.tail = self.head    # DNode has no 'tail'

# ✓ Right
new_node.next = self.head    # Use 'next'

- - -

Key Patterns Reinforced

Pattern 1: Traversal
current = self.head
while current:
    # Process current
    current = current.next

Pattern 2: Find Last Node
current = self.head
while current.next:    # Stop at last
    current = current.next
# current is now last node

Pattern 3: Check Before Access
if not self.is_empty():    # Check first
    return self.items[-1]  # Then access
return None

Pattern 4: Delete Pattern (Singly)
# Check head first
if self.head and self.head.data == data:
    self.head = self.head.next
    return True

# Then check rest
while current and current.next:
    if current.next.data == data:
        current.next = current.next.next
        return True
    current = current.next

Pattern 5: Delete Pattern (Doubly)
# Update previous (or head)
if current.prev:
    current.prev.next = current.next
else:
    self.head = current.next

# Update next (or tail)
if current.next:
    current.next.prev = current.prev
else:
    self.tail = current.prev

- - -

Optimized Learning Strategy

The Four-Step Process

1. Learn the Material 📚
- Understand concept and theory
- See visual diagrams
- Ask questions

2. See It In Action 👀
- Work through example together
- Step-by-step walkthrough
- Understand each line

3. "Wax On Wax Off" 🥋
- Write from memory
- Random order, multiple times
- Build muscle memory
- Immediate feedback

4. Apply with Exercises 💪
- Build real applications
- Combine concepts
- Solve independently

Why This Works:
Theory → Example → Practice → Application
  ↓         ↓          ↓           ↓
Understand → See → Remember → Master

Each step reinforces the previous!

- - -

Statistics

Methods Mastered
- Stack: 4 methods
- Queue: 4 methods
- Singly Linked List: 5 methods
- Doubly Linked List: 4 methods
- Total: 17 methods

Practice Sessions
- Total exercises: 44
- Each method written: 2+ times
- Success rate: 100% (after corrections)

- - -

Key Takeaways
1. Active recall - beats passive reading
2. Spaced repetition - builds long-term memory
3. Pattern recognition - comes from repetition
4. Immediate feedback - accelerates learning
5. Line-by-line understanding - creates mastery
6. Combining structures - shows real-world use

- - -

End of Day 15 Reference

- - -
