# Day 14: Linked Lists Reference

## Date: October 21, 2025

---

## What is a Linked List?

A **Linked List** is a data structure where elements (nodes) are connected by pointers/references, not stored in contiguous memory like arrays.

**Key Difference from Arrays:**
- **Array:** Elements stored together in memory, fixed size
- **Linked List:** Elements scattered in memory, connected by pointers, dynamic size

---

## Part 1: Singly Linked Lists

### Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data    # The value
        self.next = None    # Pointer to next node

Visual:
[Data|Next] → [Data|Next] → [Data|Next] → None
 Head                         Tail

- - -

Basic LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None    # First node
    
    def append(self, data):
        """Add node to end"""
        new_node = Node(data)    # Create new node
        
        if self.head is None:    # Empty list
            self.head = new_node    # Make it first
            return
        
        current = self.head    # Start at beginning
        while current.next:    # Find last node
            current = current.next
        current.next = new_node    # Add to end
    
    def display(self):
        """Print all nodes"""
        current = self.head    # Start at beginning
        while current:    # While there's a node
            print(current.data, end=" → ")    # Print data
            current = current.next    # Move to next
        print("None")
    
    def length(self):
        """Count nodes"""
        count = 0    # Start counter
        current = self.head    # Start at beginning
        while current:    # While there's a node
            count += 1    # Increment
            current = current.next    # Move to next
        return count

- - -

Common Operations

1. Prepend (Add to Beginning)
def prepend(self, data):
    """Add node to beginning"""
    new_node = Node(data)    # Create new node
    new_node.next = self.head    # Point to current head
    self.head = new_node    # Make it new head

Visual:
Before: [10] → [20] → [30]
After:  [5] → [10] → [20] → [30]
         ↑ new head

- - -

2. Insert After
def insert_after(self, target_data, new_data):
    """Insert new node after node with target_data"""
    current = self.head    # Start at beginning
    while current:    # Look for target
        if current.data == target_data:    # Found it
            new_node = Node(new_data)    # Create new node
            new_node.next = current.next    # Point to what target pointed to
            current.next = new_node    # Target points to new node
            return True
        current = current.next    # Keep looking
    return False    # Not found

Visual:
Insert 25 after 20:
Before: [10] → [20] → [30]
After:  [10] → [20] → [25] → [30]

- - -

3. Delete
def delete(self, data):
    """Delete first node with data"""
    # Special case: Delete head
    if self.head and self.head.data == data:
        self.head = self.head.next    # Move head forward
        return True
    
    # General case: Find node BEFORE the one to delete
    current = self.head    # Start at head
    while current and current.next:    # While there's a next
        if current.next.data == data:    # Found it
            current.next = current.next.next    # Skip over it
            return True
        current = current.next    # Keep looking
    return False    # Not found

Visual:
Delete 20:
Before: [10] → [20] → [30]
After:  [10] ────────→ [30]
         ↑ skips over 20

Why check current.next?
- Need to update pointer of node BEFORE the one we're deleting
- Can't delete a node without access to the previous one

- - -

4. Search
def search(self, data):
    """Check if data exists"""
    current = self.head    # Start at beginning
    while current:    # While there's a node
        if current.data == data:    # Found it
            return True
        current = current.next    # Keep looking
    return False    # Not found

- - -

The Traversal Pattern

Key pattern used in all operations:
current = self.head    # Start at beginning
while current:    # While there's a node
    # Do something with current
    current = current.next    # Move to next

- - -

Part 2: Doubly Linked Lists

DNode Structure
current = self.head    # Start at beginning
while current:    # While there's a node
    # Do something with current
    current = current.next    # Move to next

Visual:
None ← [Prev|Data|Next] ⇄ [Prev|Data|Next] ⇄ [Prev|Data|Next] → None
       Head                                    Tail

- - -

DoublyLinkedList Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None    # First node
        self.tail = None    # Last node
    
    def append(self, data):
        """Add node to end"""
        new_node = DNode(data)    # Create new node
        
        if self.head is None:    # Empty list
            self.head = new_node    # Make it head
            self.tail = new_node    # And tail
            return
        
        # Add to end
        self.tail.next = new_node    # Old tail points forward
        new_node.prev = self.tail    # New node points back
        self.tail = new_node    # Update tail
    
    def prepend(self, data):
        """Add node to beginning"""
        new_node = DNode(data)    # Create new node
        
        if self.head is None:    # Empty list
            self.head = new_node    # Make it head
            self.tail = new_node    # And tail
            return
        
        # Add to beginning
        new_node.next = self.head    # New node points forward
        self.head.prev = new_node    # Old head points back
        self.head = new_node    # Update head
    
    def display_forward(self):
        """Print from head to tail"""
        current = self.head    # Start at head
        while current:    # While there's a node
            print(current.data, end=" ⇄ ")
            current = current.next    # Move forward
        print("None")
    
    def display_backward(self):
        """Print from tail to head"""
        current = self.tail    # Start at tail
        while current:    # While there's a node
            print(current.data, end=" ⇄ ")
            current = current.prev    # Move backward
        print("None")

- - -

Delete in Doubly Linked List
def delete(self, data):
    """Delete node with data"""
    current = self.head    # Start at head
    
    while current:    # While there's a node
        if current.data == data:    # Found it
            
            # CASE 1: Update previous node (or head)
            if current.prev:    # If there's a previous node
                current.prev.next = current.next    # Skip current
            else:    # Deleting head
                self.head = current.next    # Move head forward
            
            # CASE 2: Update next node (or tail)
            if current.next:    # If there's a next node
                current.next.prev = current.prev    # Point back
            else:    # Deleting tail
                self.tail = current.prev    # Move tail backward
            
            return True
        current = current.next    # Keep looking
    return False

Three Cases:
1. Delete HEAD: Update self.head
2. Delete TAIL: Update self.tail
3. Delete MIDDLE: Update both surrounding pointers

- - -

Singly vs Doubly Linked Lists

| Feature | Singly | Doubly |

|---------|--------|--------|

| Pointers per node

| 1 (next) | 2 (prev, next) |

| Traverse forward

| ✅ Yes | ✅ Yes |

| Traverse backward

| ❌ No | ✅ Yes |

| Memory

| Less | More |

| Delete complexity

| Need previous | Have previous |

| Use case

| Simple lists | Navigation (back/forward) |

- - -

Array vs Linked List

| Operation | Array | Linked List |

|-----------|-------|-------------|

| Access by index

| O(1) Fast | O(n) Slow |

| Insert at end

| O(1) Fast | O(n) Slow* |

| Insert at beginning

| O(n) Slow | O(1) Fast |

| Insert in middle

| O(n) Slow | O(1) Fast |

|

Delete | O(n) Slow | O(1) Fast

|

| Search

| O(n) | O(n) |

| Memory

| Contiguous | Scattered |

| Size

| Fixed/expensive resize | Dynamic |

*Need to traverse to end (unless you keep tail pointer)

Once you've found the position

- - -

When to Use Linked Lists

Use Linked Lists When:

✅ Frequent insertions/deletions
✅ Don't know size in advance
✅ Don't need random access
✅ Need dynamic size
✅ Memory fragmentation is okay 

Use Arrays When:

✅ Need fast random access
✅ Know size in advance
✅ Few insertions/deletions
✅ Need contiguous memory
✅ Cache performance matters

- - -

Real-World Applications

Singly Linked Lists:
- Undo functionality - Stack of states
- Music playlist - Sequential playback
- Image viewer - Next image only
- Hash table chaining - Collision resolution

Doubly Linked Lists:
- Browser history - Back and forward buttons
- Text editor - Cursor movement
- LRU Cache - Least recently used
- Navigation systems - Previous/next

- - -

Common Patterns

Pattern 1: Traversal
current = self.head
while current:
    # Process current
    current = current.next

Pattern 2: Find Last Node
current = self.head
while current.next:    # Stop at last node
    current = current.next
# current is now the last node

Pattern 3: Find Node Before Target
current = self.head
while current and current.next:
    if current.next.data == target:
        # current is the node before target
        break
    current = current.next

Pattern 4: Count Nodes
count = 0
current = self.head
while current:
    count += 1
    current = current.next
return count

- - -

Practice Exercises Completed

1. ✅ Basic LinkedList - Node and LinkedList classes

2. ✅ Extended Operations - prepend, delete, search

3. ✅ Todo List - Task management with linked list

4. ✅ Browser History - Back/forward navigation with doubly linked list

- - -

Key Takeaways

1. Nodes have two parts: Data + Pointer(s)

2. Traversal is key: Must walk through list to access elements

3. Special cases matter: Empty list, head, tail

4. Pointer manipulation: Core skill for linked lists

5. Trade-offs: Dynamic size vs slower access

6. Doubly linked: More memory, more flexibility

- - -

End of Day 14 Reference

- - -
