class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add node to end"""
        new_node = Node(data)
        
        # If list is empty
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to end
        current = self.head
        while current.next:
            current = current.next
        
        # Add new node
        current.next = new_node
    
    def display(self):
        """Print all nodes"""
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
    
    def length(self):
        """Count nodes"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # 10 → 20 → 30 → None
print(f"Length: {ll.length()}")  # 3