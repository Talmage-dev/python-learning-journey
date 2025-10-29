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

# Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)

print("Forward:")
dll.display_forward()   # 5 ⇄ 10 ⇄ 20 ⇄ 30 ⇄ None

print("\nBackward:")
dll.display_backward()  # 30 ⇄ 20 ⇄ 10 ⇄ 5 ⇄ None

dll.delete(20)
print("\nAfter deleting 20:")
dll.display_forward()   # 5 ⇄ 10 ⇄ 30 ⇄ None