""" Day 14: Linked Lists - Dynamic Data Structure """

# Practice Exercise 1: Build Node and LinkedList
# Practice Exercise 2: Add more Methods

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

# # Test 1:
# ll = LinkedList()
# ll.append(5)
# ll.append(10)
# ll.append(15)
# ll.display()
# print(f"Length: {ll.length()}")

# Test 2:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.display()  # 5 → 10 → 20 → 30 → None

ll.delete(20)
ll.display()  # 5 → 10 → 30 → None

print(ll.search(10))  # True
print(ll.search(99))  # False