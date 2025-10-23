# Day 16: Trees & Comprehensive Project Reference

## Date: October 23, 2025

---

## Part 1: Mini Review Session

### Overview

Completed mini "Wax On Wax Off" review of Days 13-15 data structures to maintain retention.

### Structures Reviewed

**18 exercises completed:**
- Stack (4 methods)
- Queue (4 methods)
- Singly Linked List (5 methods)
- Doubly Linked List (4 methods)

### Common Mistakes Corrected

1. **Mixing list-based vs node-based structures**
   - Stack/Queue use `self.items` (list)
   - LinkedList uses `self.head` (nodes)

2. **Forgetting return statements**
   ```python
   # ❌ Wrong
   if not self.is_empty():
       self.items.pop()
   
   # ✓ Right
   if not self.is_empty():
       return self.items.pop()

1. Missing self parameter
# ❌ Wrong
def push(item):

# ✓ Right
def push(self, item):

2. Syntax errors
- Brackets vs parentheses: self.items[-1] not self.items(-1)
- Missing commas in parameters

- - -

Part 2: Trees - Hierarchical Data Structure

What is a Tree?

A tree is a hierarchical data structure with nodes connected in parent-child relationships.

Visual:
10              ← Root
       /  \
      5    15           ← Children
     / \   / \
    3   7 12  20       ← Leaves

Key Terminology

Root:
- Top node (10)
- Parent: Node with children (10, 5, 15)
- Child: Node below parent
- Leaf: Node with no children (3, 7, 12, 20)
- Siblings: Nodes with same parent (5 and 15)
- Height: Longest path from root to leaf
- Level: Distance from root (root is level 0)

- - -

Binary Tree

A tree where each node has at most 2 children (left and right).

Node Structure:
class TreeNode:
    def __init__(self, data):
        self.data = data      # The value
        self.left = None      # Left child
        self.right = None     # Right child

Comparison:
# LinkedList Node (1 pointer)
class Node:
    self.data = data
    self.next = None

# Tree Node (2 pointers)
class TreeNode:
    self.data = data
    self.left = None
    self.right = None

- - -

Binary Search Tree (BST)

A special binary tree with ordering property:
- Left child < Parent
- Right child > Parent

Example:
10
       /  \
      5    15      ← 5 < 10 < 15
     / \   / \
    3   7 12  20   ← All maintain order

- - -

BST Implementation

TreeNode Class:
class TreeNode:
    def __init__(self, data):
        self.data = data        # The value
        self.left = None        # Left child (smaller values)
        self.right = None       # Right child (larger values)

BinarySearchTreeClass:
class BinarySearchTree:
    def __init__(self):
        self.root = None        # Start with empty tree

Insert Method:
def insert(self, data):
    """Insert a new value into the BST"""
    if self.root is None:
        self.root = TreeNode(data)    # First node becomes root
    else:
        self._insert_recursive(self.root, data)

def _insert_recursive(self, node, data):
    """Helper method to insert recursively"""
    if data < node.data:              # Go left if smaller
        if node.left is None:
            node.left = TreeNode(data)
        else:
            self._insert_recursive(node.left, data)
    else:                              # Go right if larger
        if node.right is None:
            node.right = TreeNode(data)
        else:
            self._insert_recursive(node.right, data)

how it works:
Insert 10, 5, 15, 3, 7:

Step 1: 10 becomes root
    10

Step 2: 5 < 10, go left
    10
   /
  5

Step 3: 15 > 10, go right
    10
   /  \
  5    15

Step 4: 3 < 10, go left; 3 < 5, go left
    10
   /  \
  5    15
 /
3

Step 5: 7 < 10, go left; 7 > 5, go right
    10
   /  \
  5    15
 / \
3   7

Search Method:
def search(self, data):
    """Search for a value in the BST"""
    return self._search_recursive(self.root, data)

def _search_recursive(self, node, data):
    """Helper method to search recursively"""
    if node is None:                    # Not found
        return False
    
    if data == node.data:               # Found it!
        return True
    elif data < node.data:              # Search left
        return self._search_recursive(node.left, data)
    else:                                # Search right
        return self._search_recursive(node.right, data)

Example search for 7:
Start at 10
7 < 10? Yes → Go left to 5
7 < 5? No → Go right to 7
7 == 7? Yes → Found! Return True

This is FAST! Each comparision eliminates half the tree.

- - -

Tree Traversal

Three ways to visit all nodes:

1. In-order (Left -> Root -> Right)
def inorder(self, node):
    """Visit left, then root, then right"""
    if node:
        self.inorder(node.left)         # Visit left subtree
        print(node.data, end=" ")       # Visit root
        self.inorder(node.right)        # Visit right subtree

result: prints value in sorted order!
Tree:     10
         /  \
        5    15
       / \
      3   7

In-order: 3 5 7 10 15  ← Sorted!

2. Pre_order (Root -> Left -> Right)
def preorder(self, node):
    """Visit root, then left, then right"""
    if node:
        print(node.data, end=" ")       # Visit root first
        self.preorder(node.left)        # Visit left
        self.preorder(node.right)       # Visit right

Result: 10 5 3 7 15

3. Post_order (Left -> Right -> Root)
def postorder(self, node):
    """Visit left, then right, then root"""
    if node:
        self.postorder(node.left)       # Visit left
        self.postorder(node.right)      # Visit right
        print(node.data, end=" ")       # Visit root last

Result: 3 7 5 15 10

- - -

Key Conpcepts
1. Recurusion - Trees natually use recursion (each subtree is also a tree)
2. BST Property - Left < Parent < Right (maintained during insert)
3. Traversal Orders - Different orders give different results
4. In-Order Special - Always gives sorted output for BST
5. Base Cases - Always check if node is None
6. Return Statements - Must return results from recursive calls

- - -

Common Patterns

Recursive Insert Pattern:
if data < node.data:
    if node.left is None:
        node.left = TreeNode(data)
    else:
        self._insert_recursive(node.left, data)
else:
    if node.right is None:
        node.right = TreeNode(data)
    else:
        self._insert_recursive(node.right, data)

Recursive Search Pattern:
if node is None:
    return False
if data == node.data:
    return True
elif data < node.data:
    return self._search_recursive(node.left, data)
else:
    return self._search_recursive(node.right, data)

Traversal Pattern:
if node:
    self.inorder(node.left)    # Process left
    print(node.data)           # Process current
    self.inorder(node.right)   # Process right

- - -

Part 3: Task Priority System Project

Overview

Built a comprehensive system combining all 4 data structures to manage tasks with priorities.

System Architecture:
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __str__(self):
        return f"{self.name} (Priority: {self.priority})"

class TaskPrioritySystem:
    def __init__(self):
        self.priority_tree = BinarySearchTree()  # BST for priority lookup
        self.pending = Queue()                    # Pending tasks (FIFO)
        self.completed = Stack()                  # Completed tasks (LIFO)
        self.history = LinkedList()               # All tasks ever

- - -

How Each Structure is Used

1. Binary Search Tree - Priority Lookup:
def add_task(self, name, priority):
    new_task = Task(name, priority)
    self.priority_tree.insert(priority)  # Store priority for fast lookup
    # ...

def find_by_priority(self, priority):
    return self.priority_tree.search(priority)  # Fast O(log n) search

def show_priorities_sorted(self):
    self.priority_tree.inorder(self.priority_tree.root)  # Sorted output

Why BST: Fast Priority lookup and sorted diaplay

2. Queue - Pending Tasks (FIFO):
def add_task(self, name, priority):
    new_task = Task(name, priority)
    self.pending.enqueue(new_task)  # Add to back of line
    # ...

def complete_next(self):
    task = self.pending.dequeue()  # Remove from front (FIFO)
    self.completed.push(task)
    return task

Why Queue: First task added is first to be completed

3. Stack - Completed Task (LIFO):
def complete_next(self):
    task = self.pending.dequeue()
    self.completed.push(task)  # Add to top of stack
    return task

def undo_completion(self):
    task = self.completed.pop()  # Remove from top (LIFO)
    self.pending.enqueue(task)   # Put back in pending
    return task

Why Stack: Can undo last aompletion (most recent first)

4. Linked List - Task History:
def add_task(self, name, priority):
    new_task = Task(name, priority)
    self.history.append(new_task)  # Permanent record
    # ...

Why LiinkedList: Permanent chronological record of all tasks

- - - 

Complete Methods:
def add_task(self, name, priority):
    """Add new task to all structures"""
    new_task = Task(name, priority)
    self.priority_tree.insert(priority)
    self.pending.enqueue(new_task)
    self.history.append(new_task)

def complete_next(self):
    """Complete next pending task"""
    task = self.pending.dequeue()
    self.completed.push(task)
    return task

def undo_completion(self):
    """Undo last completion"""
    task = self.completed.pop()
    self.pending.enqueue(task)
    return task

def find_by_priority(self, priority):
    """Check if priority exists"""
    return self.priority_tree.search(priority)

def show_priorities_sorted(self):
    """Show all priorities in sorted order"""
    self.priority_tree.inorder(self.priority_tree.root)

def show_pending(self):
    """Show pending tasks"""
    if self.pending.is_empty():
        print("  No pending tasks")
    else:
        for task in self.pending.items:
            print(f"  - {task}")

def show_completed(self):
    """Show completed tasks"""
    if self.completed.is_empty():
        print("  No completed tasks")
    else:
        for task in self.completed.items:
            print(f"  - {task}")

- - -

Example Usage:
system = TaskPrioritySystem()

# Add tasks
system.add_task("Fix critical bug", 90)
system.add_task("Write documentation", 50)
system.add_task("Code review", 70)
system.add_task("Update tests", 60)

# View pending (Queue - FIFO order)
system.show_pending()
# Output:
#   - Fix critical bug (Priority: 90)
#   - Write documentation (Priority: 50)
#   - Code review (Priority: 70)
#   - Update tests (Priority: 60)

# View priorities sorted (BST - in-order)
system.show_priorities_sorted()
# Output: 50 60 70 90

# Complete next task (Queue - first in, first out)
task = system.complete_next()
# Completes: Fix critical bug

# View completed (Stack - LIFO)
system.show_completed()
# Output:
#   - Fix critical bug (Priority: 90)

# Undo (Stack - last in, first out)
system.undo_completion()
# Puts "Fix critical bug" back in pending

# Search by priority (BST - fast lookup)
system.find_by_priority(70)  # True

- - -

Key Learnings:

1. Combining Data Structures
- Each structure serves a specific purpose
- Choose based on access pattern needed
- Can use multiple structures for same data

2. Structure Selection
- BST: Fast lookup, sorted output
- Queue: Maintain order, FIFO
- Stack: Undo Functionality, LIFO
- LinkedList: Permanent record

3. Object-Oriented Design
- Task class encapsulates data
- __str__ method for display
- System class coordinates structures

4. Display Methods
- Direct list printing shows object references
- Loop Through items and use __str__ for proper display
- Check for empty before displaying

- - - 

Common Issues Encountered

Issue 1: BST Can't Compare Objects
# ❌ Wrong - Task objects can't be compared
self.priority_tree.insert(new_task)

# ✓ Right - Insert just the priority number
self.priority_tree.insert(priority)

Issue 2: Display Shows Object References
# ❌ Wrong - prints <Task object at 0x...>
print("Queue:", self.items)

# ✓ Right - loop and use __str__
for task in self.pending.items:
    print(f"  - {task}")

Issue 3: Forgetting Return Statements
# ❌ Wrong
def find_by_priority(self, priority):
    self.priority_tree.search(priority)

# ✓ Right
def find_by_priority(self, priority):
    return self.priority_tree.search(priority)

- - - 

Summary

Data Structures Mastered (5 total)
1. ✅ Stack (LIFO)
2. ✅ Queue (FIFO)
3. ✅ Singly Linked List
4. ✅ Doubly Linked List
5. ✅ Binary Search Tree

Key Concepts
- Trees: Hierarchical structure with parent-child relationships
- BST Property: Left < Parent < Right
- Recursion: Natural for Tree operations
- Traversal: In-order gives sorted output
- Combining Structures: Each serves specific purpose
- Object Design: Encapsulation and display methods

Skills Developed
✅ Recursive thinking
✅ Tree navigation
✅ Structure selection
✅ System design
✅ Object-oriented programming
✅ Combining multiple structures

- - - 

End of Day 16 Reference