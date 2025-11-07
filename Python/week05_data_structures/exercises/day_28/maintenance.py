"""Day 28: Maintenance - Selection sort & Singly Linked List"""

class Node:
    def __init__(self, data):
        self.data = data    # The value
        self.next = None    # Pointer to next node

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

    def prepend(self, data):
        """Add node to beginning"""
        new_node = Node(data)    # Create new node
        new_node.next = self.head    # Point to current head
        self.head = new_node    # Make it new head
    
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
    
    def display(self):
        """Print all nodes"""
        current = self.head    # Start at beginning
        while current:    # While there's a node
            print(current.data, end=" → ")    # Print data
            current = current.next    # Move to next
        print("None")
    

# Challenge mode: Selection Sort(15min), Linked List(15min)

# Slelection Sort:
# Time Start: 11:00am
# Time Finished: 11:15am
# Task 1)
def selection_sort(ar):
    n = len(ar)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if ar[j] < ar[min_index]:
                min_index = j
        if min_index != i:
            ar[i], ar[min_index] = ar[min_index], ar[i]
    return ar

# Task 2)
arr1 = [64, 25, 12, 22, 11]
# Sort it using your selection sort
print(selection_sort(arr1))

# Task 3)
arr2 = [64, 25, 12, 22, 11]
# Modify to sort in descending order (largest first)
def reverse(ar):
    stack = []
    result = []
    sort = selection_sort(ar)
    for num in sort:
        stack.append(num)
    for num in stack:
        result.append(stack.pop())
    return result
print(reverse(arr2))

# Task 4)
def find_kth_smallest(arr, k):
    # Use selection sort concept to find the kth smallest element
    sort = selection_sort(arr)
    # Example: arr = [7, 10, 4, 3, 20, 15], k = 3
    return sort[k - 1]
    # Should return 7 (3rd smallest: 3, 4, 7...)

arr3 = [7, 10, 4, 3, 20, 15] 
k = 3

print(find_kth_smallest(arr3, k))

# Linked List:
# Start: 11:15am
# Finished: 

class Node:
    def __init__(self, data):
        self.data = data    # The value
        self.next = None    # Pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        current = self.head
        while current:
            current = current.next
        current.next = new_node
    
    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        return None
    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")

    # 4min left