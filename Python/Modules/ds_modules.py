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

class Queue:
    def __init__(self):
        self.items = []
  
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)     # Add to rear
    
    def dequeue(self):
        """Remove and return front item"""
        if not self.is_empty():
            return self.items.pop(0)  # Remove from front
        return None
    
    def front(self):
        """Return front item without removing"""
        if not self.is_empty():
            return self.items[0]    # Show front
        return None
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0     # Is it empty
    
    def size(self):
        """Return number of items"""
        return len(self.items)      # How many items in queue
    
    def display(self):
        """Show all items"""
        print("Queue:", self.items)     # Show everything

class Node:
    def __init__(self, data):
        self.data = data    # Store the value
        self.next = None    # Pointer to next node (starts as None)

class LinkedList:
    def __init__(self):
        self.head = None    # First node (starts empty)
    
    def append(self, data):
        """Add node to end"""
        new_node = Node(data)    # Create new node
        
        # If list is empty
        if self.head is None:
            self.head = new_node    # Make it the first node
            return
        
        # Traverse to end
        current = self.head    # Start at beginning
        while current.next:    # While there's a next node
            current = current.next    # Move to next
        
        # Add new node at end
        current.next = new_node    # Last node points to new node
    
    def display(self):
        """Print all nodes"""
        current = self.head    # Start at beginning
        while current:    # While there's a node
            print(current.data, end=" → ")    # Print its data
            current = current.next    # Move to next
        print("None")    # End of list
    
    def length(self):
        """Count nodes"""
        count = 0    # Start counter
        current = self.head    # Start at beginning
        while current:    # While there's a node
            count += 1    # Increment counter
            current = current.next    # Move to next
        return count    # Return total
    
    def prepend(self, data):
        """Add node to beginning"""
        new_node = Node(data)    # Create new node
        new_node.next = self.head    # Point new node to current head
        self.head = new_node    # Make new node the head

    def insert_after(self, target_data, new_data):
        """Insert new node after node with target_data"""
        current = self.head    # Start at beginning
        while current:    # While there's a node to check
            if current.data == target_data:    # Found target node
                new_node = Node(new_data)    # Create new node
                new_node.next = current.next    # New node points to what target pointed to
                current.next = new_node    # Target now points to new node
                return True    # Success
            current = current.next    # Keep looking
        return False    # Target not found

    def delete(self, data):
        """Delete first node with data"""
        # Special case: If head needs to be deleted
        if self.head and self.head.data == data:
            self.head = self.head.next    # Move head to next node
            return True    # Success
    
        # General case: Find node BEFORE the one to delete
        current = self.head    # Start at head
        while current and current.next:    # While there's a next node
            if current.next.data == data:    # Found node to delete
                current.next = current.next.next    # Skip over it
                return True    # Success
            current = current.next    # Keep looking
        return False    # Not found

    def search(self, data):
        """Check if data exists in list"""
        current = self.head    # Start at beginning
        while current:    # While there's a node
            if current.data == data:    # Found it
                return True    # Success
            current = current.next    # Keep looking
        return False    # Not found
    
class DNode:
    """Node for doubly linked list"""
    def __init__(self, data):
        self.data = data        # The value
        self.next = None        # Pointer to next node
        self.prev = None        # Pointer to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None        # First node
        self.tail = None        # Last node (for easy append)
    
    def append(self, data):
        """Add node to end"""
        new_node = DNode(data)    # Create new node
        
        if self.head is None:    # Empty list
            self.head = new_node    # Make it head
            self.tail = new_node    # And tail
            return
        
        # Add to end
        self.tail.next = new_node    # Old tail points forward to new
        new_node.prev = self.tail    # New node points back to old tail
        self.tail = new_node         # Update tail to new node
    
    def prepend(self, data):
        """Add node to beginning"""
        new_node = DNode(data)    # Create new node
        
        if self.head is None:    # Empty list
            self.head = new_node    # Make it head
            self.tail = new_node    # And tail
            return
        
        # Add to beginning
        new_node.next = self.head    # New node points forward to old head
        self.head.prev = new_node    # Old head points back to new node
        self.head = new_node         # Update head to new node
    
    def display_forward(self):
        """Print from head to tail"""
        current = self.head    # Start at head
        while current:    # While there's a node
            print(current.data, end=" ⇄ ")    # Print data
            current = current.next    # Move forward
        print("None")
    
    def display_backward(self):
        """Print from tail to head"""
        current = self.tail    # Start at tail
        while current:    # While there's a node
            print(current.data, end=" ⇄ ")    # Print data
            current = current.prev    # Move backward
        print("None")
    
    def delete(self, data):
        """Delete node with data"""
        current = self.head    # Start at head
        
        while current:    # While there's a node
            if current.data == data:    # Found it
                # Update previous node's next pointer
                if current.prev:
                    current.prev.next = current.next
                else:  # Deleting head
                    self.head = current.next
                
                # Update next node's prev pointer
                if current.next:
                    current.next.prev = current.prev
                else:  # Deleting tail
                    self.tail = current.prev
                
                return True    # Success
            current = current.next    # Keep looking
        return False    # Not found